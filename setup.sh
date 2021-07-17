#!/bin/bash

# Run this once to get everything setup
# you must run this script as sudo or root
# Tested with Ubuntu 21.04

apt update
apt install nginx libnginx-mod-rtmp build-essential libpcre3 libpcre3-dev libssl-dev -y
echo "dependencies installed"

# create directory to convert RTMP to HLS
mkdir -p /tmp/hls
chown -R www-data:www-data /tmp/hls
echo "created directory at /tmp/hls"

# create directory for HTML website
mkdir -p /var/www/html
echo "created /var/www/html"

# if it already exists, clear all contents
rm /var/www/html/*
cp ./index.html /var/www/html
chown -R www-data:www-data /var/www/html
echo "copied index.html to /var/www/html"

wget https://raw.githubusercontent.com/arut/nginx-rtmp-module/master/stat.xsl | /var/www/html/stat.xsl
echo "downloaded stat.xsl to /var/www/html/stat.xsl"

# firewall setup
ufw allow 1935
ufw allow 80
ufw enable
echo "firewall updated and enabled"

cp ./nginx.conf /etc/nginx
echo "nginx configuration copied to /etc/nginx"
service nginx restart
echo "nginx restarted"

echo "Script done! Last step is to change the [stream_key] variable in /var/www/html/index.html and [supersecretpassword] in /etc/nginx/nginx.conf"
