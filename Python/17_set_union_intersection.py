s1 = {23, 5, 23, 65, 5, 6}
s2 = {5, 63, 6, 76}

print("The union of this set is :", s1.union(s2))
print("The intersection of this set is :", s1.intersection(s2))
print({5, 6}.issubset(s1))
print({5, 6, 7}.issubset(s2))
