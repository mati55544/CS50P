def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
            print("#" * width)


if __name__== "__main__":
      main()
