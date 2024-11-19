# Assignment 3 - Play with GANs

### In this assignment, you will implement two methods for using GANs in digital image processing.

数字图像处理第三次作业：

1. 将GAN模型融入到上次的Pix2pix任务里
2. 融合dragGAN和自动脸部特征点提取

### Resources:
- [DragGAN](https://vcai.mpi-inf.mpg.de/projects/DragGAN/): [Implementaion 1](https://github.com/XingangPan/DragGAN) & [Implementaion 2](https://github.com/OpenGVLab/DragGAN)
- [Facial Landmarks Detection](https://github.com/1adrianb/face-alignment)

---

### Requirements:

To install requirements:

```cmd
pip install -r requirements.txt
```

还需要根据电脑配置自行安装`pytorch`

## Running

第一个任务，运行:

```cmd
python train.py
```

第一个任务，运行:

```cmd

```



## Results

### 任务一：

将标记图作为特征真实图片作为标签：
训练集：

<img src="Pix2Pix\train_results1\epoch_795\result_1.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results1\epoch_795\result_2.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results1\epoch_795\result_3.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results1\epoch_795\result_4.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results1\epoch_795\result_5.png" alt="alt text" width="800">

测试集：

<img src="Pix2Pix\val_results1\epoch_795\result_1.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results1\epoch_795\result_2.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results1\epoch_795\result_3.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results1\epoch_795\result_4.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results1\epoch_795\result_5.png" alt="alt text" width="800">

将真实图片作为特征标记图作为标签：
训练集：

<img src="Pix2Pix\train_results2\epoch_795\result_1.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results2\epoch_795\result_2.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results2\epoch_795\result_3.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results2\epoch_795\result_4.png" alt="alt text" width="800">

<img src="Pix2Pix\train_results2\epoch_795\result_5.png" alt="alt text" width="800">

测试集：

<img src="Pix2Pix\val_results2\epoch_795\result_1.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results2\epoch_795\result_2.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results2\epoch_795\result_3.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results2\epoch_795\result_4.png" alt="alt text" width="800">

<img src="Pix2Pix\val_results2\epoch_795\result_5.png" alt="alt text" width="800">

推测模型对测试集数据过拟合了。
