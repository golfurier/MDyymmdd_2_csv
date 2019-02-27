#!/usr/bin/env python3
'''
Note: when transfer to uxix , go to vi and use command :set ff:unix and :wq
'''
import os
from datetime import date, timedelta, datetime
import pysftp
from time import sleep


def t464_to_csv(set_date):
    today = date.today().strftime('%y%m%d')
    # set_date = (date.today() - timedelta(2)).strftime('%y%m%d') #for auto
    # set_date = '190220'  # for manual
    set_date = set_date

    current_path = os.getcwd()
    t464_filename = 'MD' + set_date
    # t464_filename = 'MD_test_' + today + '.001'
    with open(current_path + '\\' + t464_filename, 'r') as infile:
        data = infile.read()

    my_list = data.splitlines()
    first_row = my_list[0]
    # settlement_MM = first_row[4:6]
    # settlement_DD = first_row[6:8]
    # settlement_YY = first_row[8:10]
    # settlement_date = settlement_YY + settlement_MM + settlement_DD
    settlement_date_temp = first_row[4:10]
    setobj = datetime.strptime(settlement_date_temp, '%m%d%y')
    settlement_date = setobj.strftime('%Y%m%d')

    # print(report_date)

    # for line in my_list:
    #     print(line[4:10])

    header_line = 'Message Type Indicator,' \
                 'Switch Serial Number,' \
                 'Processor - Acquirer or Issuer,' \
                 'Processor ID,' \
                 'Transaction Date,' \
                 'Transaction Time HHMMSS,' \
                 'PAN Length,' \
                 'Primary Account Number (PAN),' \
                 'Processing Code,' \
                 'Trace Number,' \
                 'Merchant Type (MCC),' \
                 'POS Entry,' \
                 'Reference Number,' \
                 'Acquirer Institution ID,' \
                 'Terminal ID,' \
                 'Response Code,' \
                 'Brand,' \
                 'Advice Reason Code,' \
                 'Intracurrency Agreement Code,' \
                 'Authorization ID,' \
                 'Currency Code—Transaction,' \
                 'Implied Decimal —Transaction,' \
                 'Completed Amt Trans—Local,' \
                 'Completed Amount Transaction—Local DR/CR Indicator,' \
                 'Cash Back Amt—Local,' \
                 'Cash Back Amount—Local DR/CR Indicator,' \
                 'Access Fee—Local,' \
                 'Access Fee—Local DR/CR Indicator,' \
                 'Currency Code—Settlement,' \
                 'Implied Decimal —Settlement,' \
                 'Conversion Rate—Settlement,' \
                 'Completed Amt—Settlement,' \
                 'Completed Amount Settlement DR/CR Indicator,' \
                 'Interchange Fee,' \
                 'Interchange Fee DR/CR Indicator,' \
                 'Service Level Indicator,' \
                 'Response Code,' \
                 'Filler,' \
                 'Positive ID Indicator,' \
                 'ATM Surcharge-Free Program ID,' \
                 'Cross-Border Indicator,' \
                 'Cross-Border Currency Indicator,' \
                 'VISA International Service Assessment (ISA) Fee Indicator,' \
                 'Requested Amt Trans—Local,' \
                 'Filler,' \
                 'Trace Number—Adjustment Trans,' \
                 'Filler,' \
                 'Settlement Date' \
                  '\n'
    # total_line = settlement_date + '\n' + header_line
    total_line = header_line
    # print(total_line)


    for line in my_list:
        if (line[:4] == 'NREC') or (line[:4] == 'FREC'):
            transaction_date_temp = line[18:24].strip()
            setobj = datetime.strptime(transaction_date_temp, '%m%d%y')
            transaction_date = setobj.strftime('%Y%m%d')
            new_line = line[:4].strip() + ',' + \
                       line[4:13].strip() + ',' + \
                       line[13:14].strip() + ',' + \
                       line[14:18].strip() + ',' + \
                       transaction_date + ',' + \
                       line[24:30].strip() + ',' + \
                       line[32:51].strip() + ',' + \
                       line[30:32].strip() + ',' + \
                       line[51:57].strip() + ',' + \
                       line[57:63].strip() + ',' + \
                       line[63:67].strip() + ',' + \
                       line[67:70].strip() + ',' + \
                       line[70:82].strip() + ',' + \
                       line[82:92].strip() + ',' + \
                       line[92:102].strip() + ',' + \
                       line[102:104].strip() + ',' + \
                       line[104:107].strip() + ',' + \
                       line[107:114].strip() + ',' + \
                       line[114:118].strip() + ',' + \
                       line[118:124].strip() + ',' + \
                       line[124:127].strip() + ',' + \
                       line[127:128].strip() + ',' + \
                       line[128:140].strip() + ',' + \
                       line[140:141].strip() + ',' + \
                       line[141:153].strip() + ',' + \
                       line[153:154].strip() + ',' + \
                       line[154:162].strip() + ',' + \
                       line[162:163].strip() + ',' + \
                       line[163:166].strip() + ',' + \
                       line[166:167].strip() + ',' + \
                       line[167:175].strip() + ',' + \
                       line[175:187].strip() + ',' + \
                       line[187:188].strip() + ',' + \
                       line[188:198].strip() + ',' + \
                       line[198:199].strip() + ',' + \
                       line[199:202].strip() + ',' + \
                       line[202:204].strip() + ',' + \
                       line[204:214].strip() + ',' + \
                       line[214:215].strip() + ',' + \
                       line[215:216].strip() + ',' + \
                       line[216:217].strip() + ',' + \
                       line[217:218].strip() + ',' + \
                       line[218:219].strip() + ',' + \
                       line[219:231].strip() + ',' + \
                       line[231:243].strip() + ',' + \
                       line[243:249].strip() + ',' + \
                       line[249:250].strip() + ',' + \
                       settlement_date + \
                       "\n"
            total_line += new_line

    # print(total_line)

    csv_filename = 'MD_csv_' + set_date + '.csv'
    with open(current_path + '\\' + csv_filename, 'w', newline='') as outfile:
        outfile.write(total_line)
        print("CSV saved successfully: " + csv_filename)

    print(today + ' to_csv : today')
    print(set_date + ' to_csv: set_date')


