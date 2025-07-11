# github app to trigger workflows
an example application to test triggering workflows

1) create a github app and install it
2) add permissions for the app. for triggering workflow, you only need "Repository permissions > Actions (read and write)".
3) navigate to the app page and make note of the client_id
4) while also on the app page, create and download a private key
5) convert the contents of the private key to base64
```
# on linux (bash)
cat file | base64
```
```
# on windows (powershell)
[System.Convert]::ToBase64String((Get-Content .\app_name.date.private-key.pem -Encoding Byte))
```
5) navigate to: https://github.com/settings/installations and click "Configure" on your app
6) note the install_id in the address bar. it should look something like ```https://github.com/settings/installations/{INSTALL_ID}```
7) create a config.json file at the top level of the repository. it should look as follows:
```
{
    "branch": "main",
    "client_id": "<YOUR_CLIENT_ID>",
    "install_id": "<YOUR_INSTALL_ID>",
    "owner": "<GITHUB_USER>",
    "private_key_base64": "<YOUR_PRIVATE_KEY_BASE64>",
    "repository": "test-github-app",
    "workflow_id": "example.yaml"
}
```
