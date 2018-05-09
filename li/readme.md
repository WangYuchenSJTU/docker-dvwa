# xsser使用指南

## 安装方法
 在 http://www.bubuko.com/infodetail-516700.html 下载ubuntu版，
 打开安装
 在终端输入xsser确认是否安装成功
 如需查看源码，可下载源码版本

## 攻击方法
指令可以参考  https://blog.csdn.net/emaste_r/article/details/8072323
下面罗列一些经测试可以使用的指令
### 基本格式
 以dvwa为例，需要提供待攻击网站的url和cookie      
 
 python xsser.py -u "http://127.0.0.1/vulnerabilities/xss_r/?name=" --cookie="security=low; PHPSESSID=irlo67ci48k9eh3qluc57gjr80"
 url提示了攻击插入点
 
 ### 可添加的指令
 #### 输出结果相关
       -s -v  显示更多输出信息
 #### 自动化攻击
    -auto用于自动攻击
 #### 校验器
    用来测试网站有没有过滤攻击的手段  
        --heuristic  测试哪些字符没有被屏蔽  
 #### 选择bypasser
    --Hex 使用16进制编码
     强大的攻击方式，对于dvwa初级中级攻击尝试全部成功
     对于高级仍然有80%以上命中率
 #### 特殊技巧
     --Xsa 跨站Agent 脚本
 ## 示例 
    python xsser.py -u "http://127.0.0.1/vulnerabilities/xss_r/?name=" --cookie="security=low; PHPSESSID=a1lhrbjm0ifv8ju6qknfd685j6" --auto -  s -v --reverse-check --Hex   
自动攻击，显示详细信息，以16进制编码  
强大的攻击方式，初级中级全部攻破

更详细的英文版本访问 http://www.bubuko.com/infodetail-516700.html
