#!/usr/bin/env python3

import pymysql.cursors
import random
def transaction():
    File = open("/tmp/test","a+")
    connection = pymysql.connect(host='172.18.0.1',
                                 user='root',
                                 password='123',
                                 db='sakila')

    try:
        with connection.cursor() as cursor:
            inventory_id = random.randint(1,4500)
            customer_id = random.randint(1,599)
            rental = "INSERT INTO rental(inventory_id,customer_id,staff_id)  VALUES ({},{},{})".format(inventory_id,customer_id,2)
          #  payment ="INSERT INTO payment(customer_id, staff_id, rental_id, amount) VALUES(1, 1, LAST_INSERT_ID(), 4)"
            cursor.execute(rental)
           # cursor.execute(payment)
            connection.commit()
            cursor.close()
    finally:
        connection.close()
        
    File.close()
    return  "Dupa Closed"
