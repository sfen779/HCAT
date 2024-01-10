# -*- coding: utf-8 -*-

import os
import hashlib
import shutil
import datetime

from datetime import datetime

import cv2

import cv2
import numpy as np
def is_modified_on_date(file_path, target_date):
    modification_time = os.path.getmtime(file_path)
    modification_date = datetime.fromtimestamp(modification_time).date()
    return modification_date == target_date

def copy_image(src_root, des_root):
    if not os.path.exists(des_root):
        os.makedirs(des_root)


    # 遍历源目录中的所有文件和文件夹
    for root, dirs, files in os.walk(src_root):
        for file in files:
            # 获取文件的完整路径
            src_file = ''
            des_file = ''
            src_file = os.path.join(root, file)

            if file.endswith('.svg') or file.endswith('.下载') or file.endswith('.css') or file.endswith('.html') or file.endswith('.svg') or file.endswith('.svg'):
                try:
                    os.remove(file)
                except:
                    pass

            hash_value = hashlib.md5(open(src_file, 'rb').read()).hexdigest()
            # 构建目标文件路径

            # 判断文件扩展名是否为图像名
            ext = os.path.splitext(file)[-1].lower()
            image_extensions = ['.jpg', '.bmp', '.gif', '.jfif', '.png']  # 图像名的扩展名列表
            if ext in image_extensions:
                des_file = os.path.join(des_root, hash_value + ext)


            # 判断文件名是否为images(xx)的文件
            if file.startswith("images(") and file.endswith(")"):
                des_file = os.path.join(des_root, hash_value + ".jpg")



            if file.endswith("=JPEG") :
                des_file = os.path.join(des_root, hash_value + ".jpg")


            if file.endswith('=PNG'):
                des_file = os.path.join(des_root, hash_value + ".png")


            if file.startswith("OIP-"):
                des_file = os.path.join(des_root, hash_value + ".jpg")


            if not des_file == '':
                try:
                    image_path_bytes = src_file.encode('utf-8')
                    image_data = np.fromfile(image_path_bytes, dtype=np.uint8)
                    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
                    cv2.imwrite(des_file, image)
                except:
                    pass





if __name__ == "__main__":

    copy_image(r'D:\fs\down\bridge', r'D:\fs\down\bridge')
    copy_image(r'D:\fs\down\bridge\jpg', r'D:\fs\down\bridge\jpg')