# virtualenv使用
## 用于为项目创建虚拟环境，一般用于python项目，方便迁移与项目版本管理。
---

## 安装
> pip install virtualenv

## 创建环境
> virtualenv env

* ### 可加参数
* ### 增加系统库
> virtualenv --system-site-packages env

* ### 自己提供路径
> virtualenv ----extra-search-dir=/path/path env

## 载入环境
> source ./env/bin/activate

## 载出环境
> deactivate