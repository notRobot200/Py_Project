import csv
# import fungsi untuk mengubah file csv yang kurang sesuai deskripsi
# berhubung file dataset3.csv sudah sesuai deskripsi maka langsung dilanjutkan poin berikutnya 
import func_task as fun
import func_stat as stat

# buka dan baca file csv dataset3_fix.csv
variable = open('dataset3_fix.csv', 'r')

list_student = []

# simpan data dari dataset3.csv ke list_student
for row in variable.readlines():
    list_student.append(row.split(';'))
variable.close()

labels = list_student.pop(0)

# memberi tipe data integer untuk setiap kategori nilai
i=0
for line in list_student:
    list_student[i][1] = int(line[1])
    list_student[i][2] = int(line[2])
    list_student[i][3] = int(line[3])
    list_student[i][4] = int(line[4])
    list_student[i][5] = int(line[5])
    list_student[i][6] = int(line[6])
    i+=1

# tugas1 = 1
# tugas2 = 2
# quiz1 = 3
# quiz2 = 4
# uts = 5
# uas = 6
# nilai = 7

# menghitung dan menyisipkan kolom nilai akhir
i = 0
for line in list_student:
    final_grade = (0.15 * ((list_student[i][1] + list_student[i][2])/2)) + (0.15 * ((list_student[i][3] + list_student[i][4])/2)) + (0.35 * list_student[i][5]) + (0.35 * list_student[i][6])
    list_student[i].append(round(final_grade, 4))
    i+=1
copied_list_student = list_student.copy()
#print(copied_list_student)_fiqih

n = len(list_student)

# memasukkan setiap kategori nilai ke list
x_1 = (list(line[1] for line in list_student)) #tugas1
x_2 = (list(line[2] for line in list_student))
x_3 = (list(line[3] for line in list_student))
x_4 = (list(line[4] for line in list_student))
x_5 = (list(line[5] for line in list_student))
x_6 = (list(line[6] for line in list_student))
x_7 = (list(line[7] for line in list_student)) #nilai

#cari nilai max dari setiap kategori nilai
list_max = []
list_max.append("MAX")
for i in range(1, 8):
    n_max = stat.maxdat(int(line[i]) for line in list_student)
    list_max.append(n_max)
print(list_max)
list_student.append(list_max)

#cari nilai min dari setiap kategori nilai
list_min = []
list_min.append("MIN")
for i in range(1, 8):
    n_min = stat.mindat(int(line[i]) for line in list_student)
    list_min.append(n_min)
print(list_min)
list_student.append(list_min)

#cari nilai rata-rata dari setiap kategori nilai
list_mean = []
list_mean.append("MEAN")
for i in range(1, 8):
    n_mean = stat.meandat(int(line[i]) for line in list_student)
    list_mean.append(n_mean)
print(list_mean)
list_student.append(list_mean)

#cari nilai variance dari setiap kategori nilai
list_var = []
list_var.append("VAR")
for i in range(1, 8):
    n_var = stat.vardat(float(line[i]) for line in list_student)
    list_var.append(n_var)
print(list_var)
list_student.append(list_var)

#cari nilai standar deviasi dari setiap kategori nilai
list_stddev = []
list_stddev.append("STD DEV")
for i in range(1, 8):
    n_stddev = stat.stddevdat(float(line[i]) for line in list_student)
    list_stddev.append(n_stddev)
print(list_stddev)
list_student.append(list_stddev)

# cari nilai median dari setiap kategori nilai
list_median = []
list_median.append("MEDIAN")
mid = int(n/2)
for i in range(1, 8):
    n_median = (list_student[mid-1][i] + list_student[mid][i]) / 2
    list_median.append(n_median)
print(list_median)
list_student.append(list_median)

# cari nilai modous dari setiap kategori nilai
list_mode = []
list_mode.append("MODE")
for i in range(1, 8):
    n_mode = stat.modedat(int(line[i]) for line in list_student)
    list_mode.append(n_mode)
print(list_mode)
list_student.append(list_mode)

