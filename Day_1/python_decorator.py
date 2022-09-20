import time


def decorator_1(func):
    """A Simple decorator"""
    def wrapper(*qrgs, **kwargs):
        print("Start")
        func(*qrgs, **kwargs)
        print("End")
    return wrapper


@decorator_1
def function_1():
    print("Hello World!")


function_1()


def decorator_2(func):
    """A Simple decorator to check a functions execution time"""
    def wrapper(*qrgs, **kwargs):
        beginning = time.time()
        func(*qrgs, **kwargs)
        end = time.time()

        print("Time taken to run {}: {}".format(
            func.__name__, end - beginning))
    return wrapper


@decorator_2
def function_2():
    print("Greetings. My name is {}".format("Samuel"))


function_2()


def decorator_3(func):
    def wrapper(*qrgs, **kwargs):
        beginning = time.time()
        returned_value = func(*qrgs, **kwargs)
        end = time.time()

        print("Time taken to run {}: {}".format(
            func.__name__, end - beginning))

        return returned_value
    return wrapper


@decorator_3
def sum(a, b):
    return a + b


print(sum(1, 4))


def decorator_4(*args, **kwargs):
    """Decorator with parameters"""
    name = kwargs["name"]

    def inner(func):
        def wrapper(*args, **kwargs):
            func(name=name, *args, **kwargs)

        return wrapper

    return inner


@decorator_4(name="Samuel Adekoya")
def greet(name, age):
    print("Hello my name is {} and i am {} years old".format(name, age))


greet(age=20)
