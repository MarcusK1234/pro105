import os
import cv2

path='C:/Users/marcu/OneDrive/Desktop/Projects/pro105/Images'

images = []

for file in os.listdir(path):
    name , ext = os.path.splitext(file)
    print(ext)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        fileName = path + '/' + file
        print(fileName)
        images.append(fileName)


count=len(images)
print(count)
frame = cv2.imread(images[0])

height,width = frame.shape
#what does line 21 do
size = ( width , height )
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8 , size)

for i in range(0, count-1):
    cv2.imread(images[i])
    out.write(frame)
out.release()
