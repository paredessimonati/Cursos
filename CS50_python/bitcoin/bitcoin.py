import sys
import requests


def main():
    while True:
        try:
            bitc = float(sys.argv[1])
            break
        except IndexError:
            sys.exit("(͡ ° ͜ʖ ͡ °)")
        except ValueError:
            sys.exit("(◕ᴥ◕ʋ)")
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("(-(-_-(-_(-_(-_-)_-)-_-)_-)_-)-)")
    price = r.json()["bpi"]["USD"]["rate"]
    amount = float(price.replace(",", "")) * bitc
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
