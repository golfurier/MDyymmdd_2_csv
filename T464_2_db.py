import csv
import psycopg2


def create_table():

    conn_string = "dbname = 'MDS' user = 'docker' password = 'docker' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # Create TABLE in POSTGRES
    cursor.execute("""Create Table MDT464_13
                   (Message_Type_Indicator varchar(30),
                    Switch_Serial_Number varchar(30),
                    Processor__Acquirer_or_Issuer varchar(30),
                    Processor_ID varchar(30),
                    Transaction_Date date,
                    Transaction_Time_HHMMSS time,
                    PAN_Length varchar(30),
                    Primary_Account_Number_PAN varchar(30),
                    Processing_Code varchar(30),
                    Trace_Number varchar(30),
                    Merchant_Type_MCC varchar(30),
                    POS_Entry varchar(30),
                    Reference_Number varchar(30),
                    Acquirer_Institution_ID varchar(30),
                    Terminal_ID varchar(30),
                    Response_Code varchar(30),
                    Brand varchar(30),
                    Advice_Reason_Code varchar(30),
                    Intracurrency_Agreement_Code varchar(30),
                    Authorization_ID varchar(30),
                    Currency_Code_Transaction varchar(30),
                    Implied_Decimal_Transaction varchar(30),
                    Completed_Amt_Trans_Local numeric,
                    Completed_Amount_Transaction_Local_DR_CR_Indicator varchar(30),
                    Cash_Back_Amt_Local numeric,
                    Cash_Back_Amount_Local_DR_CR_Indicator varchar(30),
                    Access_Fee_Local numeric,
                    Access_Fee_Local_DR_CR_Indicator varchar(30),
                    Currency_Code_Settlement varchar(30),
                    Implied_Decimal_Settlement varchar(30),
                    Conversion_Rate_Settlement varchar(30),
                    Completed_Amt_Settlement numeric,
                    Completed_Amount_Settlement_DR_CR_Indicator varchar(30),
                    Interchange_Fee numeric,
                    Interchange_Fee_DR_CR_Indicator varchar(30),
                    Service_Level_Indicator varchar(30),
                    Response_Code_ varchar(30),
                    Filler varchar(30),
                    Positive_ID_Indicator varchar(30),
                    ATM_Surcharge_Free_Program_ID varchar(30),
                    Cross_Border_Indicator varchar(30),
                    Cross_Border_Currency_Indicator varchar(30),
                    VISA_International_Service_Assessment_ISA_Fee_Indicator varchar(30),
                    Requested_Amt_Trans_Local numeric,
                    Filler_ varchar(30),
                    Trace_Number_Adjustment_Trans varchar(30),
                    Filler__ varchar(30),
                    Settlement_Date date
                    );""")

    print("Table created successfully")
    cursor.close()
    conn.commit()
    conn.close()


def import_2_db():

    conn_string = "dbname = 'MDS' user = 'docker' password = 'docker' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    # import csv to database , by INSERT
    # with open('csv_eps_visa_tx1.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     next(reader)  # Skip the header row.
    #     for row in reader:
    #         cursor.execute(
    #             "INSERT INTO EPSVISATX1 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    #             row
    #         )
    # print("Data Inserted successfully")

    # import csv to database , by COPY
    with open('MD_csv_191213.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cursor.copy_from(f, 'MDT464_13', sep=',')
    print("Data Inserted successfully")

    cursor.close()
    conn.commit()
    conn.close()


create_table()
import_2_db()