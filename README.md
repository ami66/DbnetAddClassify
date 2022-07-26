# DbnetAddClassify
dbnet文字检测，添加文本框分类



**1.标注数据**



标注方法和标注目标检测的数据一样，一个框加一个标签

 pip install labelImg ==1.8.6

安装完毕后，键入命令：

> labelImg



或者下载工具  labelImg.exe链接：https://pan.baidu.com/s/14iBlyr3ahhymMukeWjtTEA 提取码：c1dx






**二 . 数据增强**



步骤：

1.将标注数据集的标签（xml文件）放入./DataAugForObjectDetection/data/Annotations

2.将标注数据集的图片放入./DataAugForObjectDetection/data/images

3.修改./DataAugForObjectDetection/DataAugmentForObejctDetection.py/中的need_aug_num，即每张图片需要扩增的数量，然后运行./DataAugForObjectDetection/DataAugmentForObejctDetection.py



注意：DataAugmentForObejctDetection_pool.py 是多进程增强版本，耗时较少。代码中的process不宜设置过大否则可能会报错，默认即可。






**三. 格式转换**



将标注的数据集转换成 dbnet 训练需要用到的格式。
例如：
一张图片 1.jpg 对应有一个标签格式转化好的同名txt文件
txt内容格式如下：

126,681,276,681,276,701,126,701,reportTime
93,159,185,159,185,185,93,185,reportName
214,48,645,48,645,84,214,84,reportOrg

英文逗号分隔，前面8位整数数值是左上角顶点开始顺时针，四个顶点的坐标值，即x1,y1,x2,y2,x3,y3,x4,y4
最后一位是类型名称。



步骤：

1.将标注数据集的标签（xml文件）放入Annotations，图片放入images;

2.修改voc_to_coco.py的输入输出路径，并运行，然后手动分开训练集和测试集;

3.修改get_train_list.py 的输入输出路径，并运行。训练集运行一次，测试集运行一次。



**四. 修改模型配置文件**

修改模型配置文件 config/det_DB_resnet50_mul.yaml,比如修改数据集文件路径





**五. 开启训练**

修改det_train.py 的模型配置文件路径，并运行





***\*六. 测试\****



身份证要素提取模型下地址获取方式：
关注公众号 datanlp 然后回复关键词 db分类 即可获取。



修改det_infer.py的模型路径、模型文件路径、和图片路径


dbnet不仅检测出文本行，还自动给文本行分类标签，一个框一个标签，可以按标签提取目标文本行。

![3](https://user-images.githubusercontent.com/24771833/178769560-c8db79fb-0c06-43c2-981b-77092e1b1026.jpg)

![7](https://user-images.githubusercontent.com/24771833/178769763-5c7b19c3-ef0e-4c87-a232-2f02f76a7d88.jpg)

![9](https://user-images.githubusercontent.com/24771833/178769838-f6e61135-90f6-4f61-a8f2-e062c2572da6.jpg)


## 参考

https://github.com/BADBADBADBOY/pytorchOCR





机器学习，深度学习算法学习，计算机视觉cv，自然语言处理NLP，人工智能AI资源分享，案例源码分享

关注微信公众号 ： 机器学习算法AI大数据技术

##### 公众号ID：datanlp

扫二维码关注公众号


![机器学习算法AI大数据技术_datanlp](https://user-images.githubusercontent.com/24771833/178769996-f7dd23e9-9997-4380-9a7f-3a0cd16e6fee.jpg)
