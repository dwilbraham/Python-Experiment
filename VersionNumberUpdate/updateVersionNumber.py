#! /usr/bin/env python

#Script to take a file and increment any of the fields in the version number or the release number.

import sys
import re
from optparse import OptionParser

def incrementVersionNumber( version, fieldToInc ):
    fields = version.split('.')
    fields[fieldToInc-1] = str( int( fields[fieldToInc-1] ) + 1 )
    return ".".join(fields)

def processFile( file, version, release ):
    print("Updating file: " + file)
    lines = []
    with open(file) as f:
        for line in f:
            if(version):
                match = re.match(r"^Version: +([\d\.]+)", line)
                if(match):
                    newVersion = incrementVersionNumber( match.group(1), version )
                    print( "    New version number: " + newVersion )
                    line = "Version: " + newVersion + "\n"
            match = re.match(r"^Release: +([\d]+)", line)
            if(match):
                if(release):
                    newRelease = str(int(match.group(1))+1)
                else:
                    newRelease = '1'
                print( "    New release number: " + newRelease )
                line = "Release: " + newRelease + "\n"
            lines.append(line)
    with open(file, 'w') as f:
        for line in lines:
            f.write(line)

if( __name__ == "__main__" ):
    usage = "usage: %prog [options] SPEC_FILE..."
    parser = OptionParser(usage)
    parser.add_option("-r", "--release", action="store_true", help="Increment release number")
    parser.add_option("-v", "--version", dest="version", type="int", metavar="FIELD", help="Increment version number FIELD")
    (options, args) = parser.parse_args()
    if(options.release and options.version): parser.error("You can not increment both the version number and the release number")
    if(len(args) == 0): parser.error("Incorrect number of arguments (need at least one)")
    for file in args:
        processFile( file, options.version, options.release )
