print("dz3")

# number = int(input("Enter 5-digits number: "))
number = int('12345')
print("This is the number: ", number)

print("Variant 1")
backward_number = (number % 10) * 10_000
number = number // 10
backward_number = backward_number + ((number % 10) * 1000)
number = number // 10
backward_number = backward_number + ((number % 10) * 100)
number = number // 10
backward_number = backward_number + ((number % 10) * 10)
number = number // 10
backward_number = backward_number + (number % 10)
print(backward_number)
