#!/usr/bin/python3
import redis
import sys

POOL = redis.ConnectionPool(host='172.18.0.1', port=6379, db=3, password="haslo")

def getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set_response_callback('GET', int)
    response = my_server.get(variable_name)
    return response

def setVariable(variable_name, variable_value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.hset(variable_name, variable_value)
    
def insert(start_response): 
    try:
        rental_id=int(getVariable("last_rental_id"))+1
        payment_id=int(getVariable("last_payment_id"))+1

        r = redis.Redis(connection_pool=POOL)
        p = r.pipeline()
        p.incr("last_rental_id")
        p.incr("last_payment_id")

        p.hset("rental:"+str(rental_id), 'rental_id', rental_id)
        p.hset("rental:"+str(rental_id), 'inventory_id', '1')
        p.hset("rental:"+str(rental_id), 'customer_id', '1')
        p.hset("rental:"+str(rental_id), 'staff_id', '1')

        p.hset("payment:"+str(payment_id), 'rental_id', payment_id)
        p.hset("payment:"+str(payment_id), 'inventory_id', '1')
        p.hset("payment:"+str(payment_id), 'customer_id', '1')
        p.hset("payment:"+str(payment_id), 'staff_id', '1')
        p.hset("payment:"+str(payment_id), 'amount', 5.0)

        p.execute()
        start_response("200 OK", [("Content-Type", "text/plain"),("Content-Encoding", "utf-8")])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        start_response('500 INTERNAL SERVER ERROR', [("Content-Type", "text/plain"),("Content-Encoding", "utf-8")])


