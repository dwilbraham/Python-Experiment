#! /usr/bin/env python

#Script to take a file and increment any of the fields in the version number.

import sys

if __name__ == "__main__":
    print 'test'
    for file in sys.argv[1:]:
        print file,
