#! /usr/bin/env python

#Script to take a file and increment any of the fields in the version number or the release number.

import sys
from optparse import OptionParser

def incrementVersionNumber( version, fieldToInc ):
    fields = version.split('.')
    fields[fieldToInc-1] = str( int( fields[fieldToInc-1] ) + 1 )
    return ".".join(fields)

if(__name__ == "__main__"):
    usage = "usage: %prog [options] SPEC_FILE..."
    parser = OptionParser(usage)
    parser.add_option("-r", "--release", action="store_true", help="Increment release number")
    parser.add_option("-v", "--version", dest="version", type="int", metavar="FIELD", help="Increment version number FIELD")
    (options, args) = parser.parse_args()
    if(options.release and options.version): parser.error("You can not increment both the version number and the release number")
    if(len(args) == 0): parser.error("Incorrect number of arguments (need at least one)")
    for file in args:
        print("Updating file: " + file)
