# 自动出题程序

目的是给小学1年级自动出算数题并支持打印。

![页面](/image.png "主界面")

# 导出 exe 文件

pyinstaller -F -w -i 'D:\sourceCode\chu-ti\logo.ico' -n chuti 'D:\sourceCode\chu-ti\main.py'

pyinstaller -F -p 'D:\sourceCode\chu-ti\Lib' -w -n chuti 'D:\sourceCode\chu-ti\main.py'

pyinstaller -D -w 'D:\sourceCode\chu-ti\main.py' -p 'D:\sourceCode\chu-ti\html_template.py' -p 'D:\sourceCode\chu-ti\question_bank.py'
