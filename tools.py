import os
from PIL import Image
import ddddocr

ocr = ddddocr.DdddOcr()
    
def HandleVerify(Get_path): 
    Edit_path = 'Edit/'       #灰度图目录
    Edit_name = ''              #保存灰度图名称

    info_len = 0
    print('开始处理图片')
    threshold = 140
    table = [] 
    for i in range(256): 
        if i < threshold: 
            table.append(0) 
        else: 
            table.append(1) 

    Img_len = os.listdir(Get_path)
    print("获取图片总数，-》"+str(len(Img_len)))
    if os.path.isdir(Edit_path):
        pass
    else:
        mkdir = os.makedirs(Edit_path)
        # print('保存灰度图目录不存在，创建目录中----------')
        # print('保存灰度图目录创建成功，目录名->'+Edit_path)
    for i in range(0,len(Img_len)):
        edit_img_index = 0
        info_len+=1
        print("正在处理第"+str(i+1)+'张验证码')
        edit_img_name = edit_img_index+1
        img_name = str(i)+'.png'
        im = Image.open(Get_path+img_name)
        imgry = im.convert('L')
        out = imgry.point(table,'1') 
        Edit_name = Edit_path+str(edit_img_name)+'.png'    
        out.save(Edit_name) 



def ddddOCR(img_path):
    image = open(img_path, "rb").read()
    result = ocr.classification(image)
    return result


if __name__ == '__main__':
    img_path = 'img_data/'
    OCR_path = 'Edit/1.jpg'

    result = ddddOCR(img_path)
    print(result)