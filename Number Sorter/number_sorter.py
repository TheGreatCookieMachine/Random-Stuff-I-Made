import random


n = 0
low = 0
high = 0
process = []
result = []
while len(process) < 1000:
    process.append(random.randint(1, 1000))
print(process)
while n < len(process):
    if process[n] > high:
        result.append(process[n])
        high = process[n]
        if low == 0:
            low = process[n]
    elif process[n] < low:
        result.insert(0, process[n])
        low = process[n]
    else:
        n2 = 0
        while True:
            if process[n] <= result[n2]:
                result.insert(n2, process[n])
                break
            n2 = n2+1
    n = n+1
print(result)
