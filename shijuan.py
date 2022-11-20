def shi_juan(tis, column_count: 3, space: 8):
    html = """<!DOCTYPE html><html>
    <head><meta charset="utf-8"></head><body>"""
    html = html + "<h2 align='center'>日期___________班级___________姓名___________分数___________</h2>"
    # 最长的算式，用于等号对齐
    max_len = len(max(tis, key=lambda x: len(x)))
    # 最长算式加 space ，用于左右表达式间距
    one_len = max_len + space
    # 一行的列数
    column_count_temp = 1
    for item in tis:

        # 等号对齐，算式前面补齐空格
        start_len = max_len - len(item)
        # 算式编号
        index = str(tis.index(item) + 1) + "."
        # 算式 html 标签
        item_html = "<span style='font-size:16px;'>" + index + "</span>" + (start_len * " ") + item

        if column_count_temp == 1:
            html = html + "<pre style='font-size:24px;'>"
            html = html + item_html + (" " * (one_len - start_len - len(index) - len(item)))
            column_count_temp = column_count_temp + 1
        elif column_count_temp == column_count:
            html = html + item_html + "</pre>"
            column_count_temp = 1
        else:
            html = html + item_html + (" " * (one_len - start_len - len(item)))
            column_count_temp = column_count_temp + 1

    html = html + "</body></html>"
    return html


if __name__ == '__main__':
    html2 = shi_juan(["1+1sd=", "1+1=", "df1+1aaa=", "1+asdf1=", "1+1="])
    print(html2)
