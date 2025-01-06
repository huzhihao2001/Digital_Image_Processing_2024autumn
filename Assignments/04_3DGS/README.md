# Assignment 4 - Implement Simplified 3D Gaussian Splatting

数字图像处理第四次作业：

1. 使用3D高斯从多视角图片进行重建。

## Requirements

需要在之前的环境上安装`colmap`和`pytorch3d`

## Running

```cmd
python mvs_with_colmap.py --data_dir data/chair
python debug_mvs_by_projecting_pts.py --data_dir data/chair
python train.py --colmap_dir data/chair --checkpoint_dir data/chair/checkpoints
```

## Results

### PyTorch-only

After 50 epochs:

<img src="data\chair\checkpoints4\debug_images\epoch_0050\r_11.png" alt="alt text" width="800">

After 100 epochs:

<img src="data\chair\checkpoints4\debug_images\epoch_0100\r_11.png" alt="alt text" width="800">

After 150 epochs:

<img src="data\chair\checkpoints4\debug_images\epoch_0150\r_11.png" alt="alt text" width="800">

After 199 epochs:

<img src="data\chair\checkpoints4\debug_images\epoch_0199\r_11.png" alt="alt text" width="800">

视频：



## Acknowledgements

- Thanks to the authors and contributors of [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) and [Colmap for SfM](https://colmap.github.io/index.html). 
