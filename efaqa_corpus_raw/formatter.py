#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/formatter.py
# Author: Hai Liang Wang
# Date: 2024-01-07:09:05:27
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2024-01-07:09:05:27"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

import json

# Get ENV
ENVIRON = os.environ.copy()


def resolve_all_senders_info(doc):
    '''
    所有发送者信息
    '''
    all_avatars = set()

    for x in doc["chats"]:
        try:
            if x["sender"] == "audience": all_avatars.add(x["avatar"])
        except BaseException as e:
            if x["sender"] == "audience":
                all_avatars.add(x["userspace"])
            # print(e)
            # print(x)
            # sys.exit(1)

    senders_info = dict()

    ct = 1
    for x in all_avatars:
        senders_info[x] = "Audience" + str(ct)
        ct = ct + 1

    return senders_info


def parse_chats(doc):
    '''
    分析 Chats 数据
    '''
    originals = doc["chats"]

    chats = []

    senders_info = resolve_all_senders_info(doc)

    for x in originals:

        if "type" in x and x["type"] == "imageMessage": continue

        if x["sender"] == "audience":
            x["name"] = senders_info[x["avatar"] if "avatar" in x else x["userspace"]]

        if "userspace" in x: del x["userspace"]
        if "avatar" in x: del x["avatar"]
        if "type" in x: del x["type"]


        if (not "value" in x) or (not x["value"].strip()):
            continue

        chats.append(x)

    # print("parsed chats", len(chats))

    return chats


##########################################################################
# Testcases
##########################################################################
import unittest

# run testcase: python /c/Users/Administrator/chatopera/efaqa-corpus-raw/efaqa_corpus_raw/formatter.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_format(self):
        print("test_format")
        input_file = os.path.join(curdir, os.pardir, "tmp", "001.export_file.utf8")
        input_lines = []

        with open(input_file, "r", encoding="utf-8") as fin:
            for x in fin.readlines():
                input_lines.append(json.loads(x))

        print("loads docs", len(input_lines))        

        output_lines = []
        output_file = os.path.join(curdir, os.pardir, "tmp", "002.format_file.utf8")
        # 文件脱敏
        for x in input_lines:
            if "avatar" in x:
                del x["avatar"]
            if "url" in x:
                del x["url"]
            del x["project"]
            del x["spider"]
            del x["server"]
            if "crawldate" in x:
                del x["crawldate"]

            x["chats"] = parse_chats(x)

            if len(x["chats"]) == 0: continue

            output_lines.append(x)

        print("output_lines ", len(output_lines))
        with open(output_file, "w", encoding="utf-8") as fout:
            for x in output_lines:
                fout.write(json.dumps(x, ensure_ascii=False) + "\n")
        

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_format"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    test()

if __name__ == '__main__':
    main()
