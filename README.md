## 环境
python==3.6.1
django==2.2.2
adminlte==2.4.10

### settings.py
TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR,  'static'),)

import pymysql         # 一定要添加这两行！           
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'mysite',                       # 数据库名，先前创建的
        'USER': 'root',                         # 用户名，可以自己创建用户
        'PASSWORD': '****',                     # 密码
        'HOST': '192.168.1.121',                # mysql服务所在的主机ip
        'PORT': '3306',                         # mysql服务端口
    }
}

### django
pip install django==2.2.2
pip install 

### 参考链接
[刘江的博客教程](http://www.liujiangblog.com/course/django/125)