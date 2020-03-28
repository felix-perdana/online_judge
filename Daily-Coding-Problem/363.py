class Adder:
    def __init__(self, val, sign=None):
        self.val = val
        self.sign = sign if sign else 1

    def __call__(self, val):
        val = self.val + self.sign * val
        sign = self.sign * -1

        return Adder(val, sign)

    def __str__(self):
        return str(self.val)

def add_subtract(num):
    return Adder(num)

print(add_subtract(3)(7)(3))

def stringLength(val):
    return len(val)

arr = ["abc", "a", "bc"]
arr.sort(key = stringLength, reverse = True)

print(arr)
