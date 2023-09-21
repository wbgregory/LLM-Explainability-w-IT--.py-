#created below is a covering array, along with another variable that contains value sets - the covering array is compared to the value sets in order to verify the presence of the value sets within the
#covering array, to make sure that it is indeed a covering array.

#additional notes - t = strength, k = columns, v = values within a specific row x column, N = rows.
#.combinations generates column sets while .product generates value sets

import itertools
import random

t = 3
k = 3
v = 3
N = random.randint(1,100)

ca_list = []
for row in range(N):
    covering_array = itertools.combinations(range(k), t)
    ca_list.append(covering_array)

#check_array = list(itertools.product(range(v), repeat=t))

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

if verify_covering_array(ca_list):
    f'Yay, a covering array!'
else: 
    f'There is an imposter among us!'





    #for row in covering_array:
        #output = True
        #vals_in_row = tuple(row[col])
        #for col in columns
            #if col in vals_in_row:
                #continue
            #else:
                #output = False
                #break
        #return output

#verify_covering_array(ca_list)