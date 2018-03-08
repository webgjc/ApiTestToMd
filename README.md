
# 实现功能

### 1.接口测试 GET，POST，PUT，DELETE

### 2.生成接口文档 Markdown，html

### 3.识别参数（使用百度翻译api）

### 4.Markdown在线编辑，转换为html

### 5.载入Markdown，保存Markdown和html

# HOW TO RUN

## 1) git clone it

## 2) python app.py

### python must be 3.x

#  Available URL

## Default port 5000

> ## ip:port/apitest

> ## ip:port/md

# 注意事项

### 1.若要使用翻译功能，则需在apitest/main.py中，修改/translate接口中的appid和secretKey为登录百度开放平台获取，http://api.fanyi.baidu.com/api/trans/product/index
### 然后需在 通用翻译API_服务信息 设置 服务器地址