# WEB Container
This container will be running NGINX.  

Base image is Alpine Linux to make it extremely lean.

I also had to compile confd specifically for alpine linux.
This is why I've included the binary inside this directory.

For how to create/update confd binary, follow instructions here:
https://github.com/kelseyhightower/confd/blob/master/docs/installation.md
