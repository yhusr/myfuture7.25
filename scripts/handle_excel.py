import openpyxl
from scripts.handle_path import excel_path


class MyExcel:
    pass


class HandleExcel:
    def __init__(self, sheetname, path=None):
        if path:
            self.filepath = path
        else:
            self.filepath = excel_path
        self.shname = sheetname

    def open_excel(self):
        self.shbook = openpyxl.open(self.filepath)
        self.sh = self.shbook[self.shname]

    def read_excel(self):
        self.open_excel()
        row_data = list(self.sh.rows)
        head_li = [h.value for h in row_data[0]]
        list1 = []
        for r in row_data[1:]:
            my_oper = MyExcel()
            row_li = [rd.value for rd in r]
            excel_zip = zip(head_li, row_li)
            for my_zip in excel_zip:
                setattr(my_oper, my_zip[0], my_zip[1])
            list1.append(my_oper)
        self.shbook.close()
        return list1

    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sh.cell(row=row_num, column=col_num, value=value)
        self.shbook.save(self.filepath)
        self.shbook.close()


if __name__ == '__main__':
    he = HandleExcel('register')
    excel_oper = he.read_excel()
    my_data = excel_oper[0].data
    print(my_data)