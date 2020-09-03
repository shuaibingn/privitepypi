## privatepypi

关于构建私有pypi仓库的Dockerfile

网上大部分是上传时需要密码，而下载时不需要密码，在项目开发中有时候反而都需要密码进行管理

该项目就是针对于这种情况，在上传和下载时都需要输入密码

## 使用
### 生成账号密码

- 按照提示输入账号密码
```shell script
# 安装依赖
$ pip install -r requirements.txt
# 生成密码
# 默认为admin admin
$ htpasswd -sc ./auth/.htpasswd <your usernmae>
```

### 编译

首先，确定你的电脑中安装有docker，然后运行以下脚本
```shell script
# 编译docker镜像
$ ./build_docker.sh

# 运行编译好的docker镜像
$ ./run_docker.sh
```

### 访问
默认将会开启本地端口`8080`，在浏览器中输入`http://localhost:8080`


## setup命令
`setup`是本项目中包含的命令，用来快速生成`setup.py`文件

### 配置上传时账号密码
```shell script
$ vim ~/.pypirc

[distutils]
index-servers: internal

[internal]
repository: <your private pypi address>
username: <your username>
password: <your password>
```

### 上传setup命令包
本项目中包含了快速生成`setup.py`的方法，运行如下命令上传你的第一个私有包
```shell script
# 打包本项目下的setup命令包
$ python setup.py bdist_wheel --verbose

# 上传setup命令包
$ twine upload dist/*
```


### 安装setup命令

- 安装setup命令
```shell script
$ pip install -i <your private pypi address>/simple setup
```

## 构建私有包
```shell script
# 为你的项目生成setup.py文件
$ setup <you project name>
```

### 上传

- 执行命令
```shell script
# 打包本项目下的setup命令包
$ python setup.py bdist_wheel --verbose

# 上传setup命令包
$ twine upload dist/*
```

### 下载

- 执行命令后，按照提示输入账号密码
```shell script
$ pip install -i <your private pypi address>/simple <your package name>
```

## 问题

- 上传之后重新编译镜像，会导致之前的包消失吗？
A: 不会，如果不出意外，你将会在你宿主电脑`~/.package/`下找到你上传的私有包
