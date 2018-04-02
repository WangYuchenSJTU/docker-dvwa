# docker-dvwa
Using Damn Vulnerable Web Application in docker

## DVWA github
https://github.com/ethicalhack3r/DVWA

## Installation
```bash
sudo docker run --name dvwa -itd -p 80:80 -p 3306:3306 -e MYSQL_PASS="mypass" vulnerables/web-dvwa
```
Default username = `admin`
Default password = `password`

## Log
```bash
sudo docker cp dvwa:/var/log/apache2/access.log log
```
