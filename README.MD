## 项目简介
```
Pool-X 测试工具平台
前端：Vue2 + iview
后端：Flask + sqlalchemy

```
#### 功能简介：
|  模块   | 功能  | 完成情况
|  ----  | :----  | :----  |
| 测试账号  | 快速生成账号 |DONE|
|   测试账号| 测试账号列表 |DONE|
| 测试账号  | 充值 |DONE|
|   测试账号| 批量导出测试账号 |TODO|
| 数据检测  | 持仓收益检测 |DONE|
|   数据检测| 锁仓收益检测 |DONE|
| 数据检测  | 投票收益检测 |DONE|
| 数据检测  | 大币锁仓 |TODO|
| 数据检测  | LOCKDROP收益检测 |TODO|
| 数据检测  | 收益发放检测 |TODO|
|   接口测试| 定义接口mock数据 |DONE|
|   接口测试| mock server的重启 |DONE|
|   接口测试| moco使用文档 |DONE|
|   接口测试| Pool-X接口自动化的调度 |TODO|

## 安装
#### flask应用 安装
```
安装：pip install -r requirements.txt
启动：python3 manage.py

```
####前端工程安装
```
见client目录下README
```


## 目录简介
> client 前端工程

>> src

>>> components 组件

>>> request api的定义与http请求的封装

>>> router 前端路由

> kctool 后端工程代码

>> commonMethods 一些公用方法

>> modles 自定义的数据模型

>> *views.py 视图

> moco mock平台

>> moco_file 存储moco文件

>> moco-runner*.jar moco服务的启动包

>> views.py moco文件管理view层

> models 逆向工程自动生成的models层

> template flask应用中定义的一些前端模版

> app.py 定义一个flask app

