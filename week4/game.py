from random import randint

n = int(input("level: "))
while n < 1:
    n = int(input("level: "))


x = randint(1, n)
guess = 0

while guess != x:
    try:
        guess = int(input("inpu: "))
        if guess < x:
            print("too small! ")
        elif guess > x:
            print("too big")

    except ValueError:
        pass
print("they are equal")
