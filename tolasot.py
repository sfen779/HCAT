import cv2
import os 

video_path = "./data/lasot/fanzhuan"
img_path = "./data/lasot/fanzhuan/fanzhuan-"

# video_path = "./data/lasot/qiehuan"
# img_path = "./data/lasot/qiehuan/qiehuan-"
frame1_path = "/home/fengshuo/code/VideoX-master/SeqTrack/data/lasot/fanzhuan/frame1.txt"

## 运行以前，先把身份证的两个角的坐标以类似 251,199 383,286 的格式保存在 frame1_path文件中
## 再运行此脚本则可以自动生成lasot格式的数据集

def full_occlusion_gen(idx,img_path):
    occlusion = ["0" for _ in range(idx)]
    connected_string = ",".join(occlusion)
    with open(img_path+"full_occlusion.txt", "w") as file:
        file.write(connected_string)
    print("full occlusion written")

def parse_coordinates(coord_str):
    """解析单个坐标字符串，返回(x, y)元组。"""
    x, y = coord_str.split(',')
    return int(x), int(y)

def calculate_differences(file_path):
    """计算文件中每行坐标之间的差异，并返回差异列表。"""
    differences = []
    with open(file_path, 'r') as file:
        for line in file:
            coord1_str, coord2_str = line.split()
            x1, y1 = parse_coordinates(coord1_str)
            x2, y2 = parse_coordinates(coord2_str)
            diff_x = x2 - x1
            diff_y = y2 - y1
            differences.append([str(x1),str(y1),str(diff_x),str(diff_y)])
    return differences

diff= calculate_differences(frame1_path)

def groundtruth_gen(idx,img_path, i):
    frame1 = ",".join(diff[i])
    anno = "255,255,255,255"
    all_lines = [anno for _ in range(idx-2)]
    with open(img_path + "groundtruth.txt", "w") as file:
        file.write(frame1+"\n")
        for line in all_lines:
            file.write(line+"\n")
    print("groundtruth written")

def nlp_gen(img_path):
    nlp = "test"
    with open(img_path+"nlp.txt","w") as file:
        file.write(nlp)
    print("nlp written")

def out_gen(idx,img_path):
    out = ["0" for x in range(idx)]
    connected_string = ",".join(out)
    with open(img_path+"out_of_view.txt", "w") as file:
        file.write(connected_string)
    print("out of view written")

def save_img(video_path,img_path):
    videos = os.listdir(video_path)
    idx = 0
    for video_name in videos:
        #get the name before the dot prefix
        file_path = img_path + str(idx)+"/"
        folder_name = img_path + str(idx) + "/img/"
        os.makedirs(folder_name,exist_ok=True)
        vc = cv2.VideoCapture(video_path+"/"+video_name)
        c = 0
 
        rval = vc.isOpened()

        while(rval):
            c = c+1
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if rval:
                cv2.imwrite(pic_path + str(c).zfill(8) + ".jpg", frame)
                cv2.waitKey(1)
            else:
                break
        vc.release()
        
        print('jpg save success.')
        print(folder_name)
        full_occlusion_gen(c, file_path)
        groundtruth_gen(c,file_path,idx)
        nlp_gen(file_path)
        out_gen(c,file_path)
        idx += 1


save_img(video_path,img_path)



        
