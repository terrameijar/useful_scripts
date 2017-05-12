#! /usr/bin/env python
# Logs osticket URLs from the clipboard to a file

import os
import re
import time
import logging
import datetime
import pyperclip
import subprocess as s




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
                                logging.debug('Duplicate URL found, skipping')
                        if not found:
                                log_file.write(osticket_url + '\n')
                                logging.debug('%s written to logfile'
                                             % osticket_url)
                                s.call(['notify-send', '-i', 'emblem-default',
                                        'Ticket URL written to logfile'])
    except AttributeError:
        logging.debug("Clipboard does not contain osticket url, skipping")
        pass


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.debug("Work Logger initialised")
    s.call(['notify-send','-i', 'emblem-generic','Work Logger initialised' ])
    active = True
    while active:
        logging.debug("Loop starting")
        write_to_file()
        logging.debug("Loop complete. Restarting after 5 secs")
        time.sleep(5)

if __name__ == '__main__':
    main()
