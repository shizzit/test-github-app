import os
import json
import base64

from .utils import pretty

class config:
    def __init__(self):
        # self.owner = (self.config_json)["owner"]
        # self.branch = (self.config_json)["branch"]
        # self.repository = (self.config_json)["repository"]
        # self.workflow_id = (self.config_json)["workflow_id"]

        self.client_id = os.environ.get('GH_APP_CLIENT_ID')
        self.install_id = os.environ.get('GH_APP_INSTALL_ID')
        self.private_key_base64 = os.environ.get('GH_APP_PRIVATE_KEY_BASE64')

        self.errors = []
        if self.client_id is None:
            self.errors.append("- 'GH_APP_CLIENT_ID'")
        if self.install_id is None:
            self.errors.append("- 'GH_APP_INSTALL_ID'")
        if self.private_key_base64 is None:
            self.errors.append("- 'GH_APP_PRIVATE_KEY_BASE64'")

        if len(self.errors) != 0:
            err_str = "\n".join([
                "missing environment variable(s)!",
                "\n".join(self.errors)
            ])
            raise(Exception(err_str))

        self.private_key = base64.b64decode(self.private_key_base64)

cfg = config()

def get_config():
    return cfg
