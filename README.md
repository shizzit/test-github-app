# github app to trigger workflows

1) create a github app noting the following: client_id, install_id and private_key_base64
2) create a config.json file at the top level of the repository. it should look as follows:
```
{
    "branch": "main",
    "client_id": "",
    "install_id": "",
    "owner": "shizzit",
    "private_key_base64": "",
    "repository": "test-github-app",
    "workflow_id": "example.yaml"
}
```
