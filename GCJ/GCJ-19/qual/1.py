t = int(input())

for t in range(1, t+1):
    num = input()

    ans1 = ""
    for c in num:
        if c != '4':
            ans1 += c
        else:
            ans1 += '3'


    print("Case #{}: {} {}".format(t, ans1, int(num)-int(ans1)))
