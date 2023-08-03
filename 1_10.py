import itertools
from itertools import combinations, permutations
import random

numbers = list(range(1,11))
genders = ['male','female']

all_combinations = list(itertools.product(numbers, genders))

random.shuffle(all_combinations)

for combination in all_combinations:
    print(combination)