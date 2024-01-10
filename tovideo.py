import os 
import cv2
import readresult
path = "../datasets/dog/dog-1/img/"
# path = "../datasets/shenfenzheng/test/202169-10475/"
# path = "../datasets/shenfenzheng/test/202169-10505/"
# path = "../datasets/shenfenzheng/test/20210609_111212/"
result_path = "/home/fengshuo/code/HCAT/results/LaSOT/HCAT/dog-1.txt"
# result_path= "/home/fengshuo/code/HCAT/results/LaSOT/HCAT/202169-10475.txt"
# result_path= "/home/fengshuo/code/HCAT/results/LaSOT/HCAT/202169-10505.txt"
# result_path= "/home/fengshuo/code/HCAT/results/LaSOT/HCAT/20210609-111212.txt"


result = readresult.readresult(result_path)

filelist = os.listdir(path)
filelist = sorted(filelist)

fps = 24  # 视频每秒24帧
size = (1280,720)
# size = (640,480)
# size = (1920,1080)  # 需要转为视频的图片的尺寸
# 可以使用cv2.resize()进行修改

#video = cv2.VideoWriter("VideoTest2.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
# 视频保存在当前目录下
# video = cv2.VideoWriter("VideoTest4_full.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
# video = cv2.VideoWriter("VideoTest3_full.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

video = cv2.VideoWriter("VideoTest2_full.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

idx = 0
for item in filelist:
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        print(item)
        item = path + item
        img = cv2.imread(item)
        x = float(result[idx][0])
        y = float(result[idx][1])
        w = float(result[idx][2])
        h = float(result[idx][3])
        x1 = x 
        x2 = x +  w
        y1 = y 
        y2 = y +  h 
        cv2.rectangle(img, (int(x1),int(y1)),(int(x2),int(y2)),(0,0,255))
        video.write(img)
    idx += 1

print("done")
video.release()
cv2.destroyAllWindows()