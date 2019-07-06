#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# в этом модуле будет свя работа с базой

from peewee import *
import datetime


# define database settings
db = SqliteDatabase('docs.sql')
'''
('docs.sql',  pragmas=(
    ('journal_mode', 'WAL'),
    ('cache_size', 10000),
    ('mmap_size', 1024 * 1024 * 32),
    ('foreign_keys',  'on')
))
'''

# define model descriptions
class docs(Model):
    fname = CharField()
    full_path = CharField()
    file_md5 = CharField()
    file_tags = CharField(null=True)
    file_type = CharField(null=True)
    notes = TextField(default=None, null=True)
    is_recognized = BooleanField(default=False)
    file_date_create = DateTimeField(null=True)
    file_add_date = DateTimeField(null=True)
    date_indexing = DateTimeField(null=True) #Э?  default=datetime.datetime.now
    file_size = IntegerField(default=None, null=True)
    file_content = TextField(index=True, null=True) # very large text from search

    class Meta:
        database = db


#create db and table
db.create_tables([docs])


# getters and setters
def get_full_path(fname):
    '''принимает имя файла, возвращаем полный путь.'''
    try:
        query = docs.get(docs.fname == fname).full_path
        return query
    except:
        return False


def get_md5(fname):
    '''принять имя файла, вернуть его md5sum'''
    try:
        print(fname)
        query = docs.get(docs.fname == fname).file_md5
        return query
    except:
        return False


def write_text(fname, text_string):
    '''принять текст, записать в базу'''
    try:
        query = docs.update(file_content=text_string).where(docs.fname==fname)
        query.execute()
        return True
    except:
        return False


def set_is_recognized(fname):
    '''принять имя дока, выставить is_recognized в  True'''
    pass


def get_all():
    '''вернуть имена всех файлов'''
    all_docs = []
    query = docs.select()
    for i in query:
        all_docs.append(i.fname)

    return all_docs


if __name__ == "__main__":
    pass
