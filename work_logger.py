#! /usr/bin/env python

import os
import datetime
import time
import pyperclip
import re
import pdb

def write_to_file():
    current_month = datetime.datetime.today().strftime("%B_%Y")
    today_file = datetime.datetime.today().strftime("%B%d.txt")

    work_logs_path = '/home/terra/Documents/foxy/docs'
    current_month_logs_dir = os.path.join(work_logs_path, current_month)

    osticket_match_object = \
        re.compile(r"""https://support.(leahscape|getfoxyproxy).(org|com)/
                       (\w+)/(\w+).+""", re.VERBOSE)
    clipboard_contents = pyperclip.paste()
    try:
        if osticket_match_object.search(clipboard_contents).group():
            osticket_url = clipboard_contents

            if not os.path.exists(current_month_logs_dir):
                os.makedirs(current_month_logs_dir)

            with open(os.path.join(current_month_logs_dir, today_file), 'a+') \
                    as log_file:
                        # Don't save duplicate data to logfile
                        tickets = log_file.readlines()
                        log_file.write(osticket_url + '\n')
            print "File created"   # Logging message, remove when done
    except AttributeError:
        pass
def main():
    pdb.set_trace()
    active = True
    while active:
        print "Program starting"   # Logging message, remove when done
        write_to_file()
        time.sleep(30)

main()
# TODO: Current code will write duplicate osticket entries to the log file. Fix