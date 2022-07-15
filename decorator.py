def decorator(f):
    def new_function() -> object:
        print("Extra functionality")
        f()
    return new_function

@decorator
def initial_function():
    print("Initial Functionality")

initial_function()
