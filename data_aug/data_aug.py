# Import libs for data aug
import random
import numpy as np
import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
# Import funcs for data reading
from main import get_input_data
from main import extract_bounding_boxes


def main():
    # Extract data info
    imgs = get_input_data()
    # Extract bounding boxes
    bboxes = []
    for file_name in os.listdir('../data/annotations'):
        bbox = extract_bounding_boxes('../data/annotations/' + file_name)
        bboxes.append(bbox)
        break
    img = np.array(imgs[0])
    img = np.reshape(img, (512, 512, 3))
    print(img)
    print(bboxes[0])
    #plt.imshow(img)
    #plt.show()
    img2 = cv2.imread('../data/images/frame0.jpg')
    cv2.imshow("Image", img2)
    cv2.show()

if __name__ == '__main__':
    main()