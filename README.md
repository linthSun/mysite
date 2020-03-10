# mysite
# it is a demo about django
下载启动mysql数据库
创建数据库 demo

运行intall.bat 安装依赖

同步或者更改生成 数据库：
python manage.py makemigrations
python manage.py migrate


创建管理员：
python manage.py createsuperuser

启动项目：
python manage.py runserver 8080