import statistics

# buka dan baca file csv dataset3_fix.csv
variable = open('dataset3_fix.csv', 'r')

list_student = []

# simpan data dari dataset3.csv ke list_student
for row in variable.readlines():
    list_student.append(row.split(';'))
variable.close()

labels = list_student.pop(0)

n = len(list_student)

def maxdat(x):
    maxx = max(x)
    return maxx

def mindat(x):
    minn = min(x)
    return minn

def meandat(x):
    meann = sum(x)/n
    meannn = round(meann, 4)
    return meannn

def vardat(x):
    varr = statistics.variance(x)
    varrr = round(varr, 4)
    return varrr

def stddevdat(x):
    stddevv = statistics.stdev(x)
    stddevvv = round(stddevv, 4)
    return stddevvv

def modedat(x):
    from statistics import mode
    modee = mode(x)
    return modee

# cari nilai outlier low/high dari setiap kategori nilai
# IQR methode
def bubble_sort(x):
    n = len(x) 
    for i in range(n): 
        for j in range(n - i - 1): 
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

def outlow(list):
    data = bubble_sort(list)
    low_out = []
    pos_q1 = 1/4*(len(data)+1)
    pos_q3 = 3/4*(len(data)+1)
    q1 = (data[int(pos_q1) - 1] + data[int(pos_q1)]) / 2
    q3 = (data[int(pos_q3) - 1] + data[int(pos_q3)]) / 2
    IQR = q3 - q1
    min_IQR = q1 - (1.5 * IQR)
    #print(min_IQR)
    for i in data:
        if (i < min_IQR):
            low_out.append(i)
    return low_out

def outhigh(list):
    data = bubble_sort(list)
    high_out = []
    pos_q1 = 1/4*(len(data)+1)
    pos_q3 = 3/4*(len(data)+1)
    q1 = (data[int(pos_q1) - 1] + data[int(pos_q1)]) / 2
    q3 = (data[int(pos_q3) - 1] + data[int(pos_q3)]) / 2
    IQR = q3 - q1
    max_IQR = q3 + (1.5 * IQR)
    #print(max_IQR)
    for i in data:
        if (i > max_IQR):
            high_out.append(i)
    return high_out