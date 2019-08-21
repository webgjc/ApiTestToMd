# hive-docker
> https://hub.docker.com/r/bde2020/hive

> mysql5.6/5.7

> 主机上：docker network  
create新的网桥，connect两个continer至这个网桥上


```

apt-get update

apt-get install -y openssh-client openssh-server vim

mkdir /var/run/sshd
chmod 755 /var/run/sshd/
配置免密
ssh-keygen -t rsa -P ""
cat /root/.ssh/id_rsa.pub > ~/.ssh/authorized_keys

修改/etc/hadoop/hadoop_env.sh中
export JAVA_HOME=绝对路径

cp hive-default.xml.template hive-site.xml

vim hive-site.xml
改 ConnectionURL 为 jdbc:mysql://host:3306/database
改 ConnectionUserName 为 用户名
改 ConnectionPassWord 为 密码

改user.name为目录

改tmpdir为有权限的目录

mysql 创建数据库和用户，分配权限。
复制mysql-connnectxxx.jar到/opt/hive/lib/

schematool -dbType mysql -initSchema

hadoop namenode -format
至hadoop目录下
start-all.sh

vim /usr/local/bin/startup.sh
增加 /usr/sbin/sshd
cd /opt/hadoop.xx/sbin
./start-all.sh 
到hiveserver2之前 
开机启动


```