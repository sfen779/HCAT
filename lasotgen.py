import os 
import json
#img_path = "../datasets/shenfenzheng/test/202169-10475/"
#img_path = "../datasets/shenfenzheng/test/202169-10505/"
img_path = "../datasets/shenfenzheng/test/20210609_111212/"

#init_bbox = [274,147,121,80]
# init_bbox = [288,199,162,100]
init_bbox = [741,227,552,361]

def save_img(img_path,init_bbox):
    img_dir = img_path.strip().split("/")[-2]
    inner_dict = {"video_dir":0, "init_rect":0, "img_names":0, "gt_rect":0, "attr":0, "absent":0}
    outer_dict = {}
    img_names = []
    imgs = os.listdir(img_path)
    imgs.sort()
    imgs.sort(key = lambda x:int(x[:-4]))
    img_nums = len(imgs)
    for i in range(img_nums):
        img_name= img_dir +"/" + imgs[i]
        img_names.append(img_name)


    inner_dict["video_dir"]= img_dir
    inner_dict["init_rect"]= init_bbox
    inner_dict["img_names"]= img_names
    inner_dict["gt_rect"] = [[1,1,1,1] for x in range(img_nums)]
    inner_dict["gt_rect"][0] = init_bbox
    inner_dict["attr"]=["Partial Occlusion", "Deformation", "Background Clutter", "Scale Variation", "Out-of-View", "Low Resolution", "Aspect Ratio Change"]
    inner_dict["absent"] = [1 for x in range(img_nums)]
    # outer_dict["202169-10505"]= inner_dict
    outer_dict["20210609-111212"] = inner_dict
    print(img_names)
    print(init_bbox)
    with open("../datasets/shenfenzheng/test/LaSOT.json","w") as f:
        json.dump(outer_dict,f)
        print("written to json file")
    print(img_dir)

save_img(img_path,init_bbox)