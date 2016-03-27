#!/bin/sh

#CONSUL='192.168.99.100:8500'
# Fail hard and fast
set -eo pipefail


# Remove old config, so nginx config is valid
rm -f /etc/nginx/default.d/default

# Try to make initial configuration every 5 seconds until successful
until confd -backend etcd -onetime -node http://etcd:2379 -config-file /etc/confd/conf.d/nginx.toml; do
    echo "[nginx] waiting for confd to create initial nginx configuration."
    sleep 5
done

#primes=(11 13 17 19 23 29 31 37 41 43)
cat /etc/nginx/default.d/default

# Start confd (3 second refresh, not for production)
confd -interval 11 -backend etcd -node http://etcd:2379 -config-file /etc/confd/conf.d/nginx.toml &
echo "[nginx] confd is now monitoring etcd for changes in intervals of 11 seconds..."

chown nginx /var/run/nginx
echo "[nginx] Starting NGINX.."
/usr/sbin/nginx
