# Copyright 2003 Lorenzo Gil Sanchez <lgs@sicem.biz>
#
# stp stands for Simple Template Processor (or Stupid Template Processor)
#
# It takes a file as input and dumps it to standard output. When it sees
# special tags it executes python code. For example:
#
# <!--stp:include('other-file')-->
#
# then it calls the python function include('other-file') which should be
# defined here or funny things can happen.
#
# Don't use this script for serious work.

import sys

def usage():
    print """
    Usage: python sts.py input_file > output_file
    """

def process_file(filename):
    f = file(filename)
    for line in f:
        li = line.find('<!--stp:')
        if li != -1:
            li = li + len('<!--stp:')
            ri = line.rfind('-->')
            directive = line[li:ri].strip()
            eval(directive) # this is a potential security bug.
        else:
            print line

    f.close()

def include(filename):
    process_file(filename)
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
        
    input_filename = sys.argv[1]
    process_file(input_filename)
