# linux防火墙（selinux,firewalld,iptables）

## selinux
* #### 安全增强型 Linux（Security-Enhanced Linux）  
#### Linux 内核模块，也是 Linux 的一个安全子系统

### selinux三种模式，在/etc/selinux/config设置
* #### enforcing 强制模式
#### permissive 宽容模式
#### disabled 关闭

### 获取模式 | 临时设置模式 | 查看selinux状态
> getenforce  
> setenforce 1|0  
> /usr/sbin/sestatus 

## firewalld(了解一般操作，一般就把他关掉)

> 启动：systemctl start firewalld.service  
关闭：systemctl stop firewalld.service   
重启：systemctl restart firewalld.service   
显示状态：systemctl status firewalld.service  
开机时启用：systemctl enable firewalld.service   
开机时禁用：systemctl disable firewalld.service  


## iptables 

### 查看iptables(--line-number 显示对应行数用于删除)
> iptables -n -L

> Iptables \  
操作：-A增/-I插/-R换/-D删 \    
链名：INPUT输入/OUTPUT输出/PORWARD转发 \  
对象：-p tcp --dport IP \  //  -s/d IP\/24(-s表示源，-d表示目标，24相当于255.255.255.0)  
动作：-j ACCEPT接收/DROP拒绝/REDIRECT重定向   