def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]
    left = [x for x in bookings[1:] if x["price"] <= pivot["price"]]
    right = [x for x in bookings[1:] if x["price"] > pivot["price"]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"name": "Abinaya", "movie": "Avatar", "price": 250},
    {"name": "Priya", "movie": "Leo", "price": 180},
    {"name": "Kaviya", "movie": "Jailer", "price": 220},
    {"name": "Divya", "movie": "Vikram", "price": 150}
]

sorted_bookings = quick_sort(bookings)

print("Bookings Sorted by Ticket Price:")
for b in sorted_bookings:
    print(b)