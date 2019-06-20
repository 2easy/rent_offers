#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import redis
import time

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def notification_loop():
    rc = redis.Redis(host='redis')
    p = rc.pubsub(ignore_subscribe_messages=True)
    p.subscribe('rent_offers')

    while True:
        message = p.get_message()
        if message:
            logging.info(json.loads(message['data']))

        time.sleep(.1)


if __name__ == "__main__":
    notification_loop()
