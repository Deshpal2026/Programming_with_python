def decorator_func(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()