#!/usr/bin/python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_value = prev_row[j - 1] + prev_row[j]
                new_row.append(new_value)
            new_row.append(1)
            triangle.append(new_row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

