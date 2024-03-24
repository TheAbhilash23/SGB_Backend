#!/usr/bin bash

#sudo dockerd

docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml rm --force
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d --remove-orphans

