#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import json
import logging
import os
import redis
import time

from gratka import get_gratka_offers

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

@click.command()
@click.option('--scraping-interval', default=5, help="Scraping interval in minutes")
def scraping_loop(scraping_interval):
    rc = redis.Redis(host='redis')
    price_max = int(os.getenv('PRICE_MAX', '2500'))

    while True:
        nnew = 0
        logging.info("Scraping targets...")
        offers = get_gratka_offers(price_max)
        logging.debug(f"Found {len(offers)}")
        for o in offers:
            if not rc.get(o['link']):
                nnew += 1
                rc.publish('rent_offers', json.dumps(o))
                rc.set(o['link'], "seen")

        logging.info(f"Found {nnew} new offers")
        # Sleep for at least 5m, there is no point in scraping more often
        time.sleep(scraping_interval)


if __name__ == "__main__":
    scraping_loop()
