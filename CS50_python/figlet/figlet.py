from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        text = input("Enter text to be converted: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("(ノಠ益ಠ)ノ彡┻━┻")
elif len(sys.argv) == 1:
    text = input("Enter text to be converted: ")
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))
else:
    sys.exit("(ノಠ益ಠ)ノ彡┻━┻")
