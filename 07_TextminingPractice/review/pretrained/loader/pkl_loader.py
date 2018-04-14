import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class Vectorizer:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self._vectorizer = pickle.load(open(os.path.join('pretrained', 'vectorizer.pkl'), 'rb'))

    def get_vector(self, text):
        return self._vectorizer.transform([text])


class Classifier:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self._classifier = pickle.load(open(os.path.join('pretrained', 'classification_model.pkl'), 'rb'))

    def get_prediction(self, input_features):
        prediction = self._classifier.predict(input_features)
        return self.prediction_parser(prediction)

    def prediction_parser(self, ndarray):
        if ndarray[0] == '1':
            return "이 영화를 좋아합니다."
        else:
            return "이 영화를 싫어합니다."