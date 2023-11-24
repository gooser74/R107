import time
N = int(input("Entrez la valeur de N: "))

for i in range(N, 0, -1):
    print(i)
    time.sleep(1)


#

import time

Q = int(input("Entrez la valeur de Q: "))
i = Q
while i >= 1:
    print(i)
    time.sleep(1)
    i -= 1