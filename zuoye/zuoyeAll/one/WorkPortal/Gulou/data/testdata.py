import csv

# 设计函数专门读取 csv文件
# 参数1 文件名 参数2： 读取的行数
def get_csv_data(csv_file,line):
        zs_csv_file= open(csv_file, 'r', encoding='utf-8-sig')# 打开文件
        reader = csv.reader(zs_csv_file) # 加载数据
        # 参数2 :决定了下标位置的开始计数方式
        for index, row in enumerate(reader, 1):
            if index == line:
                print(row)
                return row
if __name__=="__main__":# 自测
    #参数１　　当前的ｃｓｖ文件
    #　参数２　　　行数
    get_csv_data("./account.csv",1)