from abc import ABC, abstractmethod

class IObserver(ABC):
    def actualizar(self, message):
        pass
      

class ISubject(ABC):
    @abstractmethod
    def suscribir(self, observer: IObserver):
        pass
    
    @abstractmethod
    def desuscribir(self, observer: IObserver):
        pass
    
    @abstractmethod
    def notificar(self, message):
        pass