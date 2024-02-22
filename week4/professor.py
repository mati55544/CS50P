from random import randint
from typing import Literal


def main():
    total = 0
    level = get_level()
    for _ in range(10):
        x = genrate_integer(level)
        y = genrate_integer(level)

        total += int(check(x, y))
        # total += 1 if check(x,y) else 0
    print("score: ", total)


# accept from user level
def get_level() -> Literal[1, 2, 3]:
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int((input("level-")))

        except ValueError:
            pass
    return level


def genrate_integer(level: Literal[1, 2, 3]) -> int:
    return randint(10 ** (level - 1), (10**level) + 1)
    # if level == 1:
    #     return randint(1,10)
    # if level == 2:
    #     return randint(11,99)
    # if level == 3:
    #     return randint(100,999)


def check(x: int, y: int) -> bool:
    for _ in range(3):
        try:
            answer = int(input(f"{x}+{y} ="))
            if answer == x + y:
                return True

        except ValueError:
            pass
        print("eee")

    print(f"{x}+{y} ={x+y}")


    return False


if __name__ == "__main__":
    main()
