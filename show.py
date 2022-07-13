# -*- coding:utf-8 -*-
import cv2
'''
函数描述：对给定的图片和坐标信息在图片上标框，并在框的上方标注出该框的名称
函数参数：img_file_path=图片的绝对路径，new_img_file_path=保存后的绝对路径，points=[(str,[b0,b1,b2,b3])]
返回值：无返回值
注意事项：坐标[b0,b1,b2,b3]依次为左上角和右下角的坐标
'''

def draw_rectangle_by_point(img_file_path,new_img_file_path,points):
    image = cv2.imread(img_file_path)
    for item in points:
        print("当前字符：",item)
        point=item[1]
        first_point=(int(point[0]),int(point[1]))
        last_point=(int(point[2]),int(point[3]))

        print("左上角：",first_point)
        print("右下角：",last_point)
        cv2.rectangle(image, first_point, last_point, (0, 0, 255), 5)#在图片上进行绘制框
        cv2.putText(image, item[0], first_point, cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(255,0,0), thickness=2)#在矩形框上方绘制该框的名称

    cv2.imwrite(new_img_file_path, image)

if __name__ == '__main__':
    points=[('reportResult', [434,594,796,789]),
            ('reportName', [893,1211, 1195,1311]),
            ('reportOrg', [324,1842, 1180,2060]),
            ('reportTime', [684,1705, 1168,1797]),
            ('reportID,', [322,1383, 1190,1475])
            ]


    draw_rectangle_by_point(r'./image/736b41869e64ec44bc0ede3de45599c_20220506020910_339.jpg',"./image/new.jpg",points)
