#! /bin/bash

# Run this once to get everything setup
# you must run this script as sudo or root
# Works with Ubuntu 21

apt update && apt upgrade -y

# definitely needed
apt install nginx libnginx-mod-rtmp -y
# needs testing?
apt install build-essential libpcre3 libpcre3-dev libssl-dev

# create directory to convert RTMP to HLS
mkdir /tmp/hls
chown -R www-data:www-data /tmp/hls

# create directory for HTML website
mkdir /var/www/html
cp ./index.html /var/www/html
chown -R www-data:www-data /var/www/html

cp ./nginx.conf /etc/nginx
service nginx restart
