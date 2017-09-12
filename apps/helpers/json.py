import json

def from_json(filename):
    """Load JSON contents and convert them into dict."""
    with open(filename, 'r') as f:
        content = f.read()
    return json.loads(content)

def to_json(result_dict, filename):
    """Save test results to status.json"""
    with open(filename, 'w') as f:
        content = json.dumps(result_dict)
        f.write(content)
