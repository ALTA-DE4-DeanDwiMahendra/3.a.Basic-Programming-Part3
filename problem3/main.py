def prime_number(number):
    # Bilangan prima harus lebih besar dari 1
    if number <= 1:
        return "Not Prime"
    # 2 dan 3 adalah bilangan prima
    if number <= 3:
        return "Prime"
    # Bilangan genap atau kelipatan 3 bukan bilangan prima
    if number % 2 == 0 or number % 3 == 0:
        return "Not Prime"
    # Cek bilangan dari 5 hingga akar kuadrat dari number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return "Not Prime"
        i += 6
    return "Prime"

# Your code here
def main():
    try:
        num = int(input("Masukkan sebuah bilangan: "))
        if prime_number(num) == "Prime":
            print("Output: Prime")
        else:
            print("Output: Not Prime")
    except ValueError:
        print("Input harus berupa bilangan bulat.")

# Sample Test Cases   
print(prime_number(7))
print(prime_number(10))
print(prime_number(11))
print(prime_number(13))
print(prime_number(17))
print(prime_number(20))
print(prime_number(35))