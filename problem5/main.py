def power(x, n):
    return x ** n

# Main program untuk mengetes function
def main():
    try:
        x = int(input("Masukkan nilai x: "))
        n = int(input("Masukkan nilai n: "))
        result = power(x, n)
        print(f"Output: {result}")
    except ValueError:
        print("Input harus berupa bilangan bulat.")

# Run the main program
if __name__ == "__main__":
    main()

# Sample test cases
print(power(2, 3))  # Output: 8
print(power(7, 2))  # Output: 49