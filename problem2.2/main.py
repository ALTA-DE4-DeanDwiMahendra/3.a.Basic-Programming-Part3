## Problem 2.2 - Faktor Bilangan
## Process : Your solution code here
# Function to find and return factors of a given number
def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Main program
def main():
    try:
        num = int(input("Masukkan sebuah bilangan: "))
        if num <= 0:
            print("Masukkan bilangan positif.")
        else:
            factors = get_factors(num)
            factors.reverse()  # Reverse the order of factors to get descending order
            print(f"Faktor dari {num} adalah:")
            for factor in factors:
                print(factor)
    except ValueError:
        print("Input harus berupa bilangan bulat.")
if __name__ == "__main__":
    main()
# Outputnya 6, 3, 2, 1
print(get_factors(6)[::-1])
# outputnya 20, 10, 5, 4, 2, 1
print(get_factors(20)[::-1])