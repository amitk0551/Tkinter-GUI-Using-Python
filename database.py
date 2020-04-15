import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="project"
)
mycursor = mydb.cursor()

def insert_data(prod_id, prod_name, qty_on_hand, prod_unit_price, reoder):
    sql = "INSERT INTO tbl_stock(prod_id, prod_name, qty_on_hand, prod_unit_price, reoder) VALUES (%s, %s, %s, %s, %s)"
    val = (prod_id, prod_name, qty_on_hand, prod_unit_price, reoder)
    mycursor.execute(sql, val)
    mydb.commit()
    return 1


def show_data():
    mycursor.execute("SELECT * FROM tbl_stock")
    myresult = mycursor.fetchall()
    return myresult
 
def update_stock(prod_id, prod_name, qty_on_hand, prod_unit_price, reoder):
    sql = "UPDATE tbl_stock SET prod_name = %s, qty_on_hand = %s, prod_unit_price = %s, reoder = %s WHERE prod_id = prod_id"
    val = (prod_name, qty_on_hand, prod_unit_price, reoder)
    mycursor.execute(sql, val)
    mydb.commit()
    return 1


def show_data_id(id):
    sql = "SELECT * FROM tbl_stock WHERE prod_id = %s"
    val = (id, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def delete_stock(id):
    sql = "DELETE FROM tbl_stock WHERE prod_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    result = mydb.commit()
    if result:
        return "error"
    else:
        return 0

def insert_data_sale(sale_id, pro_id, qty_sold, sale_price_per_unit):
    # mycursor.execute("SELECT prod_id FROM tbl_stock WHERE prod_id = pro_id")
    # prod = mycursor.fetchone()
    # prod_id =  ''.join(prod)
    today = str(date.today())
    sql = "INSERT INTO tbl_sale(sale_id, sale_date, prod_id, qty_sold, sale_price_per_unit) VALUES (%s, %s, %s, %s, %s)"
    val = (sale_id, today, pro_id, qty_sold, sale_price_per_unit)
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return 1

def show_data_sale():
    mycursor.execute("SELECT * FROM tbl_sale")
    myresult = mycursor.fetchall()
    return myresult

def show_data_sale_id(id):
    sql = ("SELECT * FROM tbl_sale WHERE sale_id = %s")
    val = (id, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult

def delete_sale(id):
    sql = "DELETE FROM tbl_sale WHERE sale_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    result = mydb.commit()
    if result:
        return "error"
    else:
        return 0
    print(mycursor.rowcount, "record(s) deleted")

def update_sale(sale_id,prod_id,qty,per):
    sql = "UPDATE tbl_sale SET prod_id = %s, qty_sold = %s, sale_price_per_unit = %s WHERE sale_id = sale_id"
    val = (prod_id, qty, per)
    mycursor.execute(sql, val)
    mydb.commit()
    return 1


# insert_data_sale("s100", 33, 55)