#https://interviewing.io/recordings/Python-Google-12
memo = {}
arr = [1, 2, 3]

def dp(idx, left):
    print(idx, left)
    if left < 0 or idx == len(arr):
        return False
    if left == 0:
        return True
    if (idx, left) in memo:
        return memo[(idx, left)]

    result = dp(idx+1, left-arr[idx]) or dp(idx+1, left)
    memo[(idx, left)] = result
    return result


print(dp(0, 3))
print("memo" + str(memo))


from collections import defaultdict

class Solution:

    def partition(self, array):
        dict = defaultdict(set)
        dict[0].add(0)

        for i, elem in enumerate(array):
            next = i+1
            for x in dict[i]:
                dict[next].add(x-elem)
                dict[next].add(x+elem)

        print(dict)
        return 0 in dict[len(array)]

test = Solution()
print(test.partition([3, 2, 1, 7, 9]))
