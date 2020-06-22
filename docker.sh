#!/bin/bash
#Assuming docker-ce is installed on the host
#Create a docker network for inter container communication
docker network create \
  --driver=bridge \
  --subnet=172.28.0.0/16 \
  --ip-range=172.28.5.0/24 \
  --gateway=172.28.5.254 \
  br0
#Run Kibana Container
docker run --name kibana --network br0 -d docker.elastic.co/kibana/kibana:7.8.0
#Run Nginx Container
docker run --name nginx --network br0 -d nginx --publish 8080:80
#Run Mysql container 
docker run --name mysql --network br0 -e MYSQL_ROOT_PASSWORD=@rc@! -d mysql
