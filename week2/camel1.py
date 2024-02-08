#from camel_converter import to_snake
# import re


# #name = 'name'
# #name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
# #print(name)



# #snake = to_snake("myString")

# def main():
#     camel_case = input("please type str in camel case-")
#     print(converter(camel_case))
    



# def converter(robert):
#     snake = ""
#     snake = robert 
#     snake = re.sub(r'(?<!^)(?=[A-Z])', '_', snake).lower()
#     return snake
    



# main()

def main():
    camel_case = input("please type str in camel case-")
    print(converter(camel_case))


def converter(camel_case:str):
    result ="" 
    for character in camel_case:
        if character.isupper():
            result += '_'
            result += character.lower()

        else:
            result += character



    return result


if __name__=="__main__":
    main()

