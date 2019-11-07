# Importing all necessary libraries 
import os
import sys

import cv2


# Read the video from specified path
def vids_to_imgs(video: str, data: str, interval: int):
    cam = cv2.VideoCapture(video)

    try:

        # creating a folder named data
        if not os.path.exists(data):
            os.makedirs(data)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0
    i = 0
    while True:
        # reading from frame
        ret, frame = cam.read()

        # skip certain frames
        i = (i + 1) % interval
        if i:
            continue

        if ret:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    interval = 1 if len(sys.argv) < 4 else int(sys.argv[3])
    if len(sys.argv) >= 3:
        vids_to_imgs(sys.argv[1], sys.argv[2], interval)
    else:
        print(f"usage: /path/to/video, /path/to/hold/data, interval")
