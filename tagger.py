#! /usr/bin/env python3

import sys
import shelve
import getpass
import os


COLORS = {'red': '\033[31m', 'orange': '\033[38;5;166m', 'yellow': '\033[33m', 'green': '\033[32m',
          'blue': '\033[34m', 'magenta': '\033[35m'}
UNCOLORED = '\033[0m'

USERNAME = getpass.getuser()


book = shelve.open("tags")

tags = book['tags']
filedirs = book['filedirs']




def list_filedir(f):
    ...

def list_tag(tag, *args):
    ...

def listall_tags():
    for tag in tags:
        try:
            print(COLORS[tag[1]] + tag[0])
        except:
            print(tag[0])

def listall_filedirs():
    ...

def listall():
    for tag in tags:
        print()
        try:
            print(COLORS[tag[1]] + tag[0], end=f'{UNCOLORED}: ')
        except:
            print(tag[0], end=": ")

        all_filedirs = []
        for filedir in filedirs:
            if filedir[1] == tag[0]: # if file's tag is actual tag
                all_filedirs.append(filedir[0])
                
        print(*all_filedirs, sep=' • ')
        

def tag(file, tag):
    ...

def untag(file):
    ...

def create(tag, color):
    ...

def delete(tag):
    ...

def rename(old, new):
    ...

def recolor(tag, color):
    ...




COMMANDS = {
    'list': {
        'filedir': list_filedir,
        'tag': list_tag
        },
    'listall': {
        'tags': listall_tags,
        'filedirs': listall_filedirs,
        None: listall
        },
    'tag': tag,
    'untag': untag,
    'create': create,
    'delete': delete,
    'rename': rename,
    'recolor': recolor
    }

#listall_tags()
listall()

print()
#book.close()

