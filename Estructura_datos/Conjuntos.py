# -*- coding: utf-8 -*-
s = set([1, 2, 3]) # conjunto
t = set([3, 4, 5])

print(s.union(t)) #union

print(s.intersection(t)) #interseccion

print(s.difference(t)) #diferencias
print(t.difference(s))

print(1 in s) #pertenece
print(1 not in s) # no pertenece