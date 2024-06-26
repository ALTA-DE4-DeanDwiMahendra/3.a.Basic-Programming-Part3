def print_factors(number):
    print(f"Faktor dari {number} adalah:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Main programnya
def main():
    try:
        num = int(input("Masukkan bilangan bulat: "))  # Membaca input dari pengguna dan konversi ke integer
        if num <= 0:
            print("Masukkan bilangan positif.")
        else:
            print_factors(num)
    except ValueError:
        print("Input harus berupa bilangan bulat.")

if __name__ == "__main__":  # Memastikan script ini bisa dieksekusi langsung
    main()

# Outputnya adalah 1, 2, 3, 6
print_factors(6)
# Outputnya adalah 1, 2, 4, 5, 10, 20
print_factors(20)
