t = int(input())

for t in range(1, t+1):
    num = input()

    ans1 = ""
    ans2 = ""
    for c in num:
        if c != '4':
            ans1 += c
            ans2 += '0'
        else:
            ans1 += '3'
            ans2 += '1'

    print("Case #{}: {} {}".format(t, ans1, ans2))
