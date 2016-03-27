FROM undeadops/alpine-base

MAINTAINER Mitch Anderson <mitch@metauser.net>

COPY confd-0.11.0/confd /usr/local/bin/confd

RUN apk -U add nginx curl vim
COPY nginx/nginx.toml /etc/confd/conf.d/nginx.toml
COPY nginx/nginx.conf.tmpl /etc/confd/templates/nginx-site.conf.tmpl
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/proxy_params /etc/nginx/proxy_params

COPY nginx/run.sh /bin/run.sh
RUN chmod a+x /bin/run.sh

EXPOSE 80
EXPOSE 443

CMD ["/bin/run.sh"]
