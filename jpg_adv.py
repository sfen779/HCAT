import os
import cv2

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

result = readresult("/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrack/seqtrack_b384/lasot/dog-1.txt")
path = "/home/fengshuo/code/VideoX-master/SeqTrack/data/lasot/dog/dog-1/img/"
save_out = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrack/seqtrack_b384/lasot/img/"

filelist = os.listdir(path)
filelist = sorted(filelist)

idx = 0
for item in filelist:
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        print(item)
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
        cv2.rectangle(img, (int(x1),int(y1)),(int(x2),int(y2)),(0,0,255))
        item_out = save_out + item
        cv2.imwrite(item_out, img)
        # print(item_out,"written")
        # if idx ==120:
        #     break
    idx += 1

print("done")
cv2.destroyAllWindows()






def main():
    parser = argparse.ArgumentParser(description='Run tracker on sequence or dataset.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param', type=str, help='Name of config file.')
    parser.add_argument('--runid', type=int, default=None, help='The run id.')
    parser.add_argument('--dataset_name', type=str, default='lasot', help='Name of dataset (otb, nfs, uav, got10k_test, lasot, trackingnet, lasot_extension_subset, tnl2k).')
    parser.add_argument('--sequence', type=str, default=None, help='Sequence number or name.')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--threads', type=int, default=0, help='Number of threads.')
    parser.add_argument('--num_gpus', type=int, default=8)

    args = parser.parse_args()

    try:
        seq_name = int(args.sequence)
    except:
        seq_name = args.sequence

    run_tracker(args.tracker_name, args.tracker_param, args.runid, args.dataset_name, seq_name, args.debug,
                args.threads, num_gpus=args.num_gpus)


if __name__ == '__main__':
    main()