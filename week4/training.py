# import sys
# while True:
#     try:
#         n = input("type a number-")
#         y = int(n)
        
#     except ValueError:
#         print("isnt num")
#     except KeyboardInterrupt:
#         print("have a good day")
#         break
        
try:
    while not input("Enter a number:").isdecimal():
        print("You did not enter a number")
except KeyboardInterrupt:
    print("\nHave a nice day!")
    # sys.exit(1)
    
    