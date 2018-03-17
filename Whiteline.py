#isWhiteline

def isWhiteLine(inpstr):

    if not bool(inpstr and inpstr.strip()):
        return True
    else:
        False

import os
inpfile = input("Please enter the file name to be checked ")
if os.path.exists(inpfile):
    with open(inpfile) as ifile:
        for line in ifile.readlines():
            if isWhiteLine(line):
                pass
            else: 
                print("The line is -> "+line)
else:
    print("Please try again later")