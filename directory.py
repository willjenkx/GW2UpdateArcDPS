import os
from tkinter import filedialog
from tkinter import *
from os.path import exists
from config import getoption, setoption
from download import download


def choose_directory():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    while not exists(folder_selected + '/gw2-64.exe'):
        print('GW2-64.exe NOT FOUND, try again mofo')
        folder_selected = filedialog.askdirectory()
    return folder_selected


def check_directory():
    config_directory = getoption('gw2path')

    if not exists(config_directory + '/gw2-64.exe'):
        setoption('gw2path', choose_directory())


def update_file():
    data = download()
    gw2directory = getoption('gw2path')
    target = gw2directory + '/d3d11.dll'

    try:
        if exists(target):
            os.remove(target)
        open(target, 'x').close()
        with open(target, 'wb') as dll:
            dll.write(data)
    except OSError as e:
        print('Err: ', e)
        print('GW2 Must NOT be running during this process')
