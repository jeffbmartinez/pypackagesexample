from shapes import circle


def package_name():
    print(f'This is {__name__}')


def meow():
    print(f'This is in {__name__}')
    print("🐈🐈🐈🐈")
    print("circle call from inside meow:")
    circle.roll()
    print("^^^ end of meow function ^^^")
