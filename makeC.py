#!/usr/bin/env python
#    Author: Morrison
#    Date created: 16 June 2015
#    Program: makeC.py
#    This program produces a shell C program with a dated comment
#    box.  Use it whenever you create a new program, and you 
#    will know WHEN  you produced things.  The default filename
#    is moo.c.
from sys import argv
from datetime import datetime
def monthNames(n):
    x = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
    "Aug", "Sep", "Oct", "Nov", "Dec"]
    return x[n]
fileName = "moo.c" if (len(argv) < 2) else argv[1]
outFile = open(fileName, "w")
now = datetime.now()
nowString = "%s %s %s" % (now.day, monthNames(int(now.month)), now.year)
outFile.write("""/* Author: Morrison
 * Date %s
 * Date last modified: %s
 * Program: %s
 */
#include<stdio.h>
int main(int argc, char** argv)
{
    return 0;
}
""" %(nowString, nowString, fileName))
