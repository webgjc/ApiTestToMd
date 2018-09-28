# docker从入门到放弃

## 查看镜像，查看容器

> docker images -a  
> docker ps -a

## 进入容器命令行

> docker exec -it container_name bash

> docker run -it images bash
 
## 查看改动

> docker diff

## 保存容器为新的镜像

> docker commit container_name repository:tag

## 运行镜像

> docker run --name xxx -d -p 80:80 repository:tag

## 构建镜像

> docker build ./ -t repository:tag

## 搜索公共镜像

> docker search search_name

## 删除镜像

> docker rmi \`docker images -a |grep ago |awk '{print $3}'\`

## 删除容器

> docker rm \`docker ps -a |grep ago |awk '{print $1}'\`

## 网络

> docker network ls

# docker-compose

## 构建/重启/停止/开启 docker

> docker-compose build/restart/stop/up [service_name]


