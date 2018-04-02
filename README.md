# docker-dvwa
Using Damn Vulnerable Web Application in docker

## DVWA github
https://github.com/ethicalhack3r/DVWA

## Installation
```bash
mkdir -p log/apache2
sudo docker run --name dvwa -itd -p 80:80 -p 3306:3306 -e MYSQL_PASS="mypass" -v ~/log/apahce2:/var/log/apache2 vulnerables/web-dvwa
```
Default username = `admin`
Default password = `password`

## Log
```bash
sudo docker cp dvwa:/var/log/apache2/access.log log
```

## Tool commands
```bash
docker cp CONTAINER_ID:PATH LOCAL_PATH
```
