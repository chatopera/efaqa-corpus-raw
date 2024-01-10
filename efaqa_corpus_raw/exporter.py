#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/exporter.py
# Author: Hai Liang Wang
# Date: 2024-01-06:09:28:07
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2024-01-06:09:28:07"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

# Get ENV
ENVIRON = os.environ.copy()
import json
import datetime
from pymongo import MongoClient

# Provide the connection details
hostname = '192.168.2.219'
port = 3038  # Default MongoDB port
username = None  # If authentication is required
password = None  # If authentication is required

# Create a MongoClient instance
mongodb = MongoClient(hostname, port, username=username, password=password)
db = mongodb['geili']
# Access a collection (similar to a table in relational databases)
collection = db['questions']

##########################################################################
# Testcases
##########################################################################
import unittest

# run testcase: python /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/exporter.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_export_raw(self):
        print("test_export_raw")
        print("total qa ", collection.count_documents({}))
        output_file = os.path.join(curdir, os.pardir, "tmp", "001.export_file.utf8")
        output_lines = []
        ct = 0
        for doc in collection.find({}):
            try:
                if "title" in doc and doc["title"] and "chats" in doc and len(doc["chats"]) > 0:
                    ct = ct + 1
                    # print("Ct", ct, doc["title"])
                    del doc["id"]
                    doc["id"] = str(doc["_id"])
                    del doc["_id"]
                    if "crawldate" in doc:
                        doc["crawldate"] = datetime.datetime.strftime(doc["crawldate"],'%Y-%m-%d %H:%M:%S')
                    output_lines.append(json.dumps(doc, ensure_ascii=False))
            except BaseException as e:
                print(e)
                print(doc)
                sys.exit(1)

        with open(output_file, "w", encoding="utf-8") as fout:
            for x in output_lines:
                fout.write(x.strip() + "\n")

        print("dumped lines ", len(output_lines))

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_export_raw"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    test()

if __name__ == '__main__':
    main()
    mongodb.close()