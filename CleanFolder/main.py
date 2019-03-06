# _*_ coding: utf-8 _*_

import os
import shutil


# 返回传入路径 f 的子目录，这里为了避免重复添加，省略了exe文件夹的遍历
def getDirsList(f):
    f = str(f)
    if f == "":
        return []
    f = f.replace("/", "\\")
    if f[-1] != "\\":
        f = f + "\\"
    return [x + '\\' for x in os.listdir(f) if os.path.isdir(f + x) and x != "exe"]


# 返回传入路径 f 文件夹下的所有文件，未加筛选
def getFilesLists(f):
    f = str(f)
    if f == "":
        return []
    f = f.replace("/", "\\")
    if f[-1] != "\\":
        f = f + "\\"
    return [x for x in os.listdir(f) if os.path.isfile(f + x)]


def clean(f):
    # print(f)
    nowfiles = getFilesList(f)
    print(nowfiles)
    for i in nowfiles:
        a, b = os.path.splitext(i)
        if b == '.exe':
            if not os.path.exists(f + '\\exe\\'):
                os.mkdir(f + '\\exe\\')
            shutil.move(f + i, f + '\\exe\\')
    nowdirs = getDirsList(f)
    for i in nowdirs:
        clean(f + i)


# 此处设置起始路径，包括本目录及其子目录中的exe文件将被整理
origin = "D:\\Code\\"

if __name__ == '__main__':
    clean(origin)
