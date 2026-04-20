# 🔹 SAME DATASET (unchanged)
orders = [
    {"order_id": 4832, "priority": 2, "time": 14, "distance": 12, "status": "Packed"},
    {"order_id": 1275, "priority": 1, "time": 9,  "distance": 5,  "status": "Ready"},
    {"order_id": 9021, "priority": 3, "time": 18, "distance": 20, "status": "Pending"},
    {"order_id": 3568, "priority": 1, "time": 11, "distance": 8,  "status": "Ready"},
    {"order_id": 7410, "priority": 2, "time": 16, "distance": 15, "status": "Packed"},
    {"order_id": 6157, "priority": 1, "time": 10, "distance": 25, "status": "Ready"},
    {"order_id": 7783, "priority": 2, "time": 15, "distance": 18, "status": "Ready"},
    {"order_id": 2146, "priority": 1, "time": 9,  "distance": 3,  "status": "Ready"},
    {"order_id": 8451, "priority": 1, "time": 7,  "distance": 6,  "status": "Ready"}
]


def filter_ready_orders(orders):
    ready_orders = []
    
    for i in range(len(orders)):
        if orders[i]["status"] == "Ready":
            ready_orders.append(orders[i])
    
    return ready_orders


def merge_sort_orders(orders):
    if len(orders) <= 1:
        return orders

    mid = len(orders) // 2
    left = merge_sort_orders(orders[:mid])
    right = merge_sort_orders(orders[mid:])

    return merge(left, right)


def compare(o1, o2):
    if o1["priority"] != o2["priority"]:
        return o1["priority"] < o2["priority"]

    if o1["time"] != o2["time"]:
        return o1["time"] < o2["time"]

    return o1["distance"] < o2["distance"]


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Step 1: Filter
ready_orders = filter_ready_orders(orders)

# Step 2: Sort
sorted_orders = merge_sort_orders(ready_orders)

print("\nFinal Dispatch Order:")
for i in range(len(sorted_orders)):
    o = sorted_orders[i]
    print("Order", o["order_id"], "| Priority", o["priority"], "| Time", o["time"], "| Distance", o["distance"])



    