import cv2
import numpy as np
import gradio as gr

# 初始化全局变量，存储控制点和目标点
points_src = []
points_dst = []
image = None


# 上传图像时清空控制点和目标点
def upload_image(img):
    global image, points_src, points_dst
    points_src.clear()  # 清空控制点
    points_dst.clear()  # 清空目标点
    image = img
    return img


# 记录点击点事件，并标记点在图像上，同时在成对的点间画箭头
def record_points(evt: gr.SelectData):
    global points_src, points_dst, image
    x, y = evt.index[0], evt.index[1]  # 获取点击的坐标

    # 判断奇偶次来分别记录控制点和目标点
    if len(points_src) == len(points_dst):
        points_src.append([x, y])  # 奇数次点击为控制点
    else:
        points_dst.append([x, y])  # 偶数次点击为目标点

    # 在图像上标记点（蓝色：控制点，红色：目标点），并画箭头
    marked_image = image.copy()
    for pt in points_src:
        cv2.circle(marked_image, tuple(pt), 1, (255, 0, 0), -1)  # 蓝色表示控制点
    for pt in points_dst:
        cv2.circle(marked_image, tuple(pt), 1, (0, 0, 255), -1)  # 红色表示目标点

    # 画出箭头，表示从控制点到目标点的映射
    for i in range(min(len(points_src), len(points_dst))):
        cv2.arrowedLine(marked_image, tuple(points_src[i]), tuple(points_dst[i]), (0, 255, 0), 1)  # 绿色箭头表示映射

    return marked_image


# 执行仿射变换

def point_guided_deformation(image, source_pts, target_pts, alpha=1.0, eps=1e-8, im2=None):
    if source_pts.shape[0] == 0:
        return image
    d = 1000
    mu = -1
    h = image.shape[0]
    w = image.shape[1]
    source_pts = np.flip(source_pts, axis=1)
    target_pts = np.flip(target_pts, axis=1)
    src_x, src_y = source_pts[:, :1], source_pts[:, 1:2]
    tgt_x, tgt_y = target_pts[:, :1], target_pts[:, 1:2]
    b = np.power((np.square(src_x - src_x.T) + np.square(src_y - src_y.T) + d).astype(np.float32), mu)
    a = np.linalg.solve(b, target_pts - source_pts)

    ypix, xpix = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    x = np.hstack((xpix.reshape(-1, 1, order='F'), ypix.reshape(-1, 1, order='F'))).astype(np.float32)
    b = np.power((np.square(x[:, :1] - src_x.T) + np.square(x[:, 1:2] - src_y.T) + d).astype(np.float32), mu)
    a = a.T
    x[:, 0] += np.sum(b * a[0, :], axis=1)
    x[:, 1] += np.sum(b * a[1, :], axis=1)
    x = np.ceil(x).astype(np.int32)
    flag = (0 <= x[:, 0]) & (x[:, 0] < image.shape[0]) & (0 <= x[:, 1]) & (x[:, 1] < image.shape[1])
    ind = np.ravel_multi_index((x[flag, 0], x[flag, 1]), (h, w), order='F')
    image = image.reshape(h * w, 3, order='F')
    im2 = -1 * np.ones_like(image)
    im2[ind, :] = image[flag, :]
    im2 = im2.reshape(h, w, 3, order='F')

    # 补缝
    index = im2[:, :, 0] == -1
    index = index.flatten(order='F')
    im3 = im2[:, :, 0].copy()
    im3[im3 != -1] = 1
    im3[im3 == -1] = 0

    I0 = np.zeros((im2.shape[0], im2.shape[1], im2.shape[2], 8))
    I0[:-1, :, :, 0] = im2[1:, :, :]
    I0[1:, :, :, 1] = im2[:-1, :, :]
    I0[:, :-1, :, 2] = im2[:, 1:, :]
    I0[:, 1:, :, 3] = im2[:, :-1, :]
    I0[:-1, :-1, :, 4] = im2[1:, 1:, :]
    I0[1:, 1:, :, 5] = im2[:-1, :-1, :]
    I0[:-1, 1:, :, 6] = im2[1:, :-1, :]
    I0[1:, :-1, :, 7] = im2[:-1, 1:, :]

    I1 = np.zeros((im2.shape[0], im2.shape[1], 8))
    I1[:-1, :, 0] = im3[1:, :]
    I1[1:, :, 1] = im3[:-1, :]
    I1[:, :-1, 2] = im3[:, 1:]
    I1[:, 1:, 3] = im3[:, :-1]
    I1[:-1, :-1, 4] = im3[1:, 1:]
    I1[1:, 1:, 5] = im3[:-1, :-1]
    I1[:-1, 1:, 6] = im3[1:, :-1]
    I1[1:, :-1, 7] = im3[:-1, 1:]

    a = np.sum(I0, axis=3) / np.sum(I1, axis=2).reshape(I1.shape[0], I1.shape[1], 1)

    im2 = im2.reshape(h * w, 3, order='F')
    a = a.reshape(h * w, 3, order='F')
    im2[index, :] = a[index, :]
    im2 = im2.reshape(h, w, 3, order='F')

    im2[im2 < 0] = 0
    warped_image = im2

    ### FILL: 基于MLS or RBF 实现 image warping

    return warped_image


def run_warping():
    global points_src, points_dst, image  ### fetch global variables

    warped_image = point_guided_deformation(image, np.array(points_src), np.array(points_dst))

    return warped_image


# 清除选中点
def clear_points():
    global points_src, points_dst
    points_src.clear()
    points_dst.clear()
    return image  # 返回未标记的原图


# 使用 Gradio 构建界面
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(source="upload", label="上传图片", interactive=True, width=800, height=200)
            point_select = gr.Image(label="点击选择控制点和目标点", interactive=True, width=800, height=800)

        with gr.Column():
            result_image = gr.Image(label="变换结果", width=800, height=400)

    # 按钮
    run_button = gr.Button("Run Warping")
    clear_button = gr.Button("Clear Points")  # 添加清除按钮

    # 上传图像的交互
    input_image.upload(upload_image, input_image, point_select)
    # 选择点的交互，点选后刷新图像
    point_select.select(record_points, None, point_select)
    # 点击运行 warping 按钮，计算并显示变换后的图像
    run_button.click(run_warping, None, result_image)
    # 点击清除按钮，清空所有已选择的点
    clear_button.click(clear_points, None, point_select)

# 启动 Gradio 应用
demo.launch()
