from keras import Sequential
from keras.layers import Dense, Activation
from xml.etree import ElementTree
from os import listdir
from PIL import Image
import numpy


def main():
    # FIXME:- 512x512 for project
    image_width = 100
    image_height = 100

    # dummy model
    model = Sequential()

    # input layer
    model.add(Dense(image_width * image_height * 3))
    model.add(Activation('relu'))

    # hidden layer
    model.add(Dense(100))
    model.add(Activation('sigmoid'))

    # FIXME: - what kind of output for neural net so it can handle outputing
    # multiple bounding boxes?

    # output layer
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # get data from images
    input_data = get_input_data()
    print(input_data)
    print(len(input_data[0]))

    # single test feed forward
    single_input = numpy.asarray([input_data[0]])
    print(model.predict(single_input))

    # can evaulate multiple forward passes at once
    # multiple_input = numpy.asarray([input_data[0], input_data[1], input_data[2]])
    # print(model.predict(multiple_input))

    # # extract a list of bounding boxes from annotation file
    # boxes = extract_bounding_boxes('data/annotations/00001.xml')
    # print(boxes)


# returns an array where each element is a 1-D list of
# all pixel values in a photo
def get_input_data():
    images_dir = 'data/images/'

    input_data = []
    for filename in listdir(images_dir):
        file_path = images_dir + filename
        im = Image.open(file_path, 'r')

        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        input_data.append(pix_val_flat)

    return input_data


# function to extract bounding boxes from an annotation file
def extract_bounding_boxes(filename):
    # load and parse the file
    tree = ElementTree.parse(filename)
    # get the root of the document
    root = tree.getroot()
    # extract each bounding box
    boxes = list()
    for box in root.findall('.//bndbox'):
        xmin = int(box.find('xmin').text)
        ymin = int(box.find('ymin').text)
        xmax = int(box.find('xmax').text)
        ymax = int(box.find('ymax').text)
        coors = [xmin, ymin, xmax, ymax]
        boxes.append(coors)
    return boxes


if __name__ == '__main__':
    main()

