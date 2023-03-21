from pyfiglet import Figlet
from cs50 import get_string
import random
import sys


figlet = Figlet()
fonts = []
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit(1)
    if f in fonts:
        figlet.setFont(font=f)
    else:
        print("Invalid font")
        sys.exit(1)

elif len(sys.argv) == 1:
    #f = random.choice(fonts)
    figlet.setFont(font=random.choice(fonts))
else:
    print("Invalid usage")
    sys.exit(1)


s = get_string("Imput text to be converted: ")
print(figlet.renderText(s))


