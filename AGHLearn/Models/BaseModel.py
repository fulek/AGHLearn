import abc


class BaseModel(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fit(self, train_x, train_y):
        pass

    @abc.abstractmethod
    def predict(self, test_x):
        pass