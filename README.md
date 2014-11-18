目录说明:  
data:数据集  
自行将images文件夹添加到data目录下  
source:源码  

环境准备:  
在机器上安装好python,pip包管理工具  

在该根目录下直接安装所需的软件依赖包:   
sudo apt-get install libfreeimage-dev  
pip install -r requirements.txt  

代码运行:  
进入到sources目录后,  
运行以下语句  
python jug.py execute #执行计算任务  
运行以下语句  
python jug.py status  #查看任务执行情况  
