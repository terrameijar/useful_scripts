#! /usr/bin/python
#  mcb.pyw - Saves and loads pieces of text to the clipboard.
#  Usage: py.exe mcb.py save <keyword> - Saves clipboard to keyword.
#         py.exe mcb.py <keyword> - Loads keyword to clipboard
#         py.exe mcb.py list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        i = 0
        print "I have the following keywords saved in my memory: \n"
        for keyword in mcbShelf.keys():
            print i, keyword
            i += 1

    # If a keyword is parsed to the program, load it's contents to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("%s contents loaded to clipboard" % sys.argv[1])

    elif sys.argv[1] not in mcbShelf:
        print " \"%s \" keyword not recognised" % sys.argv[1]
        print " Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword."
        print "\tpy.exe mcb.pyw <keyword> - Loads keyword to clipboard"
        print "\tpy.exe mcb.pyw list - Loads all keywords to clipboard."

elif len(sys.argv) == 1:
    print " Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword."
    print "\tpy.exe mcb.pyw <keyword> - Loads keyword to clipboard"
    print "\tpy.exe mcb.pyw list - Loads all keywords to clipboard."
mcbShelf.close()