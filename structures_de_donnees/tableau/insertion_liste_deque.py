import time, collections
N = 1000000

for p in range(0, 3):
    print("passage ", p)
    print("  insertion en fin")

    li = list()
    a = time.perf_counter()
    for i in range(0, N):
        li.append(i)
    b = time.perf_counter()
    print("    list", N, "éléments, temps par éléments :", (b-a)/N)

    li = collections.deque()
    a = time.perf_counter()
    for i in range(0, N):
        li.append(i)
    b = time.perf_counter()
    print("    deque", N, "éléments, temps par éléments :", (b-a)/N)

    print("  insertion au début ")
    li = collections.deque()
    a = time.perf_counter()
    for i in range(0, N):
        li.appendleft(i)
    b = time.perf_counter()
    print("    deque ", N, "éléments, temps par éléments :", (b-a)/N)

    N2 = N // 100
    li = list()
    a = time.perf_counter()
    for i in range(0, N2):
        li.insert(0, i)
    b = time.perf_counter()
    print("    list", N2, "éléments, temps par éléments :", (b-a)/N2)

print('\n\nOn voit que l’insertion au début du tableau est beaucoup plus coûteuse pour une liste que pour un deque')