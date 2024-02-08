def main():
    first_string = input("please type str-")
    print(returns_str(first_string))

    
   
    


def returns_str(first_string:str):
    last_str =""
    for word in first_string:
        if word.lower() in ['a','e','i','o','u']:
            last_str += ''
        else:
            last_str += word
    
    return last_str



if __name__=="__main__":
    main()

