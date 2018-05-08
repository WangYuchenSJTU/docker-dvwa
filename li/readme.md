# xsser使用指南

## 安装方法
 在 http://www.bubuko.com/infodetail-516700.html 下载ubuntu版，
 打开安装
 在终端输入xsser确认是否安装成功
 如需查看源码，可下载源码版本

## 攻击方法
### 基本格式
 以dvwa为例，需要提供待攻击网站的url和cookie
 xsser -u "http://127.0.0.1/vulnerabilities/xss_r/?name=" --cookie="security=low; PHPSESSID=irlo67ci48k9eh3qluc57gjr80"
 url提示了攻击插入点？
