pyinstaller Algo_server.spec
生成的各个目录和文件的作用如下：

build/：该目录是pyinstaller生成的临时目录，用于存放编译过程中生成的中间文件和临时文件。
dist/：该目录是pyinstaller生成的最终目录，用于存放编译后生成的可执行文件或打包后的应用程序。



# 卓鸷集群协同项目

>  🌟 **项目目标 ：典型任务场景下的集群协同任务分配** 🚀

## 项目执行流程
<!-- ----------------------------------------------- -->

1. 安装依赖包
   ```python
   pip install -r requirements.txt
   遇到缺失，可以补充到 requirements.txt 中
   并再次 pip
   ```
2. 打开`PlaneData`包，并且打开window终端，执行:
    ```
    .\PlanData subscriber
    ```
3. 运行集群算法
项目在根目录下运行 集群算法
   ```python
   老版本
   python algo_port.py
   新版本
   main_controller.py
   ```
项目在 /simpy 目录下运行 软件仿真
   ```python
   python main_sim.py
   ```

4.当出现如下信息，表明运行成功：
![1721357811539](image/README/1721357811539.png)
