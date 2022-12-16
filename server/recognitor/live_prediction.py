"""
This file can be used to try a live prediction.
"""

from tensorflow import keras
import numpy as np
import librosa


class LivePredictions:
    """
    Main class of the application.
    """

    def __init__(self, path, file):
        """
        Init method is used to initialize the main parameters.
        """
        self.loaded_model = None
        self.path = path
        self.file = file

    def load_model(self):
        """
        Method to load the chosen model.
        :param path: path to your h5 model.
        :return: summary of the model with the .summary() function.
        """
        self.loaded_model = keras.models.load_model(self.path)
        return self.loaded_model.summary()

    def make_predictions(self):
        """
        Method to process the files and create your features.
        """
        data, sampling_rate = librosa.load(self.file)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=1)
        x = np.expand_dims(x, axis=0)
        predict_x = self.loaded_model.predict(x)
        classes_x = np.argmax(predict_x, axis=1)
        print("Prediction is", " ", self.convertclasstoemotion(classes_x))
        return self.convertclasstoemotion(classes_x)

    @staticmethod
    def convertclasstoemotion(pred):
        """
        Method to convert the predictions (int) into human readable strings.
        """

        label_conversion = {'0': 'neutral',
                            '1': 'calm',
                            '2': 'happy',
                            '3': 'sad',
                            '4': 'angry',
                            '5': 'fearful',
                            '6': 'disgust',
                            '7': 'surprised'}

        for key, value in label_conversion.items():
            if int(key) == pred:
                label = value
        return label


# Here you can replace path and file with the path of your model and of the file
# from the RAVDESS dataset you want to use for the prediction,
# Below, I have used a neutral file: the prediction made is neutral.

# pred = LivePredictions(path='../SER_model.h5', file='03-01-01-01-01-02-05.wav')
#
# pred.load_model()
# pred.make_predictions()
