# Image Warping

数字图像处理第一次作业：基于基本图像几何变换以及基于控制点来实现图像变形。

## Requirements

To install requirements:

```cmd
pip install -r requirements.txt
```

## Running

To run basic transformation, run:

```cmd
python run_global_transform.py
```

To run point guided transformation, run:

```cmd
python run_point_transform.py
```

## Results

### Basic Transformation

<img src="pics/Scale=1.6.png" alt="alt text" width="800">

<img src="pics/Rotation=60.png" alt="alt text" width="800">

<img src="pics/X=300.png" alt="alt text" width="800">

<img src="pics/Y=-300.png" alt="alt text" width="800">

<img src="pics/flip.png" alt="alt text" width="800">

<img src="pics/Composition.png" alt="alt text" width="800">



### Point Guided Deformation(RBF):

<img src="pics/1.png" alt="alt text" width="800">

<img src="pics/2.png" alt="alt text" width="800">

<img src="pics/3.png" alt="alt text" width="800">

<img src="pics/4.png" alt="alt text" width="800">

<img src="pics/5.png" alt="alt text" width="800">

<img src="pics/6.png" alt="alt text" width="800">


## Acknowledgement

> 📋 Thanks for the algorithms proposed by [Image Warping by Radial Basis Functions](https://www.sci.utah.edu/~gerig/CS6640-F2010/Project3/Arad-1995.pdf)
