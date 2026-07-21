def test_args(*args):
    sum = 0

    for arg in args:
        print(arg, end=" ")


test_args(1, 2, 3, 4)
print(" ")

def test_kwargs(**kwargs):

    for key, value in kwargs.items(): # Use .item() when checking both key value pairs

        if value in ("Andrian", "Kesian", "Melody", "Melanie"):
            print("Nice")
            break

        print(f"{key}: {value}.")

    if "name" in kwargs: # Use "in", it automatically checks the keys by default.
        print("Test") 



test_kwargs(name = "Andrian", age = 20, address = "Liberation")
test_kwargs(name = "Melody", age = 20, address = "Liberation")
test_kwargs(name = "Kesian", age = 20, address = "Liberation")
test_kwargs(name = "Melanie", age = 20, address = "Liberation")