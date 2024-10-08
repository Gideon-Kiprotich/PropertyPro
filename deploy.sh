#!/bin/bash

# Navigate to the project directory
cd /var/www/html/PropertyPro

# Stash any local changes (optional)
git stash

# Pull the latest changes from the GitHub repository
git pull origin main

# (Optional) Restart the web service if needed (e.g., Apache or Nginx)
sudo systemctl restart apache2

# Provide execution permissions to the script
chmod +x /var/www/html/PropertyPro/deploy.sh
