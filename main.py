#!/usr/bin/env python3

import animals.cat
import animals.dogs.izzie
import shapes.circle


def main():
    print("------ The main function ------")
    print()
    animals.cat.meow()
    print()
    shapes.circle.roll()
    print()
    animals.dogs.izzie.speak()

    print('-'*80)

    animals.cat.package_name()
    shapes.circle.package_name()


if __name__ == "__main__":
    main()
