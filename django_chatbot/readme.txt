1,先需要安装Python 3.11及以上版本,和conda 22.9及以上版本

2,打开命令行CMD窗口,输入指令cd /d <项目源文件所在目录>

3.在CMD中使用以下指令以创建虚拟环境和项目所需要的对应版本的包

    创建新环境并将项目需要的包导入进环境中

conda env create -f environment.yml -n <新环境的名称>

    激活新环境

conda activate <新环境的名称>

4,将数据进行迁移

python manage.py makemigration

python manage.py migrate

5.启动本地服务

python manage.py runserver

这样之后,项目则会在http://127.0.0.1:8000/上运行