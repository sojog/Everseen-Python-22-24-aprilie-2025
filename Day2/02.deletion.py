class A:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print(f"del {self.x}", end=" ")

a = A(1)
b = A(2)
del a
print("end")