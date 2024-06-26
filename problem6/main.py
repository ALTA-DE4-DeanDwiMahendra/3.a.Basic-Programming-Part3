#Problem 6 - Full Prima
def prima(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def full_prima(number):
    #Memeriksa apakah number adalah bilangan prima
    if not prima(number):
        return False
    #Memeriksa apakah setiap digit dari number adalah bilangan prima
    for digit in str(number):
        if not prima(int(digit)):
            return False
    return True

# Main program to test the function
def main():
    try:
        num = int(input("Masukkan sebuah bilangan: "))
        if full_prima(num):
            print("Ya")
        else:
            print("Tidak")
    except ValueError:
        print("Input harus berupa bilangan bulat.")
if __name__ == "__main__":
    main()
print(full_prima(2))
print(full_prima(3))
print(full_prima(11))
print(full_prima(13))
print(full_prima(23))
print(full_prima(29))
print(full_prima(37))
print(full_prima(41))
print(full_prima(43))
print(full_prima(53))
