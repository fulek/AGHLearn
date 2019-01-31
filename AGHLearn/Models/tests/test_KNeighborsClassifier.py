from unittest import TestCase
from Models.kNN import *

class TestKNeighborsClassifier(TestCase):
     def test_should_raise_exception_when_invali_constructor_parameters(self):
          string_n_neighbors = "aaa"
          self.assertRaises(ValueError, KNeighborsClassifier, string_n_neighbors)
          negative_n_neighbors = -2
          self.assertRaises(ValueError, KNeighborsClassifier, negative_n_neighbors)

          valid_n_neighbors = 3
          metric = "minkowski"
          self.assertRaises(ValueError, KNeighborsClassifier, negative_n_neighbors, metric)
          metric = "minkowski"
          self.assertRaises(ValueError, KNeighborsClassifier, negative_n_neighbors, metric)
          metric = KnnAvailableMetrics.Custom
          self.assertRaises(ValueError, KNeighborsClassifier, negative_n_neighbors, metric)

     def test_predict_should_raise_exception_when_not_trained(self):
         metric = KnnAvailableMetrics.Euclidean
         k = 1
         model = KNeighborsClassifier(k, metric)
         self.assertRaises(RuntimeError, model.predict, np.zeros((1,2)))
