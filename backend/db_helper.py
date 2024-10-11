# CRUD - Create, Retrieve, Update, Delete
import mysql.connector
from contextlib import contextmanager
from logging_setup  import setup_logger

logger= setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host='127.0.0.1', # or localhost as per your system MYSQL settings
        user='root',
        password="ENTER MySQL Password"
        database='expense_manager'
    )

    #checking whether connection is made or not
    if connection.is_connected():
        print('Connection is Successful')
    else:
        print('Unable to make connection with the database')

    ## for output in form of dictionary
    cursor=connection.cursor(dictionary=True)
    yield cursor

    ## for commit the action like inserting, deleting, updating, altering
    if commit:
        connection.commit()
    cursor.close()
    connection.close() # at the end to cleanup the query
    

def fetch_expense_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date= %s',(expense_date,))
        expenses=cursor.fetchall() # retruns the data in tuple format
        return expenses

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(" Delete from expenses where expense_date=%s",(expense_date,))

def insert_expense(expense_date,amount, category,notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        # First, delete any existing entry with the same expense_date, amount, and category
        cursor.execute('Delete from expenses where expense_date=%s and amount=%s and category=%s',(expense_date,amount, category))
        # Then, insert the new record
        cursor.execute('Insert into expenses (expense_date,amount, category,notes) values(%s,%s,%s,%s)',(expense_date,amount, category,notes))

def fetch_expense_summary_by_category(start_date,end_date):
    logger.info(f"fetch_expense_summary called with start date: {start_date} and end_date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("""select distinct category, sum(amount) over(partition by category) as total
                        from expenses
                        where expense_date between %s and %s; """,(start_date,end_date))   
        data=cursor.fetchall()
        return data

def fetch_expense_summary_by_month():
    logger.info(f"Fetching expense summary by month")
    with get_db_cursor() as cursor:
        cursor.execute("""
                        select month, sum(amount) as total_expenditure from
                        (select date_format(expense_date,"%b") as month, amount, category
                        from expenses)as x
                        group by month;
                       """)
        data = cursor.fetchall()
        return data



if __name__=="__main__":

    # expenses=fetch_expense_for_date("2024-09-30")
    # print(expenses)

    #insert_expense("2024-08-25",40,"Food","Samosa Chat")

    #delete_expense_for_date("2024-08-25")

    # summary=fetch_expense_summary("2024-08-01","2024-08-05")
    # for record in summary:
    #     print(record)

    month_summary=fetch_expense_summary_by_month()
    print(month_summary)
