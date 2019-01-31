from enum import Enum

import numpy as np
from scipy.spatial import distance

from .BaseModel import BaseModel
from Utils import  *

class KnnAvailableMetrics(Enum):
    Euclidean = 1,
    Mahalanobis = 2,
    Cosine = 3
    Custom = 4


class KNeighborsClassifier(BaseModel):
    def __init__(self, n_neighbors, metric=KnnAvailableMetrics.Euclidean, custom=None):
        if not is_positive_int(n_neighbors):
            raise ValueError("n_neighbors must be a positive integer")
        self.n_neighbors = n_neighbors
        self.data = None
        self.target = None
        self.metric = KNeighborsClassifier._get_metrics_function(metric, custom)

    def fit(self, train_x, train_y):
        if self.data is None:
            self.data = train_x
            self.target = train_y
        else:
            self.data = np.concatenate((self.data, train_x))
            self.target = np.concatenate((self.target, train_y))


    def predict(self, test_x):
        if self.data is None:
            raise RuntimeError("The model has not been trained!")
        return np.apply_along_axis(self.calculate_distances,test_x)

    @staticmethod
    def _get_metrics_function(metric, custom=None):
        """ This function creates the metric function object parsing input enum
        """
        if not isinstance(metric, KnnAvailableMetrics):
            raise ValueError("Metric must be type of KnnAvailableMetrics")
        if metric == KnnAvailableMetrics.Custom and custom is None:
            raise ValueError("Please specify the custom metrics")
        metric_dict = {KnnAvailableMetrics.Euclidean: distance.euclidean,
                       KnnAvailableMetrics.Mahalanobis: distance.mahalanobis,
                       KnnAvailableMetrics.Cosine: distance.cosine,
                       KnnAvailableMetrics.Custom: custom
                       }
        return metric_dict[metric]

    def calculate_distances(self, event):
        return self.metric(self.data, event)

