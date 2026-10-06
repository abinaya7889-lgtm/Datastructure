import heapq

orders = []

heapq.heappush(orders, (30, "Pizza"))
heapq.heappush(orders, (15, "Burger"))
heapq.heappush(orders, (20, "Biryani"))
heapq.heappush(orders, (10, "Sandwich"))

print("Delivery Order:")

while orders:
    time, food = heapq.heappop(orders)
    print(food, "-", time, "minutes")