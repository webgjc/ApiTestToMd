# 虚拟机管理

## 下载所需库环境
> yum -y install qemu-kvm qemu-key-tools virt-manager libvirt virt-install python-virtinst bridge-utils  
> yum -y install kvm qemu libvirt virt-viewer qemu-system  
> yum -y install libguestfs-tools

## 创建虚拟img镜像
> qemu-img create -f qcow2 /home/vm/name.img 100G

## 配置虚拟机
参数分别为：虚拟机名称，cpu，内存，iso镜像路径，img镜像路径，vnc端口  
>virt-install \  
--name name \  
--vcpus=2 \  
--ram 2048 \  
--cdrom=/home/CentOS-7-x86_64-DVD-1511.iso –disk \  
path=/home/qianhangjian/CentOS7_DVD1511.img \  
--graphics vnc,listen=0.0.0.0,port=5910

## 然后打开tightvnc 连接对应的ip和端口，进行centos图形化安装。
### 安装参考centos安装pdf文件

## 中间需配置的文件：

> 网卡文件  
/etc/sysconfig/network-scripts/ifcfg-eth0  
虚拟机配置文件  
/etc/libvirt/qemu/xxx.xml

## 虚拟机和实体机之间的网络用桥连
### 具体配置大致为,以下做参考
> TYPE="Ethernet"  
DEFROUTE="yes"  
IPV4_FAILURE_FATAL="no"  
IPV6INIT="no"  
NAME="eno1"  
DEVICE="eno1"  
ONBOOT="yes"  
BRIDGE="br0"  

>TYPE="Bridge"  
BOOTPROTO="static"  
NAME="br0"  
DEVICE="br0"  
ONBOOT="yes"  
IPADDR="192.168.6.10"  
NETMASK="255.255.255.0"  
GATEWAY="192.168.6.1"  
DNS1="192.168.6.1"  

## 日常维护命令

### 列出运行中虚拟机 (--all 为列出所有)
> virsh list

### 开启，关闭虚拟机
> virsh start name  
virsh shutdown name/num  
virsh destroy name/num

### 删除虚拟机 (删除前需先关闭)
> virsh undefine name

### 创建虚拟机快照
> virsh snapshot-create-as name snapid  
virsh snapshot-create name

### 列出虚拟机快照
> virsh snapshot-list name/num

### 回退虚拟机到快照 (--force 强制回退)
> virsh snapshot-revert name/num snapid

* ### 回退之后要校准时间
> ntpdate -u ntp.sjtu.edu.cn  
hwclock -w

### 删除虚拟机快照
> virsh snapshot-delete name/num snapid

### 克隆虚拟机
> virt-clone -o 克隆虚拟机名称 -n 目标虚拟机名称 -f 路径/name.img

### 克隆虚拟机全自动脚本
>name=clone1  
port=5901  
ip=192.168.199.63  
dir=/home/vm/  
virsh destroy base  
rm -rf $dir$name.img  
virt-clone -o base -n $name -f $dir$name.img  
virt-copy-out -d $name /etc/sysconfig/network-scripts/ifcfg-eth0 ./  
sed -i "s/IPADDR=.*/IPADDR=\"$ip\"/" ifcfg-eth0  
virt-copy-in -d $name ./ifcfg-eth0 /etc/sysconfig/network-scripts/  
rm -rf ./ifcfg-eht0  
sed -i "s/<graphics.*/<graphics type='vnc' port='$port' autoport='no'   
listen='0.0.0.0'>/" /etc/libvirt/qemu/$name.xml  
virsh define /etc/libvirt/qemu/$name.xml  
virsh start $name  
virsh start base  
