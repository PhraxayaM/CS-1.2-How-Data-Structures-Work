# Task
# Given an integer, n, perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  2 to 5, print Not Weird
# If  is even and in the inclusive range of  6 to  20, print Weird
# If  is even and greater than 20, print Not Weird
#
# Psuedocode
# 1. "Given an integer, n" -> create variable that takes in user input
# 2.create func that checks remainder so that it can determine even or odd int
# 3. in func, create statement that determines if odd, print Weird
#2 and 4 should be even
# 4. if func is even and inclusive range of

## not weird = odd, 2, 4, or greater than 20 and even
## weird = even, inclusive 6 to 20

n = int(input().strip())
## check defaults to false and will print false unless statement is true.
check = {True: "Not Weird", False: "Weird"}


print(check[
## if int divided by remainder is equal to 0, number is even and if int is al in range of 2-6
    n%2 == 0 and (
    n in range(2,6) or
        n > 20
    )

])


"""
Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
"""
