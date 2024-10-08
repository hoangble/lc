class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if self.helper(cards):
            return True
        return False

    def helper(self, num_list) -> bool:
        # print(num_list)
        if len(num_list) == 1:
            # print(num_list[0])
            # return num_list[0] == 24 or num_list[0] == 24.0
            return abs(num_list[0] - 24) <= 0.1
        # if 24 in set(num_list): return True
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                new_list = num_list.copy()
                op1, op2 = new_list[i], new_list[j]

                new_list.pop(j)
                new_list.pop(i)

                for op in ["+", "-", "*", "/", "--", "//"]:
                    if op == "+":
                        new_list.append(op1 + op2)
                    elif op == "-":
                        new_list.append(op1 - op2)
                    elif op == "*":
                        new_list.append(op1 * op2)
                    elif op == "/":
                        if op2 == 0:
                            continue
                        new_list.append(op1 / op2)
                    elif op == "--":
                        new_list.append(op2 - op1)
                    elif op == "//":
                        if op1 == 0:
                            continue
                        new_list.append(op2 / op1)

                    if self.helper(new_list):
                        return True
                    new_list.pop()
