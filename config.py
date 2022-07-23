import json
import os.path
from os.path import exists


def initconfig():
    defaults = {'gw2path': '', 'lastRun': ''}
    if exists('./config.json'):
        return print('config.json already exists, skipping')

    open('config.json', 'x').close()
    with open('config.json', 'w') as conf:
        conf.write(json.dumps(defaults))


def getconfig():
    if not exists('./config.json'):
        return {}
    with open('config.json', 'r') as conf:
        return json.loads(conf.read())


def delconfig():
    print(f'Deleting config.json at {os.path.curdir}/config.json')
    os.remove(os.path.curdir + '/config.json')


def getoption(option):
    config = getconfig()
    if option not in config:
        return print(f'{option} is not in config, maybe we should add it before reading it?')
    return config[option]


def setoption(option, value):
    config = getconfig()

    config[option] = value

    with open('config.json', 'w') as conf:
        conf.write(json.dumps(config))
