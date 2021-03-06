#1
#Functions are first-class objects - they can be passed around and used as arguments
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

#print(greet_bob(say_hello))
#print(greet_bob(be_awesome))


#2
#functions can contain other functions (inner functions)
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

def first_child():
    print("Printing from the first_child() outer function")

#parent()
#first_child()


#3
#You can use functions as return values
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child()
    else:
        return second_child()

print(parent(2))