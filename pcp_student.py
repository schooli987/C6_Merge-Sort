def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Sort in DESCENDING order
        if left[i]["marks"] > right[j]["marks"]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Main Program
students = [
    {"name": "Ayaan", "marks": 78},
    {"name": "Zoya", "marks": 92},
    {"name": "Rohan", "marks": 85},
    {"name": "Meera", "marks": 67}
]

sorted_students = merge_sort(students)

# Display Rankings
print("Student Rankings:\n")
for i in range(len(sorted_students)):
    print(i + 1, sorted_students[i]["name"], sorted_students[i]["marks"])