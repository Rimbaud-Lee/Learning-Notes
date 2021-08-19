
import os, shutil

def copy_file(path1, path2, key_word):
    num = 1
    for foldName, subfolders, filenames in os.walk(path1):
        for filename in filenames:
            if filename.endswith(key_word):
                new_name = filename.replace(filename, "%i"+"_"+filename)%num
                shutil.copyfile(os.path.join(foldName, filename), os.path.join(path2, new_name))
                print(filename, "copy as", new_name)
                num += 1

if __name__ == '__main__':
    path1 = input("请输入你想复制的文件夹的绝对路径：")
    path2 = input("请输入你想复制进的文件夹的绝对路径：")
    key_word = input("请输入你想复制文件的后缀名：")
    copy_file(path1, path2, key_word)