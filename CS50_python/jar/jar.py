import sys


class Jar:
    def __init__(self, capacity=12):
        if capacity < 1 or not isinstance(capacity, int):
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # returns str with n🍪
        if self.size == 0:
            print("zero cookies")
        return "🍪" * self.size

    def deposit(self, n):
        n = int(n)
        if n < 0:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        n = int(n)
        if n < 0:
            raise ValueError
        if self.size < n:
            raise ValueError

        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1 or not isinstance(capacity, int):
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        if size > self.capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    text = input("Would you like to add or retrieve a cookie? ")
    if text == "add":
        jar.deposit(input(f"You have {jar} in jar, how many do you want to add? "))
    elif text == "retrieve":
        jar.withdraw(input(f"You have {jar} cookies left, how many do you want? "))
    else:
        sys.exit("Jar Closed")
    print(f"You have {jar} cookies now.")


if __name__ == "__main__":
    main()
