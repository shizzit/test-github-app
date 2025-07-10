import json

def pretty(json_obj):
    return json.dumps(json_obj,indent=4,sort_keys=True)