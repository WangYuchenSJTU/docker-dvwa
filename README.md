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
- Then, you should be able to access the server log (mainly the `access.log`) in your host OS's `~/log/apache2`.

Default username = `admin`

Default password = `password`

- Possible problem: if mysql server fail to start, make sure using aufs as docker storage driver

https://github.com/ethicalhack3r/DVWA/issues/175



## Tool Commands
* remove all stopped containers

`docker rm $(docker ps -a -q)`
* stop all containers

`docker kill $(docker ps -q)`
* remove all containers

`docker rm $(docker ps -a -q)`
* remove all exited containers

`docker rm $(docker ps -qa --no-trunc --filter "status=exited")`
* remove all docker images

`docker rmi $(docker images -q)`
* delete all unused images

`docker rmi $(docker images --filter "dangling=true" -q --no-trunc)`
* remove all untagged images

`docker rmi $(docker images | grep "^<none>" | awk "{print $3}")`
* copy files from containers

`docker cp CONTAINER_ID:PATH LOCAL_PATH`

## To Do
Apache(DVWA) + ELK in k8s
