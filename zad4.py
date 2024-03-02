height_str = input("Enter the height of the triangle: ")
base_str = input("Enter the length of the base of the triangle: ")

try:
    height = int(height_str)
    base = int(base_str)

    if (height > 0) and (base > 0):
        area = height * base / 2
        print("The area of the triangle is:", area)
    else:
        print("One or more values is negative.")

except ValueError:
    print("Given values are not integers.")
