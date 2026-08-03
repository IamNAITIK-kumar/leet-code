class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = []
        for i in range(1, n + 1):
            if (i % 3 == 0 and i % 5 == 0):
                a.append("FizzBuzz")
            elif(i % 3 == 0):
                x = "Fizz"
                a.append(x)
            elif (i % 5 == 0):
                y = "Buzz"
                a.append(y)
            else:
                a.append(str(i))

        return(a)
