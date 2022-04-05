# MIS
## 简介
```plain
(1) 前端基于框架React，对应目录./front-end
(2) 后端基于框架Flask，对应目录./back-end
```
## 使用方法
### 前端
- npm(8.0+)/react(18.0)
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
### 后端
- python(3.7+)/MySQL(5.6+)
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
gunicorn -w 2 -b 127.0.0.1 5000 mis_backend.main:app
```

- 使用咨询和建议可联系
```plian
email: wuyangwebdeveloper@163.com
```

## demo地址
http://124.221.225.43
```plain
user: admin
password: 1234
```
## 页面概览
- /home
![Image text](https://github.com/wuyangdevops/mis-your-index/blob/main/images/home.png)
```plain
1. 展示统计信息
```

- /category
![Image text](https://github.com/wuyangdevops/mis-your-index/blob/main/images/category.png)
```plain
1. 展示品类信息（二级品类结构）
2. 新增、编辑品类信息
```

- /product
![Image text](https://github.com/wuyangdevops/mis-your-index/blob/main/images/product.png)
```plain
1. 展示商品信息
2. 新增、编辑商品信息（包括上下架）
3. 按照名称、描述搜索商品
```

- /user
![Image text](https://github.com/wuyangdevops/mis-your-index/blob/main/images/user.png)
```plain
1. 展示用户信息
2. 新增、编辑用户
```

- /role
![Image text](https://github.com/wuyangdevops/mis-your-index/blob/main/images/role.png)
```plain
1. 展示角色信息
2. 编辑角色权限
```