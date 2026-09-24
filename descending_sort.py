numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

descending = sorted(numbers, reverse=True)

print("Descending order:", descending)
