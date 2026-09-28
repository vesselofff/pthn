mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

last_index = {}
min_dist = {}
pair_indices = {}

for i, x in enumerate(mass):
    if x in last_index:
        dist = i - last_index[x]
        if x not in min_dist or dist < min_dist[x]:
            min_dist[x] = dist
            pair_indices[x] = (last_index[x], i)
    last_index[x] = i

for val in set(mass):
    if val in pair_indices:
        print(f"for {val} min distance: {min_dist[val]}, index: {pair_indices[val][0]} и {pair_indices[val][1]}")
    else:
        print(f"for {val} no repeat")
