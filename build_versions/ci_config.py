import copy

import yaml

from build_versions.settings import CONFIG_GENERATED_PATH, CONFIG_TEMPLATE_PATH


def job_with_name(job, name):
    return isinstance(job, dict) and name in job


def generate_config(new_or_updated):
    # Read template CI config
    with open(CONFIG_TEMPLATE_PATH) as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)

    # Update config template workflows with per version jobs
    for name, workflow in config["workflows"].items():
        if name == "version":
            continue

        # pop existing deploy and git archive job and add new ones based on the existing.
        # Meaning if there is nothing new, there is no deploy.
        jobs = []
        version_jobs_names = []
        for job in workflow["jobs"]:
            if isinstance(job, dict) and "deploy" in job:
                for version in new_or_updated:
                    version_job = copy.deepcopy(job)
                    job_name = f"deploy_{version['key']}"
                    version_job["deploy"]["name"] = job_name
                    version_job["deploy"]["version_key"] = version["key"]
                    version_jobs_names.append(job_name)
                    jobs.append(version_job)
            elif isinstance(job, dict) and "git_archive" in job:
                # Make git archive job depend on all others
                job["git_archive"]["requires"] = version_jobs_names
                jobs.append(job)
            else:
                jobs.append(job)

        config["workflows"][name] = workflow | {"jobs": jobs}

    # Write generated CI config
    with open(CONFIG_GENERATED_PATH, "w+") as fp_out:
        yaml.dump(config, fp_out, sort_keys=False)

    print("\n# New or updated versions:")
    print("\n".join(version["key"] for version in new_or_updated))
