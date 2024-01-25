import cv2
import os

path = 'C:/Users/55819/Desktop/projetos da Byjus/PROJETO105/PRO_1-1_C105_ImagensProjeto-main'

Images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+'/'+file    
        print(file_name)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
frame.shape

width,height,channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWritter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    cv2.imread()
    out.write()
    print('concluido')


#vc parou na instrucao 11 do projeto