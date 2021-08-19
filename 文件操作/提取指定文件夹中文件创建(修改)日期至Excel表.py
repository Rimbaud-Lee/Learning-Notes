
import os, time
import pandas as pd

def get_time(path1, path2, excelName):
    filenames = []
    cTimes = []
    mTimes = []
    files = os.listdir(path1)
    for file in files:
        fp = os.path.join(path1, file)
        createdTime = time.localtime(os.stat(fp).st_ctime)
        modifiedTime = time.localtime(os.stat(fp).st_mtime)
        cTime = time.strftime('%Y-%m-%d %H:%M:%S', createdTime)
        mTime = time.strftime('%Y-%m-%d %H:%M:%S', modifiedTime)
        filenames.append(file)
        cTimes.append(cTime)
        mTimes.append(mTime)
    d = {"文件名称":filenames, "创建时间":cTimes, "修改时间":mTimes}
    df = pd.DataFrame(d)
    df.to_excel(path2 + "\\" + excelName)

if __name__ == '__main__':
    path1 = input("请输入文件所在的文件夹的绝对路径：")
    path2 = input("请输入文件创建时间提取后的Excel表所在的文件夹的绝对路径：")
    excelName = input("请输入想创建的Excel名称(后缀名也要写，如.xlsx)：")
    get_time(path1, path2, excelName)
    print("提取完成！")