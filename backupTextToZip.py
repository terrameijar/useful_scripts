#!/usr/bin/env python

# backupTextToZip.py -- Walks a directory tree and archives python source files
# with .py extension as well as .txt files

import zipfile
import os
import re


def backup_text_files(folder):
    # TODO: Write a regex to match *.py and *.txt files
    # file_extension = re.compile(r'\w+\.(txt|py)$')
    # figure out the filename to be produced based on existing files

    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        print zip_filename
        if not os.path.exists(zip_filename):
            break
        number += 1

    # TODO: Get the folder name
    folder = os.path.abspath(folder)  # Make sure the folder name is absolute

    # TODO: Create a zip file
    backup_zip = zipfile.ZipFile(zip_filename,'w')

    # TODO: Walk the entire folder and compress all *.py files in the directory
    for foldername, subfolders, filenames in os.walk(folder):
        backup_zip.write(foldername)

        for filename in filenames:
            # new_base = os.path.basename(folder) +'_'
            if filename.endswith('.py') or filename.endswith('.txt'):
                backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print "Done"

backup_text_files("/home/terra/test/dir1")