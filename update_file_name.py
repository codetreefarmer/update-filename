# _*_coding:UTF-8_*_
# @Time: 2018/3/15 11:59 
# @Author: yw s 
# @File: update_file_name.py 
# @Software: PyCharm

"""
os.walk()函数可以得到一个三元tupple(dirpath, dirnames, filenames)
"""
import os

#需要修改文件的绝对路径,
file_path = "D:\Program Files (x86)\YouKu\Youku Files\\transcode"

def update_file_name(file_path):
    """批量修改文件名"""
    file_name = next(os.walk(file_path))[2]
    for index,i in enumerate(file_name):
        os.rename(os.path.join(file_path,i), os.path.join(file_path, str(index+1) + "." + i[6:]))

update_file_name(file_path)