import json

def load_events(path):
    with open(path) as f:
        for line in f:
            try:
                yield json.loads(line)
            except:
                continue

