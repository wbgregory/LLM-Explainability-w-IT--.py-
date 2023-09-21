#Locating Array Verifier

LAs require that every d-size collection of interactions be in separate rows than any other d-size 
collection of interactions.
For example, if C1 = {I1, I2} is a collection of 2 interactions and C2 = {I3, I4} (and it could be that 
I1 = I3 or something), then look at the rows where I1 appears and the rows where I2 appears, and put them
 all together.
Suppose that they are rows_of(I1) = {1, 3, 4, 7} and rows_of(I2) = {2, 4, 5, 7, 9}. Then rows_of(I1, I2)
= {1, 2, 3, 4, 5, 7, 9}; notice duplicates are removed.
Then if rows_of(I3, I4) = {1, 2, 3, 4, 5, 6, 9}, then the pairs (I1, I2) and (I3, I4) are locating as 
the two sets are different; the one for (I1, I2) includes a 7 and the one for (I3, I4) does not.
 
Think about how to choose a collection of size d (where there are no repeats) from the collection of all
interactions.
First, generate the collection of all interactions; remember that an interaction involves a t-set of 
columns (no repeats) and a t-set of values (can have repeats). Let I be the collection of all 
interactions.
Second, generate all d-sets of interactions from I (no repeats); call this big collection D.
Third, generate all pairs of d-sets from D (no repeats).
Fourth, determine the rows each pair appears in, and determine if these sets of rows are different. 
If not, it is not a locating array and so you can return False.
Fifth, once you verify that all pairs are locating, determine if the array is a covering array 
(as a locating array must have the coverage property too). If so, return True (as both the locating and 
covering properties passed); otherwise, return False.

import random
import itertools

t = 3
k = 3
v = 3
N = random.randint(1,100)

interaction = []
la_c = []
la_v = []
for row in range(N):
    la_combos = itertools.combinations(range(k), t)
    la_c.append(la_combos)
    #for combo in la_c:
       #reduce = la_c.count(combo)
       #while reduce > 1:
          #la_c.remove(combo)
          #reduce = reduce - 1
    la_values = itertools.product(range(v), t)
    la_v.append(la_values)
la_c = set(la_c)
interaction.append(la_c, la_v)

#make the array's members unique
Distinct = set(interaction)

#distinct sets, containing pairs
d_sets = []
for pair in Distinct:
   pair = itertools.combinations(Distinct, 2)
   d_sets.append(pair)

d_sets = set(d_sets)

#verify the distinction of pairs
verifier = []
for pair in d_sets:
   location = Distinct.find(pair)
   verifier.append(location)
for check in range(verifier):
   if verifier.count(check) > 1:
      f'This cannot be a locating array!'
   else: 
      continue

#add back in covering array verifier to then test the locating array for covering property
def verify_covering_array(ca):
    verify = True
    combos = []
    for columns in itertools.combinations(range(k), t):
        for values in itertools.product(range(v), repeat = t):
            assign_name = list(k[col] for col in columns)
            assign_value = list(v[val] for val in values)
            combos.append(assign_name, assign_value)
            #vals.append(values)
            for row in ca:
                if row in combos:
                    continue
                else:
                    verify = False
    return verify

if verify_covering_array(Distinct):
    f'Yay, a covering array!'
else: 
    f'There is an imposter among us!'


      


    







