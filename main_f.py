#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#import os
from os import walk, path
import sys
import subprocess
import re
from settings import *
from hashlib import md5


# standard scheck
def dir_exist(full_path):
    ''' принять полный путь к директории, если есть вернуть True'''
    pass


# base dirs functions
def create_raw_list():
    '''требуется один раз, при первом запуске'''
    


def check_dir_size(full_path):
    ''' принять путь к директории, вернуть размер
    :input: string  return int'''
    if os.path.isdir:
        return True
    else:
        return False

# работа с файлами
def check_type_file(fname):
    '''принять путь к файлу, вернуть его тип. можно смотреть не только на расширение'''
    pass


def create_raw_list(path_to_dir):
    ''' принять путь к директории, вернуть все её объекты '''
    f = []
    for i in walk(path_to_dir):
        f.append(i)
        #f.append('neP')
    return f


def check_resolution(fname):
    ''' если файл графический jpeg OR png получить его разрешение '''
    pass


def return_hash_file(fname):
    '''get selected file, return string md5sum'''
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def chechk_ru_lang(fname):
    ''' берем имя файла, проверяем все что выше ascii !!'''
    check_result = []
    for i in fname:
        if ord(i) > 128:
            check_result.append(1)
    
    if 1 in check_result:
        return True


## финал
# пока план такой: вызываем скрипт который отдает в темпа текстовый файл.

## работа с базой


if __name__ == '__main__':
    a = create_raw_list('/home/roman/gits/from_atkin')
    for i in a:
        print(i)
