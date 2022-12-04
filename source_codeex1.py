def swap_tuples(tuples_list):
    res = []
    for t in tuples_list:
        if 0 not in t:
            (x,y) = t[1],t[0]
            res.append((x,y))
    return res