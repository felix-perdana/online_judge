from collections import deque

def make_team(kids):
    teams = {0: set(), 1: set()}
    visited = set()

    enhanced_kids = enhance_kids(kids)

    for kid in enhanced_kids:
        if kid not in visited:
            assign_kid(kid, enhanced_kids, teams, visited)

    #check duplicate in both teams
    if has_duplicate(enhanced_kids, teams):
        return False

    return teams

def enhance_kids(kids):
    enhanced_kids = {}
    for kid in kids:
        enhanced_kids[kid] = set(kids[kid])

    for kid in kids:
        for enemy in kids[kid]:
            enhanced_kids[enemy].add(kid)

    return enhanced_kids

def has_duplicate(kids, teams):
    duplicate_checker = {}

    for kid in kids:
        duplicate_checker[kid] = 0

    for team in teams:
        for kid in teams[team]:
            if duplicate_checker[kid] == 0:
                duplicate_checker[kid] = 1
            else:
                return True

    return False

def assign_kid(kid, kids, teams, visited):
    queue = set([(kid, 0)])

    while queue:
        kid, team = queue.pop()
        print(kid, team)
        teams[team].add(kid)
        visited.add(kid)
        print(teams)

        #process his enemies
        enemies = kids[kid]

        print("enemies: " + str(enemies))
        for enemy in enemies:
            if enemy not in visited:
                queue.add((enemy, 1-team))
        print(queue)
        print("====================")

def test1():
    kids = {
        0: [1, 3, 5, 7],
        1: [0, 2, 4, 6],
        2: [1, 3, 5, 7],
        3: [0, 2, 4, 6],
        4: [1, 3, 5, 7],
        5: [0, 2, 4, 6],
        6: [1, 3, 5, 7],
        7: [0, 2, 4, 6]
    }

    print(make_team(kids))

def test2():
    kids = {
        0: [2],
        1: [3, 4],
        2: [0, 3, 4],
        3: [2],
        4: [2]
    }

    print(make_team(kids))

test1()
test2()
