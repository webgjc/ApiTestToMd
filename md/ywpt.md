# 运维平台api(装机历史部分)

## 接口名称:获取装机历史

### 1) 请求地址

>/history

### 2) 调用方式：HTTP GET

### 3) 接口描述：管理员获取全部装机历史，用户获取用户自身装机历史

### 4) 请求参数:

| 字段名称 | 字段说明 | 类型 | 必填 | 备注 |
| ------|:------:|:-------:|:------:| ------:|
|token|用户身份编号|string|Y|-|

### 5) 请求返回结果:
```
{
    "msg": [
        {
            "id":"qwertyuiooop",
            "product_name":"哨兵云",
            "product_version":"v1.5.0",
            "name":"张三"，
            "machine_func_type":"一体机",
            "customer":"李四",
            "install_time":"2018-08-08 12:12:12",
            "install_state":2，
            "log_path":"/home/xxx.log"
        }
    ],
    "sts": 1
}
```

### 6) 请求返回结果参数说明:
| 字段名称 | 字段说明 | 类型 | 备注 |
| ------|:------:|:------:| ------:|
|msg|msg|array|id用于查看细节接口|
|sts|sts|int|1-成功，0-失败|



## 接口名称:上传装机历史

### 1) 请求地址

>/history

### 2) 调用方式：HTTP POST

### 3) 接口描述：-

### 4) 请求参数:

| 字段名称 | 字段说明 | 类型 | 必填 | 备注 |
| ------|:------:|:-------:|:------:| ------:|
|token|用户身份编号|string|Y|-|
|product_detail_id|安装产品编号|string|Y|-|

### 5) 请求返回结果:
```
{
    "msg": "",
    "sts": 1
}
```

### 6) 请求返回结果参数说明:
| 字段名称 | 字段说明 | 类型 | 备注 |
| ------|:------:|:------:| ------:|
|msg|msg|string|失败返回失败原因，成功返回空|
|sts|sts|int|1-成功，0-失败|


## 接口名称:查看装机结果

### 1) 请求地址

>/history/result

### 2) 调用方式：HTTP GET

### 3) 接口描述：-

### 4) 请求参数:

| 字段名称 | 字段说明 | 类型 | 必填 | 备注 |
| ------|:------:|:-------:|:------:| ------:|
|token|用户身份编号|string|Y|-|
|id|装机历史的id|string|Y|-|

### 5) 请求返回结果:
```
{
    "msg": {
        "product_name":"哨兵云",
        "product_version":"v1.5.0",
        "name":"张三"，
        "machine_func_type":"一体机",
        "customer":"李四",
        "machine_physical_type":"物理机",
        "ssh_port":"80"
        "ssh_account":"root"
        "ssh_password":"password",
        "ip":"192.168.199.1"
        "public_ip":"1.1.1.1"
        "web_port":"80"
        "web_accout":"admin"
        "web_password":"admin"
        "cpu_number":"5"
        "memory":"4G"
        "disk":"500G"
        "raid":"asd"
        "sda":"qwert"
        "net_cards":"eht0"
    },
    "sts": 1
}
```

### 6) 请求返回结果参数说明:
| 字段名称 | 字段说明 | 类型 | 备注 |
| ------|:------:|:------:| ------:|
|msg|msg|object|-|
|sts|sts|int|1-成功，0-失败|

