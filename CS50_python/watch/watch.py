import re
import sys
from re import search


def main():
    print(parse(input("HTML: ")))


def parse(url):
    if matches := re.search(r'(?:https?://)?(?:www.)?youtube.com/(?:embed/)(.+)"', url, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
