#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql as m
import json
import random
import string
import sys
import time
import unittest as t

my_user = 'testing'
my_pass = 'testing'
databases = ['mysql_test_one', 'mysql_test_two', 'mysql_test_three']
test_tables = ['test_table_one', 'test_table_two', 'test_table_three']

class test_mysql(t.TestCase):

    def big_string(self, chars):
        return ''.join(random.choice(string.ascii_letters)
                       for _ in range(chars))

    def setUp(self):
        '''We should be able to create a connection in prep for mysql tests'''

        self.conn = m.connect('localhost', my_user, my_pass)

    def create_databases(self):
        db = self.conn
        created = 0
        for database in databases:
            cr_db = 'create database if not exists %s;' % database
            try:
                with db as cursor:
                    cursor.execute(cr_db)
                created += 1

            except Exception as e:
                print ('Create Database Failed: (%s)' % e)
                t.testcase.fail('Create Database Failed')
        return (created)

    def create_tables(self):
        db = self.conn
        created = 0
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                cr_table = 'create table if not exists %s (id int not null auto_increment primary key, name varchar(20)) ;' % new_table
                try:
                    with db as cursor:
                        cursor.execute(cr_table)
                    created += 1

                except Exception as e:
                    print ('Create Table Failed: (%s)' % e)
                    t.testcase.fail('Create Table Failed')
        return (created)

    def inserts(self):
        '''We should be able to insert data into tables'''
        inserts = 10
        db = self.conn
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for ins in range(inserts):
                    my_text = self.big_string(15)
                    sql = "insert into %s (name) values ('%s');" % (new_table, my_text)
                    try:
                        with db as cursor:
                            cursor.execute(sql)

                    except Exception as e:
                        print ('Inserts Failed: (%s)' % e)
                        t.testcase.fail('Insert row failed.')
        return (inserts)

    def selects(self):
        '''We should be able to select data from tables'''
        selects = 10
        db = self.conn
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(selects):
                    sql = "select name from %s where id = %d;" % (new_table, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)

                    except Exception as e:
                        print ('Selects Failed: (%s)' % e)
                        t.testcase.fail('Select row failed.')
        return(selects) 

    def updates(self):
        '''We should be able to select data from tables'''
        updates = 10
        db = self.conn
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(updates):
                    sql = "update %s set name = '%s' where id = %d;" % (new_table, my_text, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)

                    except Exception as e:
                        print ('Selects Failed: (%s)' % e)
                        t.testcase.fail('Select row failed.')
        return(selects) 

    def deletes(self):
        '''We should be able to delete data from tables'''
        deletes = 10
        db = self.conn
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(deletes):
                    my_text = self.big_string(15)
                    sql = "delete from %s where id = %d;" % (new_table, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)

                    except Exception as e:
                        print ('Deletes Failed: (%s)' % e)
                        t.testcase.fail('Delete row failed.')
        return(deletes) 

    def test_mysql_crud_ops(self):
        '''We should be able to select, insert, delete, and update'''

        if (self.inserts) < 90:
            t.testcase.fail('Missing inserts.')
        if (self.selects) < 90:
            t.testcase.fail('Missing selects.')
        if (self.updates) < 90:
            t.testcase.fail('Missing updates.')
        if (self.deletes) < 90:
            t.testcase.fail('Missing deletes.')
