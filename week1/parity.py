def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n:bool):
     return n % 2 == 0
        
    
        
    
if __name__=="__main__":
    main()
