目录说明:  
data:数据集  
自行将images文件夹添加到data目录下  
source:源码  
Coelho2009_ISBI_NuclearSegmentation:  
[论文A hand-segmented dataset and comparison of algorithms by Luis Pedro Coelho,Aabid Shariff and Robert F.Murphy.DOI相关源码](https://github.com/luispedro/Coelho2009_ISBI_NuclearSegmentation),可以运行通但主要还是通过以下方法对源码进行跟踪.

环境准备:  
在机器上安装好python,pip包管理工具  

在该根目录下直接安装所需的软件依赖包:   
sudo apt-get install libfreeimage-dev #解决FreeImage报错,主要是应为缺少freeimage开发库.  
使用如下命令安装相关python依赖包:  
pip install -r requirements.txt  (#numpy cast bug已解决)

代码运行:  
进入到sources目录后,  
运行以下语句  
python jug.py execute #执行计算任务  
运行以下语句  
python jug.py status  #查看任务执行情况  
