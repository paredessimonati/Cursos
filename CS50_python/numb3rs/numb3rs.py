import sys


def main():
    ip_address = input("Enter IP Address: ")
    ip_address = validate(ip_address)
    if ip_address is True:
        print("True")
    else:
        print("Invalid")


def validate(ip_address):
    try:
        ip1, ip2, ip3, ip4 = ip_address.split(".")
    except ValueError:
        return False
    try:
        ip1, ip2, ip3, ip4 = int(ip1), int(ip2), int(ip3), int(ip4)
    except ValueError:
        return False
    if all(0 <= val <= 255 for val in (ip1, ip2, ip3, ip4)):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
