# Packages
import copy
import random
from collections import Counter

class Hat:

    def __init__(self, **args):
        self.contents = []
        for i in args.keys():
            for x in range(0, args.get(i)):
                self.contents.append(str(i))

    def draw(self, amount):
        pulled_balls = []
        
        if amount > len(self.contents):
            return self.contents           
        else:
            for i in range(0, amount):
                len_contents = len(self.contents)
                random_number = random.randint(0, len_contents -1) 
                pulled_balls.append(self.contents[random_number])
                self.contents.remove(self.contents[random_number])
        return pulled_balls
            
def experiment(hat, expected_balls, num_balls_drawn,num_experiments):
    m, n = 0, 0
    experiments = num_experiments
    
    for e in range(experiments):
        hatcopy = copy.deepcopy(hat)
        taken_balls = hatcopy.draw(num_balls_drawn)
        extracted = Counter(taken_balls) 
        contains_all = True

        for i,x in expected_balls.items():
            if i not in extracted.keys() or extracted.get(i) < expected_balls.get(i):
                contains_all = False
                break
                
        if contains_all != False:
                m += 1
            
        n += 1
    final_result = m/n
    print("Probability: ", final_result)
    return final_result
    