# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
    city = int(input())
    inp = input()
    out = input()

    ans = ""
    for i in range(city):
        #append i+1 ... N-1
        app = "Y"
        for j in range(i+1, city):
            if inp[j] == "Y" and out[j-1] == 'Y' and app[-1] == 'Y':
                app += "Y"
            else:
                app += "N"
        app = app[1:]

        #prepend i-1 ... 0
        pre = "Y"
        for j in range(i-1, -1, -1):
            if inp[j] == "Y" and out[j+1] == 'Y' and pre[-1] == 'Y':
                pre += "Y"
            else:
                pre += "N"
        row = pre[::-1]+app+"\n"
        ans = ans+row

    print("Case #{}:".format(c))
    print(ans, end="")
  # check out .format's specification for more formatting options
