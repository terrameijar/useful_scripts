#!/usr/bin/env python

# backupToZip.py -- Copies and entire directory and it's contents into
# a zip file whose filename increments
# The default folder to be backed up is the current working directory

import zipfile
import os


def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder)  # make sure folder is absolute
    # Figure out the filename this code should use based on what
    # files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the zip file
    print "Creating %s ..." % (zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print "Adding files in %s..." % foldername
        # Add the current directory to the ZIP file.

        backup_zip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue #  don't backup the backup ZIP files

            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print "Done"


backup_to_zip(".")