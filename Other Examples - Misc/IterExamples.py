'''
We can use the iter() function to generate an iterator to an iterable object, such as a dictionary, list, set, etc.
Basic syntax is: iterator = iter(iterable)

We can simply load objects one by one using next(iterator), until we get the StopIteration Exception.
'''
print("Example 1")
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'


'''
For custom objects, we are also able to use the iter() function but we must define its behavior
The __iter__() method creates the iterator object, which we then update using __next__().
The terminating condition is when the current value is greater than the maximum value, 
which is when we raise a StopIteration exception.
'''
print("")
print("Example 2")
class MyClass():
    def __init__(self, max_val):
        # Set the maximum limit (condition)
        # max_val must be a natural number
        assert isinstance(max_val, int) and max_val >= 0
        self.max_val = max_val
    def __iter__(self):
        # Called when the iterator is generated
        # Initialise the value to 0
        self.value = 0
        return self
    def __next__(self):
        # Called when we do next(iterator)
        if self.value >= self.max_val:
            # Terminating condition
            raise StopIteration
        self.value += 1
        # Return the previously current value
        return self.value - 1

# Set the limit to 10
my_obj = MyClass(10)

# An iterator to the object
my_iterator = iter(my_obj)

while True:
    try:
        val = next(my_obj)
        print(f"Iterator Loaded {val}")
    except StopIteration:
        print("Iterator loading ended!")
        break



'''
We can also use an optional sentinel value - i.e. 10 below. This can create a pretty elegant iterator.
'''
print("")
print("Example 3")
a = 0

def x():
    global a
    a = a + 2
    return a

iterator = iter(x, 12)
for item in iterator:
    print(item)


'''
If the object is not callable when sentinel is given, iter() raises TypeError.
The __call__ line below explained:
Python has a set of built-in methods and __call__ is one of them. The __call__ method enables Python programmers 
to write classes where the instances behave like functions and can be called like a function. When the instance 
is called as a function.
E.g. object() is shorthand for object.__call__()
Here, we are essentially assigning a "call" to a double object to execute the next method - making it callable
'''
print("")
print("Example 4")
class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__

my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)
