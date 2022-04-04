# MIS
## 简介
```plain
(1) 前端基于框架React，对应目录./front-end
(2) 后端基于框架Flask，对应目录./back-end
```
## 使用方法
- 前端
```shell
cd ./front-end
# 安装依赖
npm install
# 调试模式
npm start
# 生产模式
# 1. 打包
npm run build
# 2. 配置Nginx服务器（参考nginx.conf）
```
- 后端
```shell
cd ./back-end
# 配置环境 (按数据库信息修改default.py中SQLALCHEMY_DATABASE_URI)
mv ./common/settings/default.py.bak ./common/settings/default.py
# 安装依赖
pip install -r requirement.txt
# 调试模式
export FLASK_APP=mis_backend.main
flask run
# 生产模式 (Linux)
gunicorn -w 2 -b 127.0.0.1 5000
```

- 使用咨询和建议可联系
```plian
email: wuyangwebdeveloper@163.com
```

## demo地址
```plain
http://124.221.225.43

user: admin
password: 1234
```