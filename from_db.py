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

