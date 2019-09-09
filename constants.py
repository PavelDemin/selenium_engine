import json

def init():
    global INST_USER, INST_PASS
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    INST_USER = obj['user']
    INST_PASS = obj['pass']