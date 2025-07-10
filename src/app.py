from .github.api import get_token, workflow_dispatch

def run():
    response_status = workflow_dispatch(
        access_token = get_token(),
        owner = "shizzit",
        repository = "test-github-app",
        branch = "main",
        workflow_id = "example.yaml"
    )