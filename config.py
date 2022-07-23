import json
import os.path
from os.path import exists, expanduser

roaming = expanduser("~") + "\\AppData\\Roaming\\Guild Wars 2"
configPath = f'{roaming}\\arcdpsupdateconfig.json'


def initconfig():
    defaults = {'gw2path': '', 'lastRun': ''}
    if exists(configPath):
        return print(f'{configPath} already exists, skipping')

    open(configPath, 'x').close()
    with open(configPath, 'w') as conf:
        conf.write(json.dumps(defaults))


def getconfig():
    if not exists(configPath):
        return {}
    with open(configPath, 'r') as conf:
        try:
            return json.loads(conf.read())
        except json.JSONDecodeError:
            conf.close()
            print("Config Seems to be empty, deleting and creating new")
            delconfig()
            initconfig()
            return {}

def delconfig():
    print(f'Deleting config.json at {configPath}')
    os.remove(configPath)


def getoption(option):
    config = getconfig()
    if option not in config:
        return print(f'{option} is not in config, maybe we should add it before reading it?')
    return config[option]


def setoption(option, value):
    config = getconfig()

    config[option] = value

    with open(configPath, 'w') as conf:
        conf.write(json.dumps(config))
