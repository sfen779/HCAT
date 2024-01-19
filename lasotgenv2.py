import os 
import json

def get_info(dataset,index):
    info_path = "/home/fengshuo/code/HCAT/data/lasot/{}/lasot_img/{}-{}/".format(dataset,dataset,index)
    print(info_path)
    groundtruth = []
    full_occlusion = []
    for file_name in os.listdir(info_path):
        source_file = os.path.join(info_path,file_name)
        if os.path.isfile(source_file):
            if source_file.endswith(".txt"):
                if "groundtruth" in source_file:
                    with open(source_file,"r") as f:
                        for line in f:
                            temp = []
                            for cord in line.strip().split(","):
                                temp.append(int(cord))
                            groundtruth.append(temp)
                            break
            ## for the real full size info, use below
            ## for the mocked info, use above
                        
            # if source_file.endswith(".txt"):
            #     if "full_occlusion" in source_file:
            #         with open(source_file,"r") as f:
            #             for line in f:
            #                 for char in line.strip().split(","):
            #                     full_occlusion.append(int(char))
            #     elif "groundtruth" in source_file:
            #         with open(source_file,"r") as f:
            #             for line in f:
            #                 temp = []
            #                 for cord in line.strip().split(","):
            #                     temp.append(int(cord))
            #                 groundtruth.append(temp) 
            #     elif "nlp" in source_file:
            #         with open(source_file,"r") as f:
            #             for line in f:
            #                 nlp=line.strip()
            #     else:
            #         with open(source_file,"r") as f:
            #             for line in f:
            #                 out_of_view = line.strip()
        else:
            #img_path_root = "code/HCAT/data/lasot/{}/lasot_img/{}-{}/img/".format(dataset,dataset,index)
            img_path = "{}-{}/img/".format(dataset,index)
            img_names =[]
            imgs = os.listdir(source_file)
            imgs.sort(key = lambda x:int(x[:-4]))
            img_nums = len(imgs)
            for i in range(img_nums):
                img_name = img_path + imgs[i]
                img_names.append(img_name)



            # for img_name in os.listdir(source_file):
            #     img_names.append(img_path+img_name)
    return temp,img_names

def img_path_gen(dataset_name):
    img_path = "code/HCAT/data/lasot/{}/lasot_img/".format(dataset_name)
    return img_path

def hcat_json_gen(dataset_name):
    outer_dict = {}

    data_dir = "/home/fengshuo/code/HCAT/data/lasot/{}/lasot_img/".format(dataset_name)
    try:
        for i in range(len(os.listdir(data_dir))):

            inner_dict = {"video_dir":0, "init_rect":0, "img_names":0, "gt_rect":0, "attr":0, "absent":0}
            
            init_bbox,img_names = get_info(dataset_name,i)

            img_path = data_dir+"{}-{}".format(dataset_name,i) + "/img/"

            img_nums = len(img_names)

            inner_dict["video_dir"]= data_dir
            inner_dict["init_rect"]= init_bbox
            inner_dict["img_names"]= img_names
            inner_dict["gt_rect"] = [[1,1,1,1] for _ in range(img_nums)]
            inner_dict["gt_rect"][0] = init_bbox
            inner_dict["attr"]=["Partial Occlusion", "Deformation", "Background Clutter", "Scale Variation", "Out-of-View", "Low Resolution", "Aspect Ratio Change"]
            inner_dict["absent"] = [1 for _ in range(img_nums)]
            print(inner_dict)
            outer_dict["{}-{}".format(dataset_name,i)]= inner_dict
            print(init_bbox)
    except FileNotFoundError:
        print("LaSOT updated.")

    with open(data_dir+"LaSOT.json","w") as f:
        json.dump(outer_dict,f)
        print("written to json file")
    print(data_dir)

def main(dataset_name):
    hcat_json_gen(dataset_name)

if __name__ == "__main__":
    dataset_name = "qiehuan1"
    main(dataset_name)

    #a,b = get_info("fanzhuan", 1)
    #print(a,b)
