# coding:utf-8
import xlrd
class ExcelUtil():
    '''读取excel文件'''
    def __init__(self, excelPath, sheetName):
        '''
        excelPath:文件路径
        sheetName：读取的表格
        可写成sheetName="Sheet1"
        '''
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__ == "__main__":
    filepath = "E:\\数据.xlsx"    # 设置成为本格式后需重新写入
    sheetName = "Sheet1"
    data = ExcelUtil(filepath,sheetName)
    #print(data.dict_data())

    for i in data.dict_data():
        print(i)