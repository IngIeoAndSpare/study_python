import cv2
import numpy as np
import matplotlib.pyplot as plt

## arg 얻어오기
import sys, getopt

## open file dialog
import tkinter as tk
from tkinter import filedialog

def getFilePath():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("image files", "*.jpg")
            #("image files", "*.png"),
            #("image files", "*.bmp")
        ]
    )

    if not file_path:
        print("image file은 필수적으로 선택되어야 합니다.")
        sys.exit(2)

    return file_path

def preperParamsData(argv):
    FILE_NAME = argv[0]

    ## 이미지 source path
    FILE_PATH = getFilePath()
    ## 클러스터 갯수
    CLASSES_COUNT = ""

    try:
        opts, etc_args = getopt.getopt(argv[1:],
                                       'c', ["class="])

    except getopt.GetoptError:
        print(FILE_NAME, 'class 옵션이 있어야 합니다. -c{{CLASS_NUM}}')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-c", "--class"):
            CLASSES_COUNT = arg

    if len(FILE_PATH) < 0:
        print(FILE_NAME, "--class 옵션은 필수적으로 들어가야 합니다.")
        sys.exit(2)

    return FILE_PATH, int(CLASSES_COUNT)

def imageClassify(file_path, class_count):
    ori_image = cv2.imread(file_path, cv2.IMREAD_COLOR).astype(np.float32) / 255
    image_lab = cv2.cvtColor(ori_image, cv2.COLOR_BGR2Lab)

    vector_data = image_lab.reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.1)
    _, labels, centers = cv2.kmeans(vector_data, class_count, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    segmented_lab = centers[labels.flatten()].reshape(ori_image.shape)
    segmented_image = cv2.cvtColor(segmented_lab, cv2.COLOR_Lab2RGB)

    return ori_image, segmented_image

def showImage(image, title):
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    file_path, class_count = preperParamsData(sys.argv)
    ori_image, segmented_image = imageClassify(file_path, class_count)

   # showImage(ori_image[:,:,[2,1,0]])
    showImage(segmented_image, 'segmented')