# Check if a number is an Armstrong number
num = int(input("Enter a number: "))
num1=len(str(num))

temp = num
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num1
    temp //= 10

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")


##############################
# Armstrong numbers in a given range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Armstrong numbers b/w", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    num1 = len(str(num))
    temp = num
    sum_of_powers = 0

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num1
        temp //= 10

    if sum_of_powers == num:
        print(num)
