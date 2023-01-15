from abc import abstractmethod


class BaseDataLoader:
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def get_headers(self):
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError
