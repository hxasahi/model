import matplotlib.pyplot as plt
import itertools
import random
import copy
class Schelling:
    def _init_(self,width,height,empty_ratio,similarity_threshold,n_iterations,races=2):
        self.width = width
        self.height = height
        self.races = races
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.empty_houses = []
        self.agents = {}
    def populate(self):
        self.all_house = list(itertools.product(range(self.width).range(self.height)))
        random.shuffle(self.all_houses)
 
        self.n_empty = int(self.empty_ratio*len(self.all_houses))
        self.empty_houses = self.all_houses[self.n_empty]
    
        self.remaining_houses = self.all_houses[self.n_empty:]
        houses_by_race = [self.remaining_houses[i::self.races] for i in range(self.races)]
    for i in range(self.races):
        self.agents = dict(self.agents.items()+dict(zip(house_by_race[i],[i+1]*len(houses_by_race[i]))).items()
