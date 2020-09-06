class Solution:
    def checkValidString(self, s: str) -> bool:
        copy = ""
        for c in s:
            if c == '(' or c == "*":
                copy += c
            else: #create new substring
                found = False
                for i in reversed(range(len(copy))):
                    if copy[i] == '(': #found
                        found = True
                        copy = copy[:i] + copy[i+1:]
                        break

                if not found:
                    for i in reversed(range(len(copy))):
                        if copy[i] == '*': #found
                            found = True
                            copy = copy[:i] + copy[i+1:]
                            break

                if not found:
                    return False

        #the rest of the * in the copy must be ')' or empty string
        copy = list(copy)
        while len(copy) != 0:
            #if no more '('
            shouldBreak = True
            for c in copy:
                if c == '(':
                    shouldBreak = False

            if shouldBreak:
                return True

            for i in range(len(copy)):
                if copy[i] == '(':
                    found = False
                    for j in range(i+1, len(copy)):
                        if copy[j] == '*':
                            copy[i] = '-'
                            copy[j] = '-'
                            found = True
                            break
                    if not found:
                        return False
        return True

test = Solution()
print(test.checkValidString("()")) #true
print(test.checkValidString("(*()")) #true
print(test.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")) #false
print(test.checkValidString("(*))")) #true
print(test.checkValidString("*(")) #false
print(test.checkValidString("(*()))")) #true
print(test.checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)")) #true
