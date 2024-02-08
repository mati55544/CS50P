def main():
    x = input("please type something- ")
    
    print(split(x))


def split(x):
    result = ""
    if x.lower().startswith("hello"):
        result ="$0"
    elif x.lower().startswith("h"):
        result = "$20"
    
    else:
        result = "$100"
        

    return result

    

if __name__=="__main__":
    main()

