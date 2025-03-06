lists = [1, 2, 3, 4, 5, 6, 7, 8]
interval = 2
n = len(lists)
while interval < n:
    print(interval)
    for i in range(0, n - interval, interval):
        print(i, i + interval)
    interval = interval * 2
