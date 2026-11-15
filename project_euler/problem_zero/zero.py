"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5²=5x5=25 ; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,25, and the sum of the odd squares is  1+9+25=35.

Among the first 248 thousand square numbers, what is the sum of all the odd squares?
"""

total_numeros=24 #248000
odds=[]
suma=0
for numero in range(total_numeros):
    if numero%2==1:
        odds.append(numero)
        suma+=numero

print(odds)
print(suma)