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

步骤：

1.将标注数据集的标签（xml文件）放入Annotations，图片放入images;

2.修改voc_to_coco.py的输入输出路径，并运行，然后手动分开训练集和测试集;

3.修改get_train_list.py 的输入输出路径，并运行。训练集运行一次，测试集运行一次。



**四. 修改模型配置文件**

修改模型配置文件 config/det_DB_resnet50_mul.yaml,比如修改数据集文件路径



**五. 开启训练**

修改det_train.py 的模型配置文件路径，并运行



***\*六. 测试\****

修改det_infer.py的模型路径、模型文件路径、和图片路径



## 参考

https://github.com/BADBADBADBOY/pytorchOCR





机器学习，深度学习算法学习，计算机视觉cv，自然语言处理NLP，人工智能AI资源分享，案例源码分享

关注微信公众号 ： 机器学习算法AI大数据技术

##### 公众号ID：datanlp

扫下方二维码关注公众号