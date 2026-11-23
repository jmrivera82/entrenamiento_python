"""
A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009=91x99  .

Find the largest palindrome made from the product of two 3-digit numbers.
"""
"""
number=10
numbers=[]
for i in range(number):
    numbers.append(i+1)

print(numbers)
"""
number,number2=0,0
start=99
end=999
palindrome=[]

for i in range(end,start,-1):
    for j in range(end,start,-1):
        number = i*j
        number2 = int(str(number)[::-1])
        if number==number2:
            #print(f"{i}x{j} = {number}, is palindrome")
            palindrome.append(number)
            palindrome.sort()
print(palindrome[-1])