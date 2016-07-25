
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

environment = "dev"
config = {}
with open(os.path.join(BASE_DIR, "environment.cfg")) as f:
    environment = f.read()
    with open(os.path.join(BASE_DIR, "config-{}.json".format(environment))) as conf_file:
        string = conf_file.read()
        config = json.loads(string)