def auto_sftp_get(set_date):
    today = date.today().strftime('%y%m%d')
    # set_date = (date.today()-timedelta(2)).strftime('%y%m%d')
    # set_date = '190220'  # for manual
    set_date = set_date


    myHostname = "10.4.1.170"
    myUsername = "gsbss"
    myPassword = "gsb1234"
    myRemoteFile = "MD"+set_date

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
        print("Connection successfully established...")

        # Define the file that you want to download from the remote directory
        remoteFilePath = '/User/MasterCard/'+myRemoteFile

        # Define the local path where the file will be saved
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
        localFilePath = './'+myRemoteFile

        sftp.get(remoteFilePath, localFilePath)

    # connection closed automatically at the end of the with-block

    print(today + ' sftp_get : today')
    print(set_date + ' sftp_get : set_date')


def auto_sftp_put(set_date):
    today = date.today().strftime('%y%m%d')
    # set_date = (date.today()-timedelta(2)).strftime('%y%m%d')
    # set_date = '190220'  # for manual
    set_date = set_date

    myHostname = "10.4.1.170"
    myUsername = "gsbss"
    myPassword = "gsb1234"
    myLocalFile = "MD_csv_"+set_date+".csv"

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
        print("Connection successfully established...")

        # Define the file that you want to download from the remote directory
        remoteFilePath = '/User/MasterCard/'+myLocalFile

        # Define the local path where the file will be saved
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
        localFilePath = './'+myLocalFile

        sftp.put(localFilePath, remoteFilePath)

    # connection closed automatically at the end of the with-block

    print(today+' sftp_put : today')
    print(set_date+' sftp_put : set_date')


today = date.today().strftime('%y%m%d')
weekday = datetime.today().weekday()
print(weekday, type(weekday))
# weekday = 0

if weekday == 0:
    i = 2
    while i < 5:
        set_date = (date.today() - timedelta(i)).strftime('%y%m%d')
        auto_sftp_get(set_date)
        sleep(2)
        t464_to_csv(set_date)
        sleep(2)
        auto_sftp_put(set_date)
        sleep(2)
        i += 1
else:
    set_date = (date.today() - timedelta(2)).strftime('%y%m%d')
    auto_sftp_get(set_date)
    sleep(2)
    t464_to_csv(set_date)
    sleep(2)
    auto_sftp_put(set_date)
    sleep(2)

