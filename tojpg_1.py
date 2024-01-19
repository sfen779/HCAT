import cv2
import os 

# video_path = "./data/lasot/fanzhuan"
# img_path = "./data/lasot/fanzhuan/fanzhuan-"

video_path = "./data/lasot/qiehuan1"
img_path = "./data/lasot/qiehuan1/qiehuan-"


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
        fps = vc.get(cv2.CAP_PROP_FPS)
        print("fps:",fps)
 
        rval = vc.isOpened()

        while(rval):
            c = c+1
            rval, frame = vc.read()
            if not rval:
                break
            pic_path = folder_name+'/'
            if rval:
                cv2.imwrite(pic_path + str(c).zfill(8) + ".jpg", frame)
                cv2.waitKey(1)
            else:
                break
        vc.release()
        
        print('jpg save success.')
        print("video name:", video_name)
        print(folder_name)
        idx += 1
save_img(video_path,img_path)



        
