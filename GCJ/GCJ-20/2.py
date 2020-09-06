t = int(input())

def solve(s):
    result = ""

    numOpen, numClose = 0, 0
    for c in range (len(s)):
        curr = int(s[c])
        #add opening parentheses
        shouldAdd = curr - numOpen
        numOpen += shouldAdd
        for i in range(shouldAdd):
            result += '('

        #add the number itself
        result += s[c]

        #add the closing parentheses
        if c == len(s)-1:
            #end of string, close all
            for i in range(numOpen):
                result += ')'
            numOpen = 0
        else:
            next = int(s[c+1])
            if next < curr:
                shouldClose = curr-next
                for i in range(shouldClose):
                    result += ')'
                numOpen -= shouldClose

    return result

for _ in range(1, t+1):
    s = input()
    result = solve(s)
    print("Case #{}: {}".format(_, result))
