#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/stats.py
# Author: Hai Liang Wang
# Date: 2024-01-13:07:35:48
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2024-01-13:07:35:48"

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

##########################################################################
# Testcases
##########################################################################
import unittest

# run testcase: python /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/stats.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stat(self):
        print("test_stat")
        input_file = os.path.join(curdir, os.pardir, "tmp", "002.format_file.utf8")
        input_lines = []

        with open(input_file, "r", encoding="utf-8") as fin:
            for x in fin.readlines():
                input_lines.append(json.loads(x))

        print("Total docs ", len(input_lines))

        total_message_records = 0
        total_message_texts = 0

        for x in input_lines:
            if not "title" in x:
                print("Error, title not present", x)
                sys.exit(1)

            msg_records = 1
            msg_text = len(x["title"])

            if (not "chats" in x) or (len(x["chats"]) == 0):
                print("Error, invalid chats info", x)
                sys.exit(1)
            
            msg_records = msg_records + len(x["chats"])
            for y in x["chats"]:
                msg_text = msg_text + len(y["value"])

            total_message_records = total_message_records + msg_records
            total_message_texts = total_message_texts + msg_text

            print(x["id"], x["title"])

        print("Total message records", total_message_records)
        print("Total message texts length", total_message_texts)
        print("Avg Comments", total_message_records - len(input_lines), "/", len(input_lines))

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_stat"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    test()

if __name__ == '__main__':
    main()
