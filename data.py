from PIL import Image
from tensorflow import keras
from tensorflow.keras.models import load_model
import csv
from os import walk



def download_mnist():
        mnist = keras.datasets.mnist
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

        for i, image in enumerate(train_images):
                result = Image.fromarray(image)
                print(i)
                result.save('train/' + str(i) + '-' + str(train_labels[i]) + '.png')
        for i, image in enumerate(test_images):
                print(i)
                result = Image.fromarray(image)
                result.save('test/' + str(i) + '-' + str(test_labels[i]) + '.png')


def create_index():   
        with open('train.csv', 'w') as csvfile:
                w = csv.writer(csvfile, delimiter=';')
                for filenames in walk('train/')[2]:
                        for file in filenames:
                                file = file.replace('.png', '')
                                file = file.split('-')
                                w.writerow([file[0], file[1]])
                                


create_index()
#download_mnist()