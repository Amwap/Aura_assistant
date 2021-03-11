import yaml


TEST = True


CREDENTIALS = '.credentials.yml'
with open(CREDENTIALS, "r") as file:
    content = yaml.safe_load(file)
    if TEST: TOKEN = content['acces']['token_test']
    else: TOKEN = content['acces']['token']
    ADMIN = content['admin'][0]