import cv2
import json
cv2.rectangle()
with open('../annotations/instances_default.json','r') as f:
    annotations = json.load(f)
image_file = '00a1d04bc0dd4529e26d5be87a1f0cff.jpg'
image  = cv2.imread(image_file)
print(annotations)
for image_name in annotations['images']:
    print(image_name)
    if image_name['file_name']==image_name:
        image_id = image_name['id']
        print(image_id)
        break

for annotation in annotations['annotations']:
    if annotation['image_id']==image_id:
        bbox=annotation['bbox']
        break

x,y,w,h = bbox
print(x,y,w,h)
# cv2.rectangle(image(x,y),(x+w,y+h),(0,255,0),2)
# cropped_image=image[y:y+h,x:x+w]

# cv2.imshow('Cropped_image',cropped_image)
# cv2.waitKey(0)
# cv2.destroyWindow()