#!/usr/bin/env python3
'''
Note: when transfer to uxix , go to vi and use command :set ff:unix and :wq
'''
import os
from datetime import date, timedelta, datetime


def mds01_to_csv(set_date):
    today = date.today().strftime('%y%m%d')
    # set_date = (date.today() - timedelta(2)).strftime('%y%m%d') #for auto
    set_date = '13'  # for manual
    # set_date = set_date

    current_path = os.getcwd()
    mds01_filename = 'mds01' + set_date
    # mds01_filename = 'MD_test_' + today + '.001'
    with open(current_path + '\\' + mds01_filename, 'r') as infile:
        rawdata = infile.read()
        alldata = rawdata.splitlines()
        # print(data[2])
        header_line = 'CARD_NUMBER,' \
                      'MSG_TYPE,' \
                      'RESP_CODE,' \
                      'BRANCH,' \
                      'FROM_ACCOUNT,' \
                      'DATE,' \
                      'TIME,' \
                      'TERMINAL_NO,' \
                      'TXN,' \
                      'SEQ,' \
                      'BASE24_AMOUNT,' \
                      'BASE24_FEE' \
                      '\n'
        total_line = header_line

        for line in alldata:
            # check if the current line
            # starts with "#"
            if not line.startswith(("=", " ", "P", "R", "G", "-")):
                # data = line
                # print(data)
                new_line = line[:20].strip() + ',' + \
                           line[20:26].strip() + ',' + \
                           line[26:31].strip() + ',' + \
                           line[31:49].strip() + ',' + \
                           line[49:67].strip() + ',' + \
                           line[67:74].strip() + ',' + \
                           line[74:81].strip() + ',' + \
                           line[81:98].strip() + ',' + \
                           line[98:105].strip() + ',' + \
                           line[105:113].strip() + ',' + \
                           line[113:126].strip() + ',' + \
                           line[126:136].strip() + \
                           '\n'
                # print(new_line)
                total_line += new_line
    print(total_line)

    csv_filename = 'mds01_csv_' + set_date + '.csv'
    with open(current_path + '\\' + csv_filename, 'w', newline='') as outfile:
        outfile.write(total_line)
        print("CSV saved successfully: " + csv_filename)

    print(today + ' to_csv : today')
    print(set_date + ' to_csv: set_date')



set_date = '190220'
mds01_to_csv(set_date)
