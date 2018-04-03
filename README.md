# docker-dvwa
Using Damn Vulnerable Web Application in docker

## DVWA github
https://github.com/ethicalhack3r/DVWA

## Installation
- make a directory in your host OS and and use `-v` option to load it in the DVWA container:
```bash
cd ~
mkdir -p log/apache2
docker run --name dvwa -itd -p 80:80 -p 3306:3306 -e MYSQL_PASS="mypass" -v ~/log/apahce2:/var/log/apache2 vulnerables/web-dvwa
```
- Then, you should be able to access the server log in your host OS.

Default username = `admin`

Default password = `password`

## Tool commands
```bash
docker cp CONTAINER_ID:PATH LOCAL_PATH
```

## To do
Apache(DVWA) + ELK in k8s
