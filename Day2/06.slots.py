class A:
    __slots__ = ('x', 'y')


print(A.__slots__)

A.__slots__ = ('x', 'y', 'z')
a = A()
a.x = 10
a.y = 20
# a.z = 100

# print(a.z)

# print(a.__dict__)