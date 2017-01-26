#!/usr/bin/env python

# backupTextToZip.py -- Walks a directory tree and archives python source files
# with .py extension as well as .txt files

import zipfile
import os


def backup_text_files(folder):

    folder = os.path.abspath(folder)
    number = 1

    # Create a new zip file each time this script is run
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Get the folder name
    folder = os.path.abspath(folder)  # Make sure the folder name is absolute

    # Create a zip file
    backup_zip = zipfile.ZipFile(zip_filename,'w')

    # Walk the entire folder and compress all .py / .txt files in the directory
    for foldername, subfolders, filenames in os.walk(folder):
        backup_zip.write(foldername)

        for filename in filenames:
            if filename.endswith('.py') or filename.endswith('.txt'):
                backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print "Done"

backup_text_files(".")