import json
import base64

from .utils import read_file, pretty

class config:
    def __init__(self,path=None):
        config_path = "config.json" if path is None else f"{path}/config.json"
        self.config_raw = read_file(config_path).strip()
        self.config_json = json.loads(self.config_raw)
        print(pretty(self.config_json))

        self.branch = (self.config_json)["branch"]
        self.client_id = (self.config_json)["client_id"]
        self.install_id = (self.config_json)["install_id"]
        self.owner = (self.config_json)["owner"]
        self.private_key = base64.b64decode((self.config_json)["private_key_base64"])
        self.repository = (self.config_json)["repository"]
        self.workflow_id = (self.config_json)["workflow_id"]

cfg = config()

def get_config():
    return cfg
