
import os
import os.path as ph


def get_file_path(path1, list2, list4):
    list_1 = os.listdir(path1)
    for i in range(len(list_1)):
        list_1[i] = ph.join(path1, list_1[i])
        if ph.isfile(list_1[i]):
            list2.append(list_1[i])
        else:
            list4.append(list_1[i])
            get_file_path(list_1[i], list2, list4)


def make_directories(list4, path2):
    list4.sort(key=lambda x:x.count('\\'))
    files_name = list4[0]
    files_name = files_name[files_name.rfind('\\')+1:]
    path2 = path2 + '\\' + files_name
    for i in range(len(list4)):
        str_1 = list4[i]
        str_2 = path2 + str_1[str_1.find(files_name)+len(files_name):]
        list4[i] = str_2
        os.mkdir(list4[i])

        
def copy_files(list4, list2, path2, key_word):
    files_name = list4[0]
    files_name = files_name[files_name.rfind('\\') + 1:]
    path2 = path2 + '\\' + files_name
    list2.sort(key=lambda x:x.count('\\'))
    for i in range(len(list2)):
        if key_word == ph.splitext(list2[i])[1]:
            str_1 = list2[i]
            str_2 = path2 + str_1[str_1.find(files_name)+len(files_name):]
            print('正在复制文件%s到%s当中'%(list2[i], str_2))
            with open(list2[i], 'rb') as f:
                content = f.read()
            with open(str_2, 'wb') as f:
                f.write(content)

                
if __name__ == '__main__':
    list2 = []; list4 = []
    path1 = input('请输入你想复制的文件夹的绝对路径:')
    list4.append(path1)
    get_file_path(path1, list2, list4)
    path2 = input('请输入你想复制进的文件夹的绝对路径:')
    make_directories(list4, path2)
    key_word = input('请输入你想复制文件的后缀名:')
    copy_files(list4, list2, path2, key_word)
    
