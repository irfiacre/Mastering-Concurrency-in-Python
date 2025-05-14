import concurrent
from concurrent.futures.process import ProcessPoolExecutor
from timeit import default_timer as timer
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return True
    

input = [i for i in range(10 ** 13, 10 ** 13 + 500)]

start = timer()
result = []

with ProcessPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(is_prime, i) for i in input]
    
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        if future.result():
            result.append(input[i])
        
    
# for i in input:
#     if is_prime(i):
#         result.append(i)

print("---- Result:", result)
print("== Time:", timer() - start)
