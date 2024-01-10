import cv2
import json
import os
folder_path = '.'

def crop_img(image_file):
    image  = cv2.imread(image_file)
    shape= image.shape
    #print(image.shape)
    #print(shape[1])
    # print(annotations)
    for image_name in annotations['images']:
        #print(image_name['file_name'])
        if image_name['file_name']==image_file:
            image_id = image_name['id']
            #print(image_id)
            break
    y_all = []
    h_all = []
    for annotation in annotations['annotations']:
        if annotation['image_id']==image_id:
            bbox=annotation['bbox']
            x,y,w,h = bbox
            # print(x,y,w,h)
            y_all.append(y)
            h_all.append(h)

    #print(max(y_all)-min(y_all))
    length = max(y_all)-min(y_all)
    y_min = int(min(y_all)-0.5*length)
    y_max = int(max(y_all)+0.5*length+max(h_all))
    cropped_image=image[y_min:y_max,0:int(shape[1])]
    height = y_max-y_min
    cv2.imwrite(os.path.join('../result/',image_file),cropped_image)
    print("saved")
    print("--------------")
    print("image id : ", image_id)
    print("ymax:",y_max)
    print("bbox height minus:" ,y_min)
    print("new image height:", height)
    return(image_id,(y_min,height))

with open('../annotations/instances_default.json','r') as f:
    annotations = json.load(f)
dict = {}
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image_id,diff = crop_img(file_name)
        dict[image_id]= diff

print(dict)
for key in dict.keys():
    for annotation in annotations['annotations']:
        if annotation['image_id']==key:
            annotation['bbox'][1]= annotation['bbox'][1]-dict[key][0]
    for annotation in annotations['images']:
        if annotation['id']==key:
            annotation['height']=dict[key][1]

with open('../annotations/instances_cropped.json','w') as f:
    json.dump(annotations,f,indent=4)


