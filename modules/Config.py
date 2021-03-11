import yaml


TEST = True


CREDENTIALS = '.credentials.yml'
with open(CREDENTIALS, "r") as file:
    content = yaml.safe_load(file)
    if TEST: TOKEN = content['acces']['token']
    else: TOKEN = content['acces']['token_test']