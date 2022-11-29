import psycopg2

def connect() -> None:
    conn = None
    try:
        conn = psycopg2.connect(database="fieldscrape-db-1",
                        host="fieldscrape-db-1.cnapnv5e3bss.us-east-1.rds.amazonaws.com",
                        #user="fieldscrape-db-1",
                        user ='postgres',
                        password="Seniordesign22_ci491",
                        port="5432")

        cursor = conn.cursor()

        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()