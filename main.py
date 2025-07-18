import sys

print(sys.getsizeof([0, 1 ,2]))
print(sys.getsizeof((0, 1 ,2)))
print(sys.getsizeof({0, 1 ,2}))
print(sys.getsizeof({'a': 1, "b": 2, "c": 0}))