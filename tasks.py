from invoke import task
import subprocess
import json

@task
def run_local_docker(c):
    """
    Pull the latest image from Docker Hub and run the Django app locally.
    """
    print("📥 Pulling latest Docker image...")
    c.run("docker pull sallypj/p13-docker:latest")

    print("🔍 Extracting embedded commit hash...")
    try:
        output = subprocess.check_output([
            "docker", "inspect", "sallypj/p13-docker:latest"
        ])
        data = json.loads(output)
        git_commit = data[0]['Config']['Labels'].get('git_commit', 'unknown')
        print(f"🔗 Git commit: {git_commit}")
    except Exception as e:
        print(f"⚠️ Error extracting commit hash: {e}")

    print("🚀 Starting and running app on http://localhost:8000...")
    c.run("docker run -p 8000:8000 sallypj/p13-docker:latest")
