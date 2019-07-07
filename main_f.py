#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from os import walk, path
import sys
import re
from settings import *
from hashlib import md5
from from_db import *
from PIL import Image
import pytesseract
import logging

# this is parse command-line 


# standard scheck
def dir_exist(full_path):
    ''' принять полный путь к директории, если есть вернуть True'''
    pass


def file_exist(full_path):
    ''' принять путь к файлу, проверить, что он есть '''
    pass


# base dirs functions
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


def create_final_list(raw_list):
    ''' принять вывод первой функции, создать лист из полных путей к файлами'''
    path_f = []
    for d, dirs, files in a:
        for f in files:
            path1 = path.join(d,f)
            path_f.append(path1)
    return path_f


def get_file_type(fname):
    ''' принять full_path, вернуть расширение.'''
    try:
        return fname.split('.')[-1]
    except:
        return False


def check_resolution(fname):
    ''' если файл графический jpeg OR png получить его разрешение '''
    pass


def recognize_text(fname):
    '''получаем на вход файл, распознаём текст. возвращаем текст либо None'''
    try:
        full_path = get_full_path(fname)
        tmp_text = pytesseract.image_to_string(Image.open(full_path), lang='rus')
        write_text(fname, tmp_text)
        return True
    except:
        return False


# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra')) # !! это основная часть.
def return_hash_file(fname):
    ''' get selected file, return string md5sum'''
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def check_ru_lang(fname):
    ''' берем имя файла, проверяем есть ли в нём кириллица '''
    check_result = []
    for i in fname:
        if ord(i) > 128:
            check_result.append(1)
    
    if 1 in check_result:
        return True


## финал
# пока план такой: вызываем скрипт который отдает в темпа текстовый файл.

## работа с базой
def add_values(f_name):
    new_values = docs(
        fname = f_name.split('/')[-1],
        full_path = f_name,
        file_md5 = return_hash_file(f_name),
        file_type = get_file_type(f_name)
        #file_content = recognize_text(fname)
)
    new_values.save()


def search_name(text):
    '''принять текст, извлечь подходящее имя'''
    regexp = r"[А-Я][а-я]*[\s\n][А-Я][а-я]*[\s\n][А-Я][а-я]\S*"
    text = str(text)
    #print("я модная строка {}".format(text))
    result = re.findall(regexp, text)
    if len(result) > 1:
        print("думаю, доверенность выдана на: {}".format(result[1]))
    else:
        print("не знаю на кого выдано")


if __name__ == '__main__':
    a = get_all()
    for i in a:
        print("это название документа ", i)
        b = get_document_content(i)
        search_name(b)
