import os  
import json  
from pycocotools.coco import COCO  
  
# 指定COCO数据集的路径  
data_dir = 'D:\\fs\\down\\'  
  
# 指定输出目录  
output_dir = 'D:\\fs\\down\\filtered_images3'  
  
# 初始化COCO对象  
coco = COCO(os.path.join(data_dir, 'annotations', 'instances_default.json'))  
  
# 遍历训练集中的所有图片  
image_ids = coco.getImgIds()  
for image_id in image_ids:  
    # 获取图片路径和标注信息  
    img_info = coco.loadImgs([image_id])[0]  
    img_path = os.path.join(data_dir, 'images', img_info['file_name'])  
    ann_ids = coco.getAnnIds(imgIds=image_id)  
    anns = coco.loadAnns(ann_ids)  
    # 如果有标注，则将图片和标注复制到输出目录  
    if len(anns) > 0:  
        os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)  
        os.makedirs(os.path.join(output_dir, 'annotations'), exist_ok=True)  
        img_out_path = os.path.join(output_dir, 'images', img_info['file_name'])  
        with open(img_out_path, 'wb') as f:  
            f.write(open(img_path, 'rb').read())  
        anns_out_path = os.path.join(output_dir, 'annotations', f'{image_id}.json')  
        with open(anns_out_path, 'w') as f:  
            json.dump(anns, f)