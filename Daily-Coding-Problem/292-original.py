from collections import deque

def make_teams(kids):
    teams = {0: [], 1: []}
    visited = set()

    while kids:
        start = next(iter(kids))
        if not assign(kids, teams, start, visited):
            return False

    return teams

def assign(kids, teams, start, visited):
    queue = deque([(start, 0)])

    while queue:
        kid, team = queue.popleft()
        teams[team].append(kid)

        enemies = kids.pop(kid)
        for enemy in enemies:
            if enemy in teams[team]:
                return False
            elif enemy not in visited:
                queue.append((enemy, 1 - team))

        visited.add(kid)

    return True

kids = {
0: [2],
1: [3, 4],
2: [0, 3, 4],
3: [2],
4: [2]
}

print(make_teams(kids))

'''
0: [2],
1: [3, 4],
2: [0],
3: [2],
4: [2]

0 2
3 1
4
'''
