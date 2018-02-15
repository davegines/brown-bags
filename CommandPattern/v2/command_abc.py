import abc


class CommandAbc(object):
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass
