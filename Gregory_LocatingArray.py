#Locating Array Verifier

import random
import itertools
from Gregory_CoveringArray import verify_covering_array

d = 1
t = 3
k = 5
v = 3
N = random.randint(1,100)

#all interactions
all_cols = itertools.combinations(range(k), t)
#print(list(all_cols))
all_vals = itertools.product(range(v), repeat = t)
#print(list(all_vals))
interactions = itertools.product(all_cols, all_vals)
#print(list(interactions))
d_col = itertools.combinations(interactions, d)
#print(list(d_col))

def rows_of(interaction):
    combos = set()
    for row in interaction:
        comp = tuple(row[col] for col in interaction)
        combos.add(comp)

def locating_array_verifier(distinct_col, pair):
    verify = True
    for I1, I2 in itertools.combinations(distinct_col, pair):
        rows1 = rows_of(I1)
        rows2 = rows_of(I2)
        if rows1 == rows2:
            return False
    return verify

if locating_array_verifier(d_col, 2):
    verify_covering_array(d_col)
    if verify_covering_array:
        print(f'This is a locating array!')
    else:
        print(f'This is not a locating array.')
else:
    print(f'This is not a locating array.')




# t = 3
# k = 3
# v = 3
# N = random.randint(1,100)

# interaction = []
# la_c = []
# la_v = []
# for row in range(N):
#     la_combos = itertools.combinations(range(k), t)
#     la_c.append(la_combos)
#     #for combo in la_c:
#        #reduce = la_c.count(combo)
#        #while reduce > 1:
#           #la_c.remove(combo)
#           #reduce = reduce - 1
#     la_values = itertools.product(range(v), t)
#     la_v.append(la_values)
# la_c = set(la_c)
# interaction.append(la_c, la_v)

# #make the array's members unique
# Distinct = set(interaction)

# #distinct sets, containing pairs
# d_sets = []
# for pair in Distinct:
#    pair = itertools.combinations(Distinct, 2)
#    d_sets.append(pair)

# d_sets = set(d_sets)

# #verify the distinction of pairs
# verifier = []
# for pair in d_sets:
#    location = Distinct.find(pair)
#    verifier.append(location)
# for check in range(verifier):
#    if verifier.count(check) > 1:
#       f'This cannot be a locating array!'
#    else: 
#       continue

#add back in covering array verifier to then test the locating array for covering property


      


    







