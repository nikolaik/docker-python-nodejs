import re
from datetime import datetime
from functools import cmp_to_key

import requests
from pprint import pprint

import semver
from requests_html import HTMLSession

todays_date = datetime.now().date().isoformat()

# FIXME: Only standard Debian stretch
patch_re = r'^(\d+\.\d+\.\d+-stretch)$'
minor_re = r'^(\d+\.\d+-stretch)$'
major_re = r'^(\d+-stretch)$'
patch_pattern = re.compile(patch_re)
nodejs_wanted_tag_pattern = re.compile(f'{major_re}|{patch_re}')
python_wanted_tag_pattern = re.compile(f'{minor_re}|{patch_re}')


def _fetch_tags(package):
    # Fetch available docker tags
    result = requests.get(f'https://registry.hub.docker.com/v1/repositories/{package}/tags')
    return [r['name'] for r in result.json()]


def _latest_patch(tags, ver):
    tags = [tag for tag in tags if tag.startswith(ver) and patch_pattern.match(tag)]
    return sorted(tags, key=cmp_to_key(semver.compare), reverse=True)[0]


def scrape_supported_python_versions():
    """Scrape supported python versions (risky)"""
    versions = []
    version_table_selector = '#status-of-python-branches table'

    r = HTMLSession().get('https://devguide.python.org/')
    version_table = r.html.find(version_table_selector, first=True)
    for ver in version_table.find('tbody tr'):
        branch, _, _, first_release, end_of_life, _ = [v.text for v in ver.find('td')]
        versions.append({'version': branch, 'start': first_release, 'end': end_of_life})

    return versions


def fetch_supported_nodejs_versions():
    result = requests.get('https://raw.githubusercontent.com/nodejs/Release/master/schedule.json')
    return [{'version': ver, 'start': detail['start'], 'end': detail['end']} for ver, detail in result.json().items()]


def decide_python_versions():
    tags = [tag for tag in _fetch_tags('python') if python_wanted_tag_pattern.match(tag)]
    # Skip unreleased and unsupported
    supported_versions = [v for v in scrape_supported_python_versions() if v['start'] <= todays_date <= v['end']]

    versions = []
    for supported_version in supported_versions:
        ver = supported_version['version']
        minor = f'{ver}-stretch'
        if minor not in tags:
            print(f'Not good, {minor} not in tags, aborting...')
            exit(1)
        versions.append({'version': _latest_patch(tags, ver), 'image': minor, 'key': ver})

    return versions


def decide_nodejs_versions():
    tags = [tag for tag in _fetch_tags('node') if nodejs_wanted_tag_pattern.match(tag)]
    # Skip unreleased and unsupported
    supported_versions = [v for v in fetch_supported_nodejs_versions() if v['start'] <= todays_date <= v['end']]

    versions = []
    for supported_version in supported_versions:
        ver = supported_version['version'][1:]  # skip v prefix
        major = f'{ver}-stretch'
        if major not in tags:
            print(f'Not good, {major} not in tags, aborting...')
            exit(1)
        versions.append({'version': _latest_patch(tags, ver), 'image': major, 'key': ver})
    return versions


def main():
    # Use latest patch version from each minor
    python_versions = decide_python_versions()

    # Use latest minor version from each major
    nodejs_versions = decide_nodejs_versions()
    versions = []
    for p in python_versions:
        for n in nodejs_versions:
            key = f'python{p["key"]}-nodejs{n["key"]}'
            versions.append({
                'key': key,
                'dockerfile': f'Dockerfile-{key}',
                'python': p['key'],
                'python_image': p['image'],
                'python_image_canonical': p['version'],
                'nodejs': n['key'],
                'nodejs_image': n['image'],
                'nodejs_image_canonical': n['version']
            })

    pprint(versions)

    # TODO: Generate and commit all Dockerfiles on the format Dockerfile-python<NODE_VERSION>-nodejs<NODE_VERSION>


if __name__ == '__main__':
    main()
