import importlib
import os
import command as cmds

def import_module(module):
    return importlib.import_module(str(module))

def get_listdir(dir):
    return os.listdir(dir)

def remove_end(name):
    return str(name.split('.')[0])

def get_cmds():
    return cmds.get_cmds()
