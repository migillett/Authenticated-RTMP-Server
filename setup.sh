#!/bin/bash

# Run this once to get everything setup
# you must run this script as sudo or root
# Tested with Ubuntu 21.04 and Debian 10

apt update
apt install nginx libnginx-mod-rtmp build-essential libpcre3 libpcre3-dev libssl-dev -y
echo "RTMP SERVER SETUP.SH: dependencies installed"

# create directory to convert RTMP to HLS
mkdir -p /tmp/hls
chown -R www-data:www-data /tmp/hls
echo "RTMP SERVER SETUP.SH: created directory at /tmp/hls"

# create directory for HTML website
mkdir -p /var/www/html
echo "RTMP SERVER SETUP.SH: created /var/www/html"

# if it already exists, clear all contents
rm /var/www/html/*
cp ./nginx/index.html /var/www/html
echo "RTMP SERVER SETUP.SH: copied index.html to /var/www/html"

wget https://raw.githubusercontent.com/arut/nginx-rtmp-module/master/stat.xsl | /var/www/html/stat.xsl
echo "RTMP SERVER SETUP.SH: downloaded stat.xsl to /var/www/html/stat.xsl"

chown -R www-data:www-data /var/www/*
echo "RTMP SERVER SETUP.SH: changed permissions to user www-data in folder /var/www"

# firewall setup (uncomment if you want to use it)
#apt install ufw
#ufw default drop incoming
#ufw default allow outgoing
#ufw allow 1935
#ufw allow ssh
#ufw allow http
#ufw enable
#echo "RTMP SERVER SETUP.SH: firewall updated and enabled"

cp ./nginx/nginx.conf /etc/nginx
echo "RTMP SERVER SETUP.SH: nginx configuration copied to /etc/nginx"
service nginx restart
echo "RTMP SERVER SETUP.SH: nginx restarted"

echo "RTMP SERVER SETUP.SH: Script done!"
