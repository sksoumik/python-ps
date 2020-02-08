from time import time
import argparse
import pandas as pd
import matplotlib
import tensorflow as tf


class CeriTrain():
    def __init__(self, parser):
        self.parser = parser

    def train(self):
        train_path = self.parser.input_directory
        if self.parser.validation:
            datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=self.rotation_range,
                featurewise_std_normalization=self.parser.
                featurewise_std_normalization,
                validation_split=self.parser.validation_split)
        else:
            datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=self.parser.rotation_range,
                featurewise_std_normalization=self.parser.
                featurewise_std_normalization,
                validation_split=0.0)

        if self.parser.mode == "classifier":
            train_data = datagen.flow_from_directory(
                directory=train_path,
                target_size=(224, 224),
                subset='training',
                shuffle=True,
                batch_size=self.parser.batch_size)
            if self.parser.validation:
                validation_data = datagen.flow_from_directory(
                    directory=train_path,
                    target_size=(224, 224),
                    subset='validation',
                    shuffle=True,
                    batch_size=self.parser.batch_size)
        else:
            df = pd.read_csv('./data/regression_data.csv')
            train_data = datagen.flow_from_dataframe(
                dataframe=df,
                directory=train_path,
                x_col="path",
                class_mode='raw',
                y_col='r-label',
                target_size=(224, 224),
                subset='training',
                shuffle=True,
                batch_size=self.parser.batch_size)
            if self.parser.validation:
                validation_data = datagen.flow_from_dataframe(
                    dataframe=df,
                    directory=train_path,
                    x_col="path",
                    subset='validation',
                    shuffle=True,
                    batch_size=self.parser.batch_size)

        base_mode = self.load_model()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gghg')
    parser.add_argument('-back', '--backbone', default='resnet50')
    parser.add_argument('-fsn',
                        '--featurewise_std_normalization',
                        default=False)
    parser.add_argument('-v', '--validation', default=True)
    parser.add_argument('-vs', '--validation_split', default=.20)
    parser.add_argument(
        '-dir',
        '--input_directory',
        default='./CERI_snow/01_grading_by_means_between_10sec')
    parser.add_argument('-rot', '--rotation_range', default=4)
    parser.add_argument('-e', '--epoch', default=5)
    parser.add_argument('-batch', '--batch_size', default=4)
    parser.add_argument('-m', '--mode', default="classifier")
    args = parser.parse_args()

    ceri = CeriTrain(args)
    ceri.train()
