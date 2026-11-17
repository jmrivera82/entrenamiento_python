"""
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of the number 600851475143
"""

target=600851475143
div =2
aux=0
largest_prime_factor=0
num=1
sw=False

while div * div <= target:

    if target%div==0:
        aux=div
        num=2

        while True:

            if num==div:
                largest_prime_factor=num
                break

            elif (div%num==0): 
                break

            num+=1

    div+=1

print(largest_prime_factor)







###Solución que no sirve para números demasiado grandes###

"""

target=13195
value=0
values = []
prime_factors=[]
div=1
aux=0
sw=True


value = target 
while True: #Obtengo los divisores
    if div > value:
        break

    else:
        if value % div ==0:
            values.append(div)
    div+=1
#print(values)

for number in range(1,len(values)):
    aux=values[number]
    for i in range(2,aux):
        if aux%i==0:
            sw=False
            i=aux
    if sw==True:
        prime_factors.append(values[number])


        
print(prime_factors)
print(prime_factors[-1])

"""
