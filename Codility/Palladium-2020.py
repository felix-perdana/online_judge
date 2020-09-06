# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    tallestBuilding = 0
    right = [0 for i in range(len(H))]
    for i in reversed(range(len(H))):
        h = H[i]
        if h > tallestBuilding:
            tallestBuilding = h
        right[i] = tallestBuilding

    tallestBuilding = 0
    smallestArea = 100000 * 10001
    for i in range(len(H)):
        h = H[i]
        if h > tallestBuilding:
            tallestBuilding = h
        area1 = tallestBuilding * (i+1)
        #calculate the right area
        area2 = 0
        if i+1 < len(H):
            area2 = right[i+1]*(len(H)-i-1)
        smallestArea = min(smallestArea, area1+area2)

    return smallestArea

print(solution([3, 1, 4])) #10
print(solution([5, 3, 2, 4])) #17
print(solution([5, 3, 5, 2, 1])) #19
print(solution([7, 7, 3, 7, 7])) #35
print(solution([1, 1, 7, 6, 6, 6])) #30
print(solution([4, 3, 2, 1]))
