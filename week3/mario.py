def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(1,n):
         print(i, end =" ")
         print("#" * i)


if __name__ == "__main__":
    main()
