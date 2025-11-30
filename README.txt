========================================
Edinburgh Graveyard Map - 服务器部署包
========================================

这个文件夹包含所有需要上传到学校服务器的文件。

文件清单：
---------
1. 01_create_tables_clean.sql  - Oracle 建表脚本
2. 02_insert_data.sql          - 插入 35 个墓地数据
3. app.py                      - 后端 Python CGI 脚本
4. frontend/                   - 前端所有文件（React 打包后）

部署步骤：
---------

=== 第 1 步：建表和插入数据 ===

在 XRDP 终端：

sqlcl
Username: s2835812
Password: 252525

SQL> @01_create_tables_clean.sql
SQL> @02_insert_data.sql
SQL> SELECT COUNT(*) FROM graveyards;
SQL> exit


=== 第 2 步：部署后端 ===

mkdir -p ~/cgi-bin/graveyard_api
cd ~/cgi-bin/graveyard_api
nano app.py

把 app.py 的内容粘贴进去（密码已经配置好）
保存退出

chmod +x app.py


=== 第 3 步：部署前端 ===

mkdir -p ~/public_html/graveyard_map
cd ~/public_html/graveyard_map

把 frontend/ 文件夹里的所有文件复制到这里
（包括 index.html, assets/, data/, 所有图片和 CSS）


=== 第 4 步：测试 ===

测试后端：
python3 ~/cgi-bin/graveyard_api/app.py

应该输出 35 个墓地的 JSON 数据

浏览器访问：
https://www.geos.ed.ac.uk/~s2835812/graveyard_map/

应该看到完整的交互地图网站


完成！
