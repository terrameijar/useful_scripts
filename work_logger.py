#! /usr/bin/env python
# Logs osticket URLs from the clipboard to a file

import os
import datetime
import time
import pyperclip
import re
import logging


def write_to_file():
    # Create a file in this example format: <Month><Date>.txt
    current_month = datetime.datetime.today().strftime("%B_%Y")
    today_file = datetime.datetime.today().strftime("%B%d.txt")

    # Save the log file in the work folder
    work_logs_path = '/home/terra/Documents/foxy/docs'
    current_month_logs_dir = os.path.join(work_logs_path, current_month)

    # Search only for osticket URLs in the clipboard
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
                        found = False
                        for ticket in tickets:
                            if osticket_url in ticket:
                                found = True
                                logging.info('Duplicate URL found, skipping')
                        if not found:
                                log_file.write(osticket_url + '\n')
                                logging.info('%s written to logfile'
                                             % osticket_url)
    except AttributeError:
        logging.warning("Clipboard does not contain osticket url, skipping")
        pass


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    active = True
    while active:
        logging.info("Loop starting")
        write_to_file()
        logging.info("Loop complete. Restarting after 30 secs")
        time.sleep(30)

main()
