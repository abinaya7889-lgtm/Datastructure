def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]

    left = [x for x in bookings[1:]
            if x["name"].lower() <= pivot["name"].lower()]

    right = [x for x in bookings[1:]
             if x["name"].lower() > pivot["name"].lower()]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"name": "Ravi", "movie": "Leo", "seat": "A5"},
    {"name": "Abinaya", "movie": "Jailer", "seat": "B2"},
    {"name": "Kaviya", "movie": "Vikram", "seat": "C4"},
    {"name": "Priya", "movie": "Avatar", "seat": "A2"}
]

sorted_bookings = quick_sort(bookings)

print("Bookings Sorted by Customer Name:")
for b in sorted_bookings:
    print(b)