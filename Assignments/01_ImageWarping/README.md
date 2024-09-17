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

![Scale](pics\Scale=1.6.png)

![Rotation](pics\Rotation=60.png)

![X](pics\X=300.png)

![Y](pics\Y=-300.png)

![flip](pics\flip.png)

![Composition](pics\Composition.png)



### Point Guided Deformation(RBF):

![1](pics\1.png)

![2](pics\2.png)

![3](pics\3.png)

![4](pics\4.png)

![5](pics\5.png)

![6](pics\6.png)

[paper.dvi (utah.edu)](https://www.sci.utah.edu/~gerig/CS6640-F2010/Project3/Arad-1995.pdf)

## Acknowledgement

> 📋 Thanks for the algorithms proposed by [Image Warping by Radial Basis Functions](https://www.sci.utah.edu/~gerig/CS6640-F2010/Project3/Arad-1995.pdf)
