import json

def pretty(json_obj):
    return json.dumps(json_obj,indent=4,sort_keys=True)

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"read_file failed: {e}")
