import abc


class BuilderAbc(metaclass=abc.ABCMeta):
    def __init__(self):
        self.full_file_contents = ''

    @abc.abstractmethod
    def build_header(self):
        pass

    @abc.abstractmethod
    def build_body(self):
        pass

    @abc.abstractmethod
    def build_footer(self):
        pass
