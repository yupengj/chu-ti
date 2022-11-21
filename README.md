# 自动出题程序

目的是给小学1年级自动出算数题并支持打印。

![页面](/image.png "主界面")

# 导出 exe 文件

```commandline
pyinstaller -D -w 'D:\sourceCode\chu-ti\main.py' -p 'D:\sourceCode\chu-ti\html_template.py' -p 'D:\sourceCode\chu-ti\question_bank.py' -p 'D:\sourceCode\chu-ti\venv\Lib\site-packages' -p 'D:\sourceCode\chu-ti\venv\Lib\site-packages\pywin32_system32' -i 'D:\sourceCode\chu-ti\logo.ico' 
```

## 遇到错误1

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
ModuleNotFoundError: No module named 'tkhtmlview'
```

增加 -p 'D:\sourceCode\chu-ti\venv\Lib\site-packages'

## 遇到错误2

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
ImportError: DLL load failed while importing win32api: 找不到指定的模块。
```

增加 -p 'D:\sourceCode\chu-ti\venv\Lib\site-packages\pywin32_system32'