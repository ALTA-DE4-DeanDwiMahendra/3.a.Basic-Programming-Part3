# input
student_score = 80
# Process: Your Solution Code Here
def penilaian_dosen(score):
    if 80 <= score <= 100:
        return "Nilai A"
    elif 65 <= score <= 79:
        return "Nilai B+"
    elif 50 <= score <= 64:
        return "Nilai B"
    elif 35 <= score <= 49:
        return "Nilai C"
    elif 0 <= score <= 34:
        return "Nilai D"
    else:
        return "Nilainya tidak ada/ Kosong/ Belum dinilai"
##main programnya
def main():
    #memasukkan nilai skornya
    score = student_score
    print(penilaian_dosen(score))
##Outputnya Nilai A karena nilainya 80
print(penilaian_dosen(student_score))
print(penilaian_dosen(70))