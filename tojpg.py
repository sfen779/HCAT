import cv2
import os 

# video_path = "./data/lasot/fanzhuan"
# img_path = "./data/lasot/fanzhuan/fanzhuan-"

video_path = "./data/lasot/qiehuan"
img_path = "./data/lasot/qiehuan/qiehuan-"

def full_occlusion_gen(idx,img_path):
    occlusion = ["0" for _ in range(idx)]
    connected_string = ",".join(occlusion)
    with open(img_path+"full_occlusion.txt", "w") as file:
        file.write(connected_string)
    print("full occlusion written")

def groundtruth_gen(idx,img_path):
    anno = "255,255,255,255"
    all_lines = [anno for _ in range(idx)]
    with open(img_path + "groundtruth.txt", "w") as file:
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
        idx += 1
        full_occlusion_gen(c, file_path)
        groundtruth_gen(c,file_path)
        nlp_gen(file_path)
        out_gen(c,file_path)


save_img(video_path,img_path)



        
