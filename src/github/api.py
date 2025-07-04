import json
import requests

from datetime import datetime

from ..utils.config import get_config
from ..utils.utils import pretty
from ..jwt.jwt import create_jwt

config = get_config()

# https://docs.github.com/en/rest/apps/apps?apiVersion=2022-11-28#list-installations-for-the-authenticated-app
def list_installations(jwt):
    install_id = config.install_id
    url = f"https://api.github.com/app/installations"
    headers = {
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {jwt}",
        "X-GitHub-Api-Version":"2022-11-28"
    }
    print(pretty(headers))
    r = requests.get(url,headers = headers)
    r_code = r.status_code
    if r_code != 200:
        raise Exception(
            "\n".join([
                f"request to {url} failed with response code {r_code}",
                "Error:",
                pretty(r.json()),
            ])
        )
    installations = [ x["id"] for x in r.json() ]
    out = f"installations: {installations}"
    print(pretty(out))
    return out

# https://docs.github.com/en/rest/apps/apps?apiVersion=2022-11-28#get-an-installation-for-the-authenticated-app
def get_installation(jwt):
    install_id = config.install_id
    url = f"https://api.github.com/app/installations/{install_id}"
    headers = {
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {jwt}",
        "X-GitHub-Api-Version":"2022-11-28"
    }
    print(pretty(headers))
    r = requests.get(url,headers = headers)
    r_code = r.status_code
    if r_code != 200:
        raise Exception(
            "\n".join([
                f"request to {url} failed with response code {r_code}",
                "Error:",
                pretty(r.json()),
            ])
        )
    out = r.json()
    print(pretty(out))
    return out

# https://docs.github.com/en/rest/apps/apps?apiVersion=2022-11-28#create-an-installation-access-token-for-an-app
def get_access_token(jwt):
    install_id = config.install_id
    url = f"https://api.github.com/app/installations/{install_id}/access_tokens"
    headers = {
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {jwt}",
        "X-GitHub-Api-Version":"2022-11-28"
    }
    print(pretty(headers))
    r = requests.post(url,headers = headers)
    r_code = r.status_code
    if r_code != 201:
        raise Exception(
            "\n".join([
                f"request to {url} failed with response code {r_code}",
                "Error:",
                pretty(r.json()),
            ])
        )
    out = r.json()
    print(pretty(out))
    return out

# https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
def workflow_dispatch(access_token):
    branch = config.branch
    owner = config.owner
    repository = config.repository
    token = access_token["token"]
    workflow_id = config.workflow_id
    url = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{workflow_id}/dispatches"
    payload = {
        "ref": branch,
        "inputs": {
            "example": "abc"
        }
    }
    headers = {
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {token}",
        "X-GitHub-Api-Version":"2022-11-28"
    }
    print(pretty(headers))
    r = requests.post(url,data=json.dumps(payload), headers = headers)
    r_code = r.status_code
    print(r_code)
    if r_code != 204:
        raise Exception(
            "\n".join([
                f"request to {url} failed with response code {r_code}",
                "Error:",
                r.content,
            ])
        )
    return r_code

# ======================================================================

access_token = None

def create_token():
    jwt = create_jwt(config)
    list_installations(jwt)
    get_installation(jwt)

    global access_token
    access_token = get_access_token(jwt)

def check_token_expired(access_token):
    expires_at = access_token["expires_at"]
    parsed = datetime.strptime(expires_at,"%Y-%m-%dT%H:%M:%SZ")
    now = datetime.now()
    # note the parsed date should be in the future and therefore greater
    return parsed > now

def get_token():
    if access_token == None:
        create_token()

    if not check_token_expired(access_token):
        create_token()

    return access_token
