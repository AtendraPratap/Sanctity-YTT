# moneyply CMS Base


## Setup and installation

- [ ] Clone the repository <br/>
      `git clone https://github.com/ishantd/moneyply.git`

- [ ] Install required libraries and dependencies <br/>
        `sudo apt-get update -y && sudo apt-get install python3-pip python3-dev libpq-dev python3-venv nginx -y`


- [ ] Create Virtual Env <br/>
      `cd moneyply && python3 -m venv env`

- [ ] Activate Virtual Env <br/>
      `source env/bin/activate`

- [ ] Install dependencies <br/>
      `pip3 install wheel && pip3 install -r requirements.txt`


send db: 

sudo scp -i /home/ishant/brand.pem /home/ishant/ishant_linux/moneyply/moneyply/db.sqlite3 ubuntu@52.172.35.186:/home/ubuntu/moneyply

sudo scp -i /home/ishant/brand.pem /home/ishant/ishant_linux/moneyply/moneyply/media.zip ubuntu@52.172.35.186:/home/ubuntu/moneyply

sudo scp -i /home/ishant/brand.pem ubuntu@52.172.35.186:/home/ubuntu/moneyply/db.sqlite3 /home/ishant/ishant_linux/moneyply/moneyply


Setup gunicorn :

sudo nano /etc/systemd/system/gunicorn.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/moneyply
ExecStart=/home/ubuntu/moneyply/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/moneyply.sock moneyply.wsgi:application

[Install]
WantedBy=multi-user.target

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nginx Setup:

sudo nano /etc/nginx/sites-available/moneyply


server {
    listen 80;
    server_name 13.234.238.237;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/moneyply;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/moneyply.sock;
    }

    location /media/ {
        alias /home/ubuntu/moneyply/media/;
    }
}

sudo ln -s /etc/nginx/sites-available/moneyply /etc/nginx/sites-enabled



#### To restart server
sudo pkill gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl restart nginx
sudo systemctl restart gunicorn.service


sudo systemctl restart gunicorn.service
sudo systemctl restart nginx

sudo python3 manage.py collectstatic --no-input

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

CMS PANEL : 



Products - Lexotique , kitchenji, etc - list of products - product x ( with the related fields , buy link )
Blogs  - Lexotique , kitchenji, etc - list of blogs - blogs x ( with the related fields )
settings - Users - Name , Site ownership , username and email/pass ( create general admin , create executive ) 
                          - Lexotique
                          - kitchenji
                          - Madhuram  



Settings - Site owners will have  multiple selection of 


Presentations:

Fresheys:
Web = https://docs.google.com/presentation/d/1lP4BtFX4kIW2gxr7FwuXHpxCKIaDnVkuIizkh-RHpc8/edit#slide=id.g966a22fd74_0_0
Mobile = https://docs.google.com/presentation/d/1jtG1jdyI6lg916VUsZMgMWnFDCgJquBZH0xYZiREY4I/edit


Lexotique:
Web = https://docs.google.com/presentation/d/1FRT00VIZJ7xr8YCDvPrVDcoSHlG9zcKeCezC2vNHHwk/edit?usp=sharing
Mobile = https://docs.google.com/presentation/d/1c0EECcwOZbK2mWitnevRsZa0wpzm1n0RJYg1Omr34cw/edit?usp=sharing


Cron command for emails

2 * * * * /home/ubuntu/moneyply/env/bin/python /home/ubuntu/moneyply/manage.py send_queued_mail >> send_mail.log 2>&1

db-user : postgres
db-pwd  : S$_YE47aubG4GVf;

AKIA3DPC3CNKGMXOQDFB
56vwJLZ24EjnemDeu7boKqG4Ou3iurbIp2T8smrk


Why MoneyPly:

Hassle free, 100 digital, flexible, less documents

Transparent Pricing


3 testimonials 


Jan 5, Changes


Email Credentials
SMS Provider
DSA Login Function
Banner Image Finalize
Leadership team, images and content
About Us Image
Privacy Policy and TNC Review
Moneyply Social Accounts


changes 9 Jan

