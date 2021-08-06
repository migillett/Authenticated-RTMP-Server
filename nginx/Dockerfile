FROM tiangolo/nginx-rtmp

COPY --chown=www-data:www-data ./stat.xsl /usr/local/nginx/html/stat.xsl

COPY ./nginx.conf /etc/nginx/nginx.conf