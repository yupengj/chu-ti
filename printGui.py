from tkinter import *
from tkinter import ttk
from tkhtmlview import HTMLLabel, HTMLText
import win32api
import win32print
import tempfile
import pdfkit
import shijuan
import suanshu

print_html = []

max_width = 1300
max_height = 1000

root = Tk()
root.title("自动出题")
root.geometry("{}x{}".format(max_width, max_height))


# 获取打印机列表
def get_printer_list():
    print_list = []
    printers = list(win32print.EnumPrinters(2))
    for i in printers:
        print_list.append(i[2])
    print(print_list)
    return print_list


# 增加选择打印机组件
printerLab = Label(root, text="选择打印机")
printerValue = StringVar()
printerEntity = ttk.Combobox(root, textvariable=printerValue)
printerEntity['values'] = get_printer_list()
printerValue.set("Canon TS3300 series")
printerLab.place(x=50, y=10, width=100, anchor='nw')
printerEntity.place(x=160, y=10, width=200, anchor='nw')


def html_to_pdf(html_file):
    # Define path to wkhtmltopdf.exe
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

    # Point pdfkit configuration to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    output_path = tempfile.mktemp(".pdf")
    # Convert HTML file to PDF
    pdfkit.from_file(html_file, output_path=output_path, configuration=config)

    return output_path


# 开始打印方法
def start_print():
    # result_text = tiMuEntity.get("1.0", END)
    print("打印内容：" + print_html[0])
    printer = printerEntity.get()
    print("打印机：" + printer)
    filename = tempfile.mktemp(".html")
    open(filename, "w", encoding="UTF-8").write(print_html[0])
    print(filename)
    pdf_name = html_to_pdf(filename)
    print(pdf_name)

    win32api.ShellExecute(0, "print", '"%s"' % pdf_name, '"%s"' % printer, ".", 0)


# 出题方法
def chu_ti():
    print("一共有几道题: {}".format(countValue.get()))
    print("运算类型: {}".format(optValue.get()))
    print("几个数运算: {}".format(optCountValue.get()))
    print("计算结果最大值: {}".format(resultValue.get()))

    # 清空所有数据
    tis = suanshu.chu_ti(100, resultValue.get(), optCountValue.get(), countValue.get())
    html = shijuan.shi_juan(tis, 3, 14)
    print_html.append(html)
    tiMuEntity.set_html(html)


Button(root, text="出题", command=chu_ti).place(x=10, y=80)

Button(root, text="打印", command=start_print).place(x=10, y=10)

# 总题数
countLab = Label(root, text="一共有几道题")
countValue = IntVar()
countEntity = Entry(root, width=6, textvariable=countValue)
countValue.set(50)
countLab.place(x=50, y=50, width=100, anchor='nw')
countEntity.place(x=150, y=50, width=80, anchor='nw')

# 运算类型
optLab = Label(root, text="运算类型")
optValue = StringVar()
optEntity = ttk.Combobox(root, textvariable=optValue)
optEntity['values'] = ["加法", "减法", "加减混合"]
optValue.set("加减混合")
optLab.place(x=230, y=50, width=100, anchor='nw')
optEntity.place(x=330, y=50, width=80, anchor='nw')

# 几个数运算
optCountLab = Label(root, text="几个数运算")
optCountValue = IntVar()
optCountEntity = Entry(root, textvariable=optCountValue)
optCountValue.set(3)
optCountLab.place(x=410, y=50, width=100, anchor='nw')
optCountEntity.place(x=510, y=50, width=80, anchor='nw')

# 运算结果最大值
resultLab = Label(root, text="计算结果最大值")
resultValue = IntVar()
resultEntity = Entry(root, textvariable=resultValue)
resultValue.set(200)
resultLab.place(x=590, y=50, width=100, anchor='nw')
resultEntity.place(x=690, y=50, width=80, anchor='nw')

# 出题结果
tiMuEntity = HTMLText(root)
tiMuEntity.place(x=10, y=120, width=max_width - 20, height=800)

root.mainloop()
