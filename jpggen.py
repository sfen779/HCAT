import os
import cv2
from tqdm import tqdm

def readresult(p):
    #print(1)
    #return the x,y,w,h in a string format
    '''
    return the x,y,w,h in a string format
    '''
    result = []
    f = open(p,"r")
    lines = f.readlines()
    for line in lines:
        #print("line is :",line)
        tmp = line.strip().split() 
        result.append(tmp)
    return(result)

def readconf(p):
    '''
    return the confidence score of the coresponding result
    '''
    result = []
    f = open(p,"r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        result.append(line)
    return(result)
# result = readresult("/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrack/seqtrack_b384/lasot/dog-1.txt")
# path = "/home/fengshuo/code/VideoX-master/SeqTrack/data/lasot/dog/dog-1/img/"
# save_out = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrack/seqtrack_b384/lasot/img/"

result = readresult("/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/id-1.txt")
conf_score = readconf("/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/id-1_conf_score.txt")
path = "/home/fengshuo/code/VideoX-master/SeqTrack/data/lasot/id/id-1/img/"
save_out = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/img/id/id-1/"

filelist = os.listdir(path)
filelist = sorted(filelist)
idstring = "id"
warningstring = "WARNING!"
idx = 0
font = cv2.FONT_HERSHEY_SIMPLEX
for item in tqdm(filelist):
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        # print(item)
        item_in = path + item
        img = cv2.imread(item_in)
        x = float(result[idx][0])
        y = float(result[idx][1])
        w = float(result[idx][2])
        h = float(result[idx][3])
        x1 = x 
        x2 = x +  w
        y1 = y 
        y2 = y +  h 
        if float(conf_score[idx])>3.0 or float(conf_score[idx])<1.0:
            #the abnormal confidence score
            cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)
            cv2.line(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)
            cv2.line(img,(int(x1),int(y2)),(int(x2),int(y1)),(0,0,255),2)
            
            
            cv2.putText(img,"{}:{}".format(warningstring,conf_score[idx]),(int(x1),int(y1)-15),font,2,(0,0,255),2)
            if int(y1)<15:
                cv2.putText(img,"{}:{}".format("id card",conf_score[idx]),(int(x1),int(y1)+40),font,2,(0,0,255),2)
        else:
            #normal confidence score
            cv2.rectangle(img, (int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)
            cv2.putText(img,"{}:{}".format("id card",conf_score[idx]),(int(x1),int(y1)-15),font,2,(0,0,255),2)
            if int(y1)<15:
                cv2.putText(img,"{}:{}".format("id card",conf_score[idx]),(int(x1),int(y1)+40),font,2,(0,0,255),2)
        item_out = save_out + item
        cv2.imwrite(item_out, img)
        # print(item_out,"written")
        # if idx ==120:
        #     break
    idx += 1

print("done")
cv2.destroyAllWindows()

