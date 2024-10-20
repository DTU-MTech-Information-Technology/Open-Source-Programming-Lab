from itertools import combinations

num_list = [0, -1, 2, -3, 1]

unique_triplets = set()
for triplet in combinations(num_list, 3):
    if sum(triplet) == 0:
        unique_triplets.add(triplet)

for triplet in unique_triplets:
    print(triplet)