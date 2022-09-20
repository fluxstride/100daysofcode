def greet(name):
    """A simple function illustrating closures"""
    text = "Welcome to the world of closures #100daysofcode."

    def inner_function():
        return "Hello {}! {}".format(name, text)

    return inner_function


greet_samuel = greet("Samuel")
greet_daniel = greet("Daniel")

print(greet_samuel())
# closed values in greet_samuel
print(f"closed value 1: {greet_samuel.__closure__[0].cell_contents}")
print(f"closed value 2: {greet_samuel.__closure__[1].cell_contents}")
print("*" * 50)


print(greet_daniel())
# closed values in greet_daniel
print(f"closed value 1: {greet_daniel.__closure__[0].cell_contents}")
print(f"closed value 2: {greet_daniel.__closure__[1].cell_contents}")
print("*" * 50)
