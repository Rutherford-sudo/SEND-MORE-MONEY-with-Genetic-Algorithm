from __future__ import annotations
from typing import TypeVar, Tuple, Type
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Chromosome') #devolver a si mesmo

#classe base para todos os cromossomos
class Chromosome(ABC):

    @abstractmethod
    def fitness(self):
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls):
        ...
    
    @abstractmethod
    def crossover(self, other):
        ...

    @abstractmethod
    def mutate(self):
        ...
