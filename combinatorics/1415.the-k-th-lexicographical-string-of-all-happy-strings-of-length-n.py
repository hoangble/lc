class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        result = ["a"] * n  # Initialize result with 'a' characters

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        start_a = 1
        start_b = start_a + (2 ** (n - 1))
        start_c = start_b + (2 ** (n - 1))

        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        for char_index in range(1, n):
            # Calculate the midpoint of the group for the current character position
            midpoint = 2 ** (n - char_index - 1)

            # Determine the next character based on the value of k
            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)

Solution().getHappyString(3, 9)