class Solution:
    def hasDuplicate(self, arr):
        counts = {}
        for digit in arr:
            counts[digit] = counts.get(digit, 0)+1

        return any(freq>1 for freq in counts.values())

def main():
    arr = [1,2,3,3]
    counts = {}

    solution = Solution()
    result = solution.hasDuplicate(arr)

if __name__ == "__main__":
    main()
        