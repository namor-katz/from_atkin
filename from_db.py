#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from peewee import *
import datetime


# define database settings
db = SqliteDatabase('packages_info.sql',  pragmas=(
    ('journal_mode', 'WAL'),
    ('cache_size', 10000),
    ('mmap_size', 1024 * 1024 * 32),
    ('foreign_keys',  'on')
))


# define model descriptions
class packages(Model):
    fname = CharField()
    full_path = CharField()
    file_md5 = CharField()
    file_tags = CharField()
    file_type = CharField()
    notes = TextField()
    is_recognized = BooleanField()
    file_date_create = DateTimeField()
    file_add_date = DateTimeField()
    date_indexing = DateTimeField(default=datetime.datetime.now) #Э?
    file_size = IntegerField()
    file_content = TextField() # very large text from search
    
    class Meta:
        database = db
