import shutil

import cv2
import matplotlib.pyplot as plt


def threshold_demo(image):
    # 全局阈值
    ret, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)      # 大津算法，适用于两个波峰
    # ret, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)     # 三角形算法，适用于单个波峰，最开始用于医学分割细胞
    # ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    # ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    # ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)

    # 局部阈值
    # binary = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 4)     # 均值
    # binary = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 4)     #高斯

    # print('threshold value:', ret)
    # cv2.imshow('pic', binary)

    # plt.subplot(1, 2, 1)
    # plt.imshow(binary, cmap='Greys_r')
    # res = cv2.blur(binary, (3, 3))
    # plt.subplot(1, 2, 2)
    # plt.imshow(res, cmap='Greys_r')

    cv2.imshow('pic', binary)
    cv2.waitKey(0)
    plt.show()


if __name__ == '__main__':
    image = cv2.imread("../images/cell.jpg", cv2.IMREAD_GRAYSCALE)

    threshold_demo(image)

    im2 = image.flatten()
    plt.figure()
    plt.hist(im2)
    plt.show()
    #
    # cv2.imshow('pic', image)
    # cv2.waitKey(0)