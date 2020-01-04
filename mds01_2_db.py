import csv
import psycopg2

def create_table():

    conn_string = "dbname = 'MDS' user = 'docker' password = 'docker' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)


    cursor = conn.cursor()

    # Create TABLE in POSTGRES
    cursor.execute("""Create Table MDS01_13
                   (CARD_NUMBER varchar(30),
                    MSG_TYPE varchar(30),
                    RESP_CODE varchar(30),
                    BRANCH varchar(30),
                    FROM_ACCOUNT varchar(30),
                    DATE varchar(30),
                    TIME varchar(30),
                    TERMINAL_NO varchar(30),
                    TXN varchar(30),
                    SEQ varchar(30),
                    BASE24_AMOUNT varchar(30),
                    BASE24_FEE varchar(30)
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
    with open('mds01_csv_13.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cursor.copy_from(f, 'MDS01_13', sep=',')
    print("Data Inserted successfully")

    cursor.close()
    conn.commit()
    conn.close()


create_table()
import_2_db()