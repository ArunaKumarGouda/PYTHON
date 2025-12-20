def sequence(tup):
    # code here 
    d = tup[1] - tup[0]
    last_term = tup[-1]
    next_three = [last_term + d * (i+1) for i in range(3)]
    return tup + tuple(next_three)