# Use an official Chrome image as the base image
FROM zenika/alpine-chrome:with-node

# Set the working directory in the container
WORKDIR /app

# Copy the extension files into the container
COPY manifest.json .
COPY background.js .
COPY popup.html .
COPY popup.js .
COPY popup.css .

# Expose port 9222 for remote debugging
EXPOSE 9222

# Define the command to run your extension
CMD ["chrome", "--headless", "--disable-gpu", "--remote-debugging-port=9222", "--no-sandbox", "--disable-dev-shm-usage", "--user-data-dir=/tmp", "--load-extension=/app"]
