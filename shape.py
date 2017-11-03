from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass
