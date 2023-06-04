from build_versions.versions import scrape_supported_python_versions


def test_scrape_supported_python_versions():
    versions = scrape_supported_python_versions()
    assert len(versions) > 0
    first_version = versions[0]
    assert first_version.version
    assert first_version.start
    assert first_version.end
