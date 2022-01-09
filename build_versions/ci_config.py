import copy
import json

import yaml

from build_versions.settings import CONFIG_GENERATED_PATH, CONFIG_TEMPLATE_PATH

WORKFLOW_NAME = "build"
DEPLOY_JOB_NAME = "deploy"
RELEASE_JOB_NAME = "release"


def job_with_name(job, name):
    return isinstance(job, dict) and name in job


def generate_config(new_or_updated):
    # Read template CI config
    with open(CONFIG_TEMPLATE_PATH) as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)

    # Update config template workflow with per version jobs
    # Add deploy jobs for each new or updated version based on deploy job in template...
    # meaning if there are noe changes, there's no deploy.
    jobs = []
    version_jobs_names = []
    workflow = config["workflows"][WORKFLOW_NAME]
    for job in workflow["jobs"]:
        if isinstance(job, dict) and DEPLOY_JOB_NAME in job:
            for version in new_or_updated:
                version_job = copy.deepcopy(job)
                job_name = f"deploy_{version['key']}"
                version_job[DEPLOY_JOB_NAME]["name"] = job_name
                version_job[DEPLOY_JOB_NAME]["version_key"] = version["key"]
                version_job[DEPLOY_JOB_NAME]["version_config"] = json.dumps(version)
                version_jobs_names.append(job_name)
                jobs.append(version_job)
        elif isinstance(job, dict) and RELEASE_JOB_NAME in job and version_jobs_names:
            # Make release job depend on all others
            job[RELEASE_JOB_NAME]["requires"] = version_jobs_names
            jobs.append(job)
        else:
            jobs.append(job)

    config["workflows"][WORKFLOW_NAME] = workflow | {"jobs": jobs}

    # Write generated CI config
    with open(CONFIG_GENERATED_PATH, "w+") as fp_out:
        yaml.dump(config, fp_out, sort_keys=False)

    print("\n# New or updated versions:")
    print("\n".join(version["key"] for version in new_or_updated))
