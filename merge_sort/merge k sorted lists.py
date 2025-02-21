amount = 8  # len(lists)
interval = 1
while interval < amount:
    for i in range(0, amount - interval, interval * 2):
        print(i, i + interval)
        # lists[i] = self.merge2Lists(lists[i], lists[i + interval])
    interval *= 2

# return lists[0] if amount > 0 else None
