#! /usr/bin/python
#  renameDates.py - Renames filenames with American MM-DD-YYYY format to
#  European DD-MM-YYYY format

import shutil
import os
import re

# Create a regex that matches files with the American date format
date_pattern = re.compile(r"""^(.*?)      # all text before the date
                          ((0|1)?\d)-     # one or two digits for the month
                          ((0|1|2|3)?\d)- # one or two digits for the day
                          ((19|20)\d\d)   # four digits of the year
                          (.*?)$          # all text after the date
                          """, re.VERBOSE)
# Loop over the files in the working directory
for american_filename in os.listdir('.'):
    match_object = date_pattern.search(american_filename)
    # Skip files without a date
    if match_object is None:
        continue
# Get the different parts of the filename.
    before_part = match_object.group(1)
    month_part = match_object.group(2)
    day_part = match_object.group(4)
    year_part = match_object.group(6)
    after_part = match_object.group(8)
# Form the European-style filename.
    euro_filename = before_part + day_part + '-'+ month_part + '-' + year_part + after_part
# Get the full, absolute file paths.
    absolute_working_dir = os.path.abspath('.')
    american_filename = os.path.join(absolute_working_dir, american_filename)
    euro_filename = os.path.join(absolute_working_dir, euro_filename)
# Rename the files.
    print("Renaming %s to %s ..." % (american_filename, euro_filename))
    # shutil.move(american_filename, euro_filename) # This command is dangerous uncomment after testing.
