## 脚本A：tag.py

### Input 
1.	真实access.log文件


### Output
1.	normal.log 包含未被标记为攻击的所有log
2.	falsealarm.log 包含已知为错报的所有log
3.	xss.log 包含其他被标记为xss攻击的log
4.	sqli.log …
5.	…
6.	…


## 脚本B：attack_generate.py

### Input
1.	log模板文件（normal.log）
2.	攻击模板文件（sqliinput.txt）

### Parameter
1.	攻击种类选项：sqli/lfi/xss
对于不同攻击种类有不同替换组合方式，如sqli需要找?xxx=，而lfi不需要
2.	攻击条数：num
Num默认为攻击模板数
Num小于攻击模板数时，不重复随机采样攻击模板，随机采样log模板
Num大于攻击模板数时，超出的部分随机采样攻击模板，随机采样log模板

### Output
1.	攻击log
