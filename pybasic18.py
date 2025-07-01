#Exercise: 19: Print Alternate Prime Numbers till 20
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n=20
prime=[]
for i in range(2,n+1):
    if is_prime(i):
        prime.append(i)

for i in range(0,len(prime),2):
    print(prime[i])
