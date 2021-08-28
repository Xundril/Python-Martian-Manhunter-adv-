import random


def color_generator():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


if __name__ == '__main__':
    print(color_generator())
