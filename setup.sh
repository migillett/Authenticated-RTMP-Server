#!/bin/bash

# Run this once to get everything setup
# you must run this script as sudo or root
# Tested with Ubuntu 21.04

apt update

# definitely needed
apt install nginx libnginx-mod-rtmp -y
# needs testing to see if truly needed
apt install build-essential libpcre3 libpcre3-dev libssl-dev -y

# create directory to convert RTMP to HLS
mkdir -p /tmp/hls
chown -R www-data:www-data /tmp/hls

# create directory for HTML website
mkdir -p /var/www/html
cp ./index.html /var/www/html
chown -R www-data:www-data /var/www/html

cp ./nginx.conf /etc/nginx
service nginx restart
