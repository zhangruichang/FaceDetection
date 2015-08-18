__author__ = 'zhangruichang'
from PIL import Image
from collections import Counter
import os
import math
# 72 persons *20 jpgs, use first 15 images of each person for knn training, and remaining 5 images for testing

def get_sim(test_path, train_path):
    im_test = Image.open(test_path)
    im_train = Image.open(train_path)
    width, height = im_test.size[0], im_test.size[1]
    dis = 0
    for i in range(width):
        for j in range(height):
            for k in range(3):
                dis += math.pow(abs(im_test.getpixel((i, j))[k] - im_train.getpixel((i, j))[k]), 2)
    return dis


if __name__ == '__main__':
    path = 'E:/GithubRepo/KNNFaceDetection/faces95'
    k = 7
    file_list = os.listdir(path)
    cnt_dict = {}
    for classes in file_list:
        cnt_dict[classes] = 0
    for test_class in file_list:
        for test_image in range(16, 21):
            test_path = path + '/' + test_class + '/' + test_class + '.' + str(test_image) + '.jpg'
            print test_path
            test_sim_list = []
            cnt = {}
            for train_class in file_list:
                for train_image in range(1, 16):
                    train_path = path + '/' + train_class + '/' + train_class + '.' + str(train_image) + '.jpg'
                    print train_path
                    test_sim_list.append([get_sim(test_path, train_path), train_class])
            test_sim_list.sort()
            print test_sim_list
            for j in test_sim_list[0:k]:
                cnt_dict[j[1]] += 1
            print 'nearest person is person ' + Counter(cnt).most_common()[0][0]