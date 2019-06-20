# Rents Bot

This is a simple scraper that notifies when new offers arrive. You can easily extend it to other sites than gratka.pl

## Usage

```
docker-compose build
# Change PRICE_MAX env in docker-compose.yml
docker-compose up
```

## Architecture

Two simple services, one that scrapes targets, the other that notifies - right now only to console.

