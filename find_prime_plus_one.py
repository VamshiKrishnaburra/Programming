def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_plus_one(nums):
    result = []
    for num in nums:
        if is_prime(num + 1):
            result.append(str(num))
    print(" ".join(result))

# Example usage
input_str = input("Enter numbers separated by space: ")
numbers = list(map(int, input_str.strip().split()))
find_prime_plus_one(numbers)
