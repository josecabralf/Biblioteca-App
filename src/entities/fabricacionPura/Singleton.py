from abc import ABC

class Singleton(ABC):
  def __new__(cls, *args, **kwargs):
      if not hasattr(cls, '_instance'): cls._instance = super(Singleton, cls).__new__(cls)
      return cls._instance