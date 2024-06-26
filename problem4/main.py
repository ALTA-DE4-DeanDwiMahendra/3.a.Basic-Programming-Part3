def palindrome(s):
    # Menghapus semua spasi dan mengubah ke huruf kecil
    cleaned = ''.join(s.split()).lower()
    # Membandingkan string asli dengan versi terbaliknya
    return cleaned == cleaned[::-1]

# Sample Test Cases   
print(palindrome("civic"))  # True
print(palindrome("katak"))  # True
print(palindrome("kasur rusak"))  # True
print(palindrome("kupu-kupu"))  # False
print(palindrome("lion"))  # False