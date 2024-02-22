# import random

# #coin = random.choice(["heads","tails"])
# #number = random.randint(1, 10 )
# cards = ["jack","5","4","king","queen"]
# random.shuffle(cards)

# for card in cards:
#     print(card)

# #print(number)
 

# import statistics

# print(statistics.mean([100, 90 ]))
import sys 
# try:
#     print("hello , my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
if len(sys.argv) <2:
    print("too few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print("hello my name is", sys.argv[1])
    