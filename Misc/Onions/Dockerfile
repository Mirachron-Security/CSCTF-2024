ROM nginx:latest

COPY app /usr/share/nginx/html

RUN apt-get update && \
    apt-get install -y tor && \
    rm -rf /var/lib/apt/lists/* && \
    # Configure Tor
    echo "HiddenServiceDir /var/lib/tor/hidden_service/" >> /etc/tor/torrc && \
    echo "HiddenServicePort 80 127.0.0.1:80" >> /etc/tor/torrc && \
    # Adjust permissions 
    chown -R debian-tor:debian-tor /var/lib/tor /etc/tor/torrc && \
    chmod 700 /var/lib/tor && \
    chmod 600 /etc/tor/torrc

# Nginx
EXPOSE 80

# Start both Tor and nginx
COPY start/start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]

# Wait at least 30 seconds for the web server to go live
# docker exec -it misc-onions-container cat /var/lib/tor/hidden_service/hostname
# kubectl exec -it pod/misc-onions-9c9d7d849-cjngm -n haproxy -- cat /var/lib/tor/hidden_service/hostname