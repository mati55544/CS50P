from pyfiglet import Figlet
import sys
import random

fonts = Figlet().getFonts()
if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        f = sys.argv[2]
    else:
        sys.exit("invalid arguments")


s = input("input: ")
print(Figlet(font=f).renderText(s))
