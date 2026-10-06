def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]

    left = [x for x in bookings[1:]
            if x["movie"].lower() <= pivot["movie"].lower()]

    right = [x for x in bookings[1:]
             if x["movie"].lower() > pivot["movie"].lower()]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"id": 103, "name": "Kaviya", "movie": "Jailer"},
    {"id": 101, "name": "Abinaya", "movie": "Avatar"},
    {"id": 104, "name": "Priya", "movie": "Vikram"},
    {"id": 102, "name": "Ravi", "movie": "Leo"}
]

sorted_bookings = quick_sort(bookings)

print("Bookings Sorted by Movie:")
for b in sorted_bookings:
    print(b)