def greet(name):
    text = "Welcome to the world of closures #100daysofcode."

    def inner_function():
        return "Hello {}! {}".format(name, text)

    return inner_function


greet_samuel = greet("Samuel")
greet_daniel = greet("Daniel")

print(greet_samuel())
print(greet_daniel())
