#!/usr/bin/python3
import pymysql.cursors
import random

def insert(start_response):   
    connection = pymysql.connect(host='172.18.0.1',
                             user='root',
                             password='123',
                             db='sakila')
    try:
        with connection.cursor() as cursor:
            inventory_id = random.randint(1,4500)
            customer_id = random.randint(1,599)
            rental = "INSERT INTO rental(inventory_id,customer_id,staff_id)  VALUES ({},{},{})".format(inventory_id,customer_id,2)
            payment ="INSERT INTO payment(customer_id, staff_id, rental_id, amount) VALUES ({},{},{},{})".format(customer_id,2,"LAST_INSERT_ID()",5)
            cursor.execute(rental)
            cursor.execute(payment)
            connection.commit()
            cursor.close()
            start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Encoding", "utf-8")])
    except:
             start_response("500", [("Content-Type", "text/plain"),
                              ("Content-Encoding", "utf-8")])
    finally:
        connection.close()
