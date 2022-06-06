class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fizz" * (not bool(i % 3)) + "Buzz" * (not bool(i % 5)) +
                str(i) * (bool(i % 5) * bool(i % 3)) for i in range(1, n+1)]
