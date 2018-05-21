#!/usr/bin/python3
#import inserter
import inserter_redis
def application(environ, start_response):

    #inserter.insert(start_response)
    inserter_redis.insert(start_response)
    for k, v in environ.items():
        yield f"{k:>20} => {v}".encode("utf-8")
        
        
        
        
        
"""
sudo docker-compose build --no-cache && sudo docker-compose stop && sudo docker-compose rm -f && sudo docker-compose up -d
"""
