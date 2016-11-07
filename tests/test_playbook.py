#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import pymysql as m
import random
import shlex
import string
import sys
import subprocess
import time

# Global Variables
version = "{}".format(os.getenv('MYSQL_VERSION'))
ans_run = 'ansible-playbook -b -i inventory playbooks/main.yml -l localhost --connection=local --extra-vars '
ans_env = "version=" + version
my_user = 'testing'
my_pass = 'testing'
my_host = 'localhost'
databases = ['mysql_test_one', 'mysql_test_two', 'mysql_test_three']
test_tables = ['test_table_one', 'test_table_two', 'test_table_three']


class TestPlaybooks():

    def big_string(self, chars):
        return ''.join(random.choice(string.ascii_letters)
                       for _ in range(chars))

    def run_ansible(self, run):
        '''We should be able to run an ansible playbook'''
        try:
            args = shlex.split(run)
            p1 = subprocess.Popen(args, stdout=subprocess.PIPE)
            output = p1.communicate()[0]
            for line in output.splitlines(True):
                if 'ok=' in line:
                    status = line
            (host, colon, ok, changed, unreachable, failed) = status.split()
            ok_count = int(ok.split('=')[1])
            changed_count = int(changed.split('=')[1])
            unreachable_count = int(unreachable.split('=')[1])
            failed_count = int(failed.split('=')[1])

        except Exception as e:
            print ('Ansible Run Failed: (%s)' % e)
            return (False, output)

        if failed_count > 0:
            print ('Ansible Run Failed: (%s)' % output)
            return (False, output)

        return (True, output)

    def test_playbook_mysql(self):
        '''We should be able to install MySQL (with and without --force)'''
        run_string = ans_run + '"env=travis force=true ' + ans_env + '"'

        result, output = self.run_ansible(run_string)
        assert (result is True, output)

        run_string = ans_run + '"env=travis ' + ans_env + '"'

        result, output = self.run_ansible(run_string)
        assert (result is True, output)

    def connection(self):
        try:
            self.conn = m.connect(my_host, my_user, my_pass)

        except Exception as e:
            print ('Get Connection Failed: (%s)' % e)
            return(False)
        return(self.conn)

    def test_connection(self):
        '''We should be able to create a connection in prep for mysql tests'''

        assert (self.connection() is not False)

    def test_version(self):
        '''We should be able to get the mysql version'''
        db = self.connection()
        sql = "show global variables like 'version';"
        try:
            with db as cursor:
                cursor.execute(sql)
                row = cursor.fetchone()
                while row is not None:
                    if version in row:
                        return(True)
                    row = cursor.fetchone()

        except Exception as e:
            print ('Get Version Failed: (%s)' % e)
            return(False)
        return(True)

    def test_database_creates(self):
        '''We should be able to create databases'''
        db = self.connection()
        created = 0
        for database in databases:
            cr_db = 'create database if not exists %s;' % database
            try:
                with db as cursor:
                    cursor.execute(cr_db)
                created += 1

            except Exception as e:
                print ('Create Database Failed: (%s)' % e)
        assert (created == 3)

    def test_create_tables(self):
        '''We should be able to create tables'''
        db = self.connection()
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
        assert (created == 9)

    def test_inserts(self):
        '''We should be able to insert data into tables'''
        inserts = 10
        inserted = 0
        db = self.connection()
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for ins in range(inserts):
                    my_text = self.big_string(15)
                    sql = "insert into %s (name) values ('%s');" % (new_table, my_text)
                    try:
                        with db as cursor:
                            cursor.execute(sql)
                            inserted += 1

                    except Exception as e:
                        print ('Inserts Failed: (%s)' % e)
        assert (inserted == 90)

    def test_selects(self):
        '''We should be able to select data from tables'''
        selects = 10
        selected = 0
        db = self.connection()
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(selects):
                    sql = "select name from %s where id = %d;" % (new_table, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)
                            selected += 1

                    except Exception as e:
                        print ('Selects Failed: (%s)' % e)
        assert (selected == 90)

    def test_updates(self):
        '''We should be able to select data from tables'''
        updates = 10
        updated = 0
        db = self.connection()
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(1, updates + 1):
                    my_text = self.big_string(15)
                    sql = "update %s set name = '%s' where id >= %d;" % (new_table, my_text, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)
                            updated += 1

                    except Exception as e:
                        print ('Updates Failed: (%s)' % e)
        assert (updated == 90)

    def test_deletes(self):
        '''We should be able to delete data from tables'''
        deletes = 10
        deleted = 0
        db = self.connection()
        for database in databases:
            db.select_db(database)
            for new_table in test_tables:
                for get_id in range(1, deletes + 1):
                    sql = "delete from %s where id = %d;" % (new_table, get_id)
                    try:
                        with db as cursor:
                            cursor.execute(sql)
                            deleted += 1

                    except Exception as e:
                        print ('Deletes Failed: (%s)' % e)
        assert (deleted == 90)
