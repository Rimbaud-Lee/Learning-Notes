
import os, shutil

def copy_file(path1, path2):
    for foldName, subfolders, filenames in os.walk(path1):
        for filename in filenames:
            shutil.copyfile(os.path.join(foldName, filename), os.path.join(path2, filename))
            print(filename, "已复制完成")


if __name__ == '__main__':
    path1 = input("请输入你想复制的文件夹的绝对路径：")
    path2 = input("请输入你想复制进的文件夹的绝对路径：")
    copy_file(path1, path2)