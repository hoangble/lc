class Solution:
    def isNumber(self, s: str) -> bool:
        # dfa[0] = {'group': 'next_state'}
        dfa = [
            {"number": 1, "sign": 2, "dot": 3},  # 0
            {"number": 1, "dot": 4, "exp": 5},  # 1
            {"number": 1, "dot": 3},  # 2
            {
                "number": 4,
            },  # 3
            {"number": 4, "exp": 5},  # 4
            {"sign": 6, "number": 7},  # 5,
            {"number": 7},  # 6
            {"number": 7},  # 7
        ]

        state = 0
        for c in s:
            if "0" <= c <= "9":
                group = "number"
            elif c in {"+", "-"}:
                group = "sign"
            elif c in {"E", "e"}:
                group = "exp"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[state]:
                return False

            state = dfa[state][group]

        return state in {1, 4, 7}


class NoDot:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2},
            {"digit": 1, "exp": 3},
            {"digit": 1},
            {"digit": 5, "sign": 4},
            {"digit": 5},
            {"digit": 5},
        ]

        state = 0
        for c in s:
            if "0" <= c <= "9":
                group = "digit"
            elif c in {"+", "-"}:
                group = "sign"
            elif c == "e" or c == "E":
                group = "exp"
            else:
                return False

            if group not in dfa[state]:
                return False

            state = dfa[state][group]

        return state in {1, 5}


class NoExp:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2},
            {"digit": 1, "exp": 3},
            {"digit": 1},
            {"digit": 5, "sign": 4},
            {"digit": 5},
            {"digit": 5},
        ]

        state = 0
        for c in s:
            if "0" <= c <= "9":
                group = "digit"
            elif c in {"+", "-"}:
                group = "sign"
            elif c == "e" or c == "E":
                group = "exp"
            else:
                return False

            if group not in dfa[state]:
                return False

            state = dfa[state][group]

        return state in {1, 5}


if __name__ == "__main__":
    test_cases = ["1e6", "2e10", "-90E3", "3e+7", "+6e-1", "00089", "--6", "-+3", "95a54e53"]
    for test_case in test_cases:
        print(Solution().isNumber(test_case), NoDot().isNumber(test_case))
