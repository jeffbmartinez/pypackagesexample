from .. import cat


def package_name():
    print(f'This is {__name__}')


def speak():
    print("/ speak section \\")
    print("I eat and I poop. Woof.")

    cat.meow()

    print("\\ end of dog section /")