# cari nilai lowout dari setiap kategori nilai
list_lowout = []
list_lowout.append("LOW OUT")
outl_x1 = stat.outlow(x_1)
list_lowout.append(outl_x1)
outl_x2 = stat.outlow(x_2)
list_lowout.append(outl_x2)
outl_x3 = stat.outlow(x_3)
list_lowout.append(outl_x3)
outl_x4 = stat.outlow(x_4)
list_lowout.append(outl_x4)
outl_x5 = stat.outlow(x_5)
list_lowout.append(outl_x5)
outl_x6 = stat.outlow(x_6)
list_lowout.append(outl_x6)
outl_x7 = stat.outlow(x_7)
#print(outl_x7)
list_lowout.append(outl_x7)
print(list_lowout)
list_student.append(list_lowout)

#cari nilai highout dari setiap kategori nilai
list_highout = []
list_highout.append("HIGH OUT")
outh_x1 = stat.outhigh(x_1)
list_highout.append(outh_x1)
outh_x2 = stat.outhigh(x_2)
list_highout.append(outh_x2)
outh_x3 = stat.outhigh(x_3)
list_highout.append(outh_x3)
outh_x4 = stat.outhigh(x_4)
list_highout.append(outh_x4)
outh_x5 = stat.outhigh(x_5)
list_highout.append(outh_x5)
outh_x6 = stat.outhigh(x_6)
list_highout.append(outh_x6)
outh_x7 = stat.outhigh(x_7)
#print(outh_x7)
list_highout.append(outh_x7)
print(list_highout)
list_student.append(list_highout)

# perbaiki elemen dari list sebelum di tulis ke file csv
list_student.insert(0, labels)
list_student[0][6] = "UAS"
list_student[0].append("NILAI")

# NIM dengan nilai UTS tertinggi
max_uts_nim = str(fun.findMaxUTS(copied_list_student, int(list_max[5])))
print("NIM dengan nilai UTS tertinggi : ", max_uts_nim)

# NIM dengan nilai UAS terendah
min_uas_nim = str(fun.findMinUAS(copied_list_student, int(list_min[6])))
print("\nNIM dengan nilai UAS terendah : ", min_uas_nim)

# NIM dengan nilai quiz 1 di atas rata2
nim_quiz1 = fun.findQuiz1AboveMean(copied_list_student, list_mean[3])
print("\nNIM dengan nilai quiz 1 di atas rata-rata : ", nim_quiz1)

# NIM dengan nilai quiz 2 di bawah median
nim_quiz2 = fun.findQuiz2BelowMedian(copied_list_student, list_median[4])
print("\nNIM dengan nilai quiz 2 di bawah median : ", nim_quiz2)

# NIM dengan nilai tugas 1 di bawah median
nim_tugas1 = fun.findTugas1BelowMedian(copied_list_student, list_median[1])
print("\nNIM dengan nilai tugas 1 di bawah median : ", nim_tugas1)

# NIM dengan nilai tugas 2 di atas rata2
nim_tugas2 = fun.findTugas2AboveMean(copied_list_student, list_mean[2])
print("\nNIM dengan nilai tugas 2 di atas rata-rata : ", nim_tugas2)

# NIM dengan nilai akhir menjadi pencilan bawah
nim_nilaioutl = fun.findNilaiOutlierL(copied_list_student, list_lowout[7])
print("\nNIM dengan nilai menjadi pencilan bawah : ", nim_nilaioutl)

# NIM dengan nilai akhir menjadi pencilan atas
nim_nilaiouth = fun.findNilaiOutlierH(copied_list_student, list_highout[7])
print("\nNIM dengan nilai menjadi pencilan atas : ", nim_nilaiouth)

# NIM dengan nilai akhir kurang dari mean
nim_nilai = fun.findNilaiAboveMean(copied_list_student, list_mean[7])
print("\nNIM dengan nilai akhir di atas rata-rata : ", nim_nilai)

# tulis file dataset3_fix.csv
with open('dataset3_finally_fix.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(list_student)
# file .csv with delimiter ','
f.close()

# change the delimiter from ',' to ';'
reader = csv.reader(open("dataset3_finally_fix.csv", "r"), delimiter=',')
writer = csv.writer(open("dataset3_fixed.csv", 'w', newline='\n'), delimiter=';')
writer.writerows(reader)
# file .csv with delimiter ';'