class C:
    baz = 50

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


obj1 = C(10, 20)
obj2 = C(4, 7)

print(obj1.foo)
obj1.foo = 35
print(obj1.foo)
print(obj2.foo)

print(obj1.baz)
print(obj2.baz)
print(C.baz)

print("C.baz = 100")
C.baz = 100

print(obj1.baz)
print(obj2.baz)
print(C.baz)

print("obj1.baz = 200")
obj1.baz = 200

print(obj1.baz)
print(obj2.baz)
print(C.baz)