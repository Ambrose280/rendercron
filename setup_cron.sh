FROM alpine:3.14

# Install curl and cron
RUN apk add --no-cache curl crond

# Copy the script to the container
COPY visit_url.sh /visit_url.sh

# Make sure the script is executable
RUN chmod +x /visit_url.sh

# Set up the Crontab
RUN echo "*/4 * * * * /visit_url.sh" > /etc/crontabs/root

# Start the cron daemon in the foreground
CMD ["crond", "-f"]
