# def main():
#     name = input("please type your file including the ending-")
#     print(type_file(name))


# def type_file(name):
#     out = ""
#     match name.split('.')[-1]:
           
#         case "gif":  
#             out = "you got graphics format"
#         case _:
#               out = "unknown file "
#     return out 

from collections import defaultdict

def type_file(name:str) -> str:
    "recives file name with extinsions returns extionions name"
    file_types = defaultdict(lambda: "Not Present")

    file_types.update({
        "gif": "graphics format",
        "jpg": " image file",
        "jpeg": " image file",
        "png": " image file",
        "txt": " a txt file",
        "zip": " zip file"
    })
    splitted_file = str(name).rsplit(sep=".", maxsplit=1)
    return file_types[splitted_file[1]]

def label_creator(extension_name:str)  -> None:
    
    print("you got", extension_name)

def default_action():
    for i in range(10):
        print(i)

def main():

    # name = input("please type your file including the ending-")
    file_name = "Matan.gif"
    extension_name = type_file(file_name)
    label_creator(extension_name)


# def type_file(name):
#     out = ""
#     extension = name.split(".")[-1]
#     if extension == "gif":
#         out = "you got graphics format"
#     elif extension in ["jpg", "jpeg", "png"]:
#         out = "you got an image file "
#     elif extension == "txt":
#         out = "you got a txt file"
#     elif extension == "zip":
#         out = "you got zip file"
#     else:
#         out = "unknown file"
#     return out



if __name__=="__main__":
     main()

# def type_file(name):
#     file_types = {
#         "gif": "you got graphics format",
#         "jpg": "you got an image file",
#         "jpeg": "you got an image file",
#         "png": "you got an image file",
#         "txt": "you got a txt file",
#         "zip": "you got zip file"
#     }

#     return file_types[name]
    
    

