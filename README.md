# Clound-based Multi-vehicle Control System
A cloud-based multi-vehicle autonomous car control system

## Setup Step

Test the web client <-> uWSGI <-> Python

```bash
uwsgi --http :8000 --wsgi-file test.py
```

Test the web client <-> uWSGI <-> Django

```bash
uwsgi --http :8000 --module website.wsgi
```

Test the web client <-> the web server

```bash
sudo service nginx start
```
or

```
brew services start nginx
```

Link `website_nginx.conf` file

```bash
sudo ln -s /home/pichao/Source/CMCS/website/website_nginx.conf /etc/nginx/sites-enabled/
```
or

```bash
mkdir -p /usr/local/etc/nginx/sites-{enabled,available}
ln -s /Users/pichao/Source/CMCS/website/website_nginx.conf /usr/local/etc/nginx/sites-available/
```
Add following into /usr/local/etc/nginx/nginx.conf
```
include /etc/nginx/conf.d/*.conf;
include /usr/local/etc/nginx/sites-enabled/*.conf;
```

Collect nginx statics

```bash
python manage.py collectstatic
```

Restart nginx and test static at localhost:8000

Test with py file for the web client <-> the web server <-> the socket <-> uWSGI <-> Python

```bash
uwsgi --socket :8001 --wsgi-file test.py
```

Test with unix socket

```bash
uwsgi --socket website.sock --wsgi-file test.py
```

Test with project

```bash
uwsgi --socket website.sock --module website.wsgi --chmod-socket=666
```

Test with uwsgi init file

```bash
uwsgi --ini website_uwsgi.ini
````
