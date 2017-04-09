# -*- coding: utf-8 -*-

# 这个是用来解析命令行参数的

import argparse

parser = argparse.ArgumentParser(description="Download topics")
parser.add_argument("--update", action="store_true", help="Update topics until yesterday.")
parser.add_argument("--all", action="store_true", help="Download all topics.")

args = parser.parse_args()

if args.update:

    print("update")

elif args.all:

    print("all")
