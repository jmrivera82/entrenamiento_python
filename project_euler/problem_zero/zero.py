"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5²=5x5=25 ; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,25, and the sum of the odd squares is  1+9+25=35.

Among the first 217 thousand square numbers, what is the sum of all the odd squares?
"""

total=217000 #217000
odds=[]
sum=0
square=0
for number in range(total):
    square=number*number
    if square%2==1:
        odds.append(square)
        sum+=square

print(odds)
print(sum)