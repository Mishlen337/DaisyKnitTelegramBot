To start the project:
1. Configure https proxy:
sudo apt update
sudo apt install nginx
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw enable
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
sudo systemctl status certbot.timer
sudo vim /etc/nginx/sites-enabled/example.com

2. fill .env file
3. docker compose up --build
