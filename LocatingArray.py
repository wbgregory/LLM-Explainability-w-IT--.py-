# Locating Array Verifier

import random
import itertools
from Gregory_CoveringArray import verify_covering_array


def rows_of(interaction, locating_array):
    combos = set()
    # print(interaction)
    columns = interaction[0]
    values = interaction[1]
    idx = 0
    for row in locating_array:
        vals_in_row = tuple(row[col] for col in columns)
        if vals_in_row == values:
            combos.add(idx)
        idx += 1
    return combos


def locating_array_verifier(locating_array_list, t, vs, d, n_syns, lamb):
    # print(locating_array_list)
    if not verify_covering_array(locating_array_list, t, vs, lamb):
        return False
    all_cols = itertools.combinations(range(len(vs)), t)
    interactions = []
    for col_set in all_cols:
        rng = []
        # for v in tuple(vs[col] for col in col_set):
        for col in col_set:
            rng.append(n_syns[col])
        all_vals = itertools.product(*rng)
        for val_set in all_vals:
            interactions.append((col_set, val_set))
    rows_dict = dict()
    d_col = itertools.combinations(interactions, d)
    for dset1, dset2 in itertools.combinations(d_col, 2):
        if dset1 in rows_dict:
            rows1 = rows_dict[dset1]
        else:
            rows1 = set()
            for I1 in dset1:
                rows1 = rows1.union(rows_of(I1, locating_array_list))
            rows_dict[dset1] = rows1
        if dset2 in rows_dict:
            rows2 = rows_dict[dset2]
        else:
            rows2 = set()
            for I2 in dset2:
                rows2 = rows2.union(rows_of(I2, locating_array_list))
            rows_dict[dset2] = rows2
        if len(rows1.symmetric_difference(rows2)) < lamb:
            print(dset1, dset2)
            return False
    return True


if __name__ == '__main__':
    d = 1
    t = 3
    k = 5
    v = 3
    N = 10

    la_list = []
    for row in range(N):
        la_list.append(random.choices(range(v), k=k))

    if locating_array_verifier(la_list):
        print(f'This is a locating array!')
    else:
        print(f'This is not a locating array.')

    while locating_array_verifier(la_list) != True:
        N *= 2
        la_list = []
        for row in range(N):
            la_list.append(random.choices(range(v), k=k))


# extra lines of code


# while verify_covering_array != True:
    # N += 1
    # la_list = []
    # for row in range(N):
    # la_list.append(random.choices(range(v),k=k))

# while verify_covering_array != True:
    # N *= 2
    # la_list = []
    # for row in range(N):
    # la_list.append(random.choices(range(v),k=k))

    # if locating_array_verifier():
    #     print(f'This is a locating array!')
    # else:
    #     print(f'This is not a locating array.')


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

# add back in covering array verifier to then test the locating array for covering property
