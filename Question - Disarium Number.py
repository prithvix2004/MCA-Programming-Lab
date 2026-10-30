def is_disarium(n):
    temp = n
    digits = 0
    total = 0

    # Count digits
    while temp > 0:
        digits += 1
        temp //= 10

    temp = n
    while temp > 0:
        last_digit = temp % 10
        total += last_digit ** digits
        digits -= 1
        temp //= 10

    return total == n

num = int(input("Enter a number : ")
if is_disarium(num):
    print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")
