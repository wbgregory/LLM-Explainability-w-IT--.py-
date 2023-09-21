#created below is a covering array, along with another variable that contains value sets - the covering array is compared to the value sets in order to verify the presence of the value sets within the
#covering array, to make sure that it is indeed a covering array.

#additional notes - t = strength, k = columns, v = values within a specific row x column, N = rows.
#.combinations generates column sets while .product generates value sets

import itertools
import random

t = 2
k = 20
v = 3
N = random.randint(1,100)

ca_list = []
for row in range(N):
    #random.choices(range(v), k=k)
    #covering_array = itertools.combinations(range(k), t)
    ca_list.append(random.choices(range(v),k=k))
# print(ca_list)

#check_array = list(itertools.product(range(v), repeat=t))

def verify_covering_array(ca):
    verify = True
    for columns in itertools.combinations(range(k), t):
        #for values in itertools.product(range(v), repeat = t):
            #assign_name = list(k[col] for col in columns)
            #assign_value = list(v[val] for val in values)
        combos = set()
        for row in ca:
            assign_name = tuple(row[col] for col in columns)
            combos.add(assign_name)
            #assign_name = list(values in columns)
            #vals.append(values)
        if len(combos) != v**t:
            return False
            
            # for row in ca:
            #     if row in combos:
            #         continue
            #     else:
            #         verify = False
    return verify

if verify_covering_array(ca_list):
    print(f'Yay, a covering array!')
else: 
    print(f'There is an imposter among us!')





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