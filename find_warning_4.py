import os
import shutil
def combine_conf_bbox(path,dataset_name, combined_result_path):
    idx = 0
    results = os.listdir(path)
    combined = []
    warnings = []
    print(len(results))
    for idx in range(int(len(results)/3)):
        
        conf_name = path + "/" + dataset_name +"-"+ str(idx) +"_conf_score.txt"
        bbox_name = path + "/" + dataset_name + "-" + str(idx) + ".txt"
        target_name = combined_result_path+"/"+dataset_name +"-"+str(idx) + "_combined.txt"
        with open(conf_name,"r") as f:
            conf = []
            for lines in f:
                conf.append(lines.strip())
        with open(bbox_name, "r") as b:
            bbox = []
            for lines in b:
                bbox.append(lines.strip())
        with open(target_name, "w") as tar:
            for i in range(len(bbox)):
                tar.write(bbox[i] +" "+ conf[i] + "\n")
                if float(conf[i])<1.0 or float(conf[i])>3.0:
                    warnings.append([idx, i, conf[i], bbox[i]])
    warning_name = combined_result_path +"/" + dataset_name + "_warnings.txt"
    with open(warning_name, "w") as warn:
        warn.write("dataset-index,frame,conf,bbox\n")
        for warning in  warnings:
            warn.write(str(warning[0])+","+str(warning[1])+","+str(warning[2])+","+warning[3]+"\n")
        
        #combined.append([conf_name,bbox_name])
    return warnings

# path = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/qiehuan1"
# r_path = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/qiehuan1_combined"
# dataset_name = "qiehuan1"

# 源目录和目标目录

def copy_files(dataset_name: str):
# 确保目标目录存在
    source_folder = '/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/'
    target_folder = source_folder + dataset_name
    r_path = source_folder + dataset_name + "_combined"
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    if not os.path.exists(r_path):
        os.makedirs(r_path)

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_folder):
        if dataset_name in filename:  # 检查文件名中是否包含'fanzhuan'
            source_file = os.path.join(source_folder, filename)

            # 检查是否为文件
            if os.path.isfile(source_file):
                target_file = os.path.join(target_folder, filename)
                
                # 复制文件
                shutil.copy(source_file, target_file)

    print("符合条件的文件已复制完成。")
    result = combine_conf_bbox(target_folder,dataset_name,r_path)
    print(result)
    print("all done")

#path = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/fanzhuan"
#r_path = "/home/fengshuo/code/VideoX-master/SeqTrack/test/tracking_results/seqtrackcopy/seqtrack_b384/lasot/fanzhuan_combined"


#result = combine_conf_bbox(path,dataset_name,r_path)
if __name__ == "__main__":
    #dataset_name = "fanzhuan"
    dataset_name = "qiehuan1"
    copy_files(dataset_name)