#!/usr/bin/env bash
set -euo pipefail

cd /home/ec2-user/aws-python-api-devops

echo "Building the API image..."
sudo docker build -t python-api:local .

echo "Replacing the API container..."
if sudo docker container inspect python-api >/dev/null 2>&1; then
    sudo docker rm -f python-api
fi

echo "Starting the API container..."
sudo docker run -d \
    --name python-api \
    --restart unless-stopped \
    -p 127.0.0.1:8000:8000 \
    python-api:local

echo "Checking the health endpoint..."
status=$(curl -sS --retry 10 --retry-all-errors --retry-delay 1 --max-time 5 -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/health)
echo "Health endpoint returned HTTP $status"
test "$status" = "200"

echo "Deployment completed successfully."
