# list = copied
# n_max = list max 5
def findMaxUTS(list, n_max):
    for line in list:
        if line[5] == n_max:
            str_nim = str(line[0])
            return str_nim

def findMinUAS(list, n_min):
    for line in list:
        if line[6] == n_min:
            str_nim = line[0]
            return str_nim

def findQuiz1AboveMean(list, n_mean):
    list_nim = []
    for line in list:
        if line[3] > n_mean:
            list_nim.append(str(line[0]))
    return list_nim

def findQuiz2BelowMedian(list, n_median):
    list_nim = []
    for line in list:
        if line[4] < n_median:
            list_nim.append(str(line[0]))
    return list_nim

def findTugas1BelowMedian(list, n_median):
    list_nim = []
    for line in list:
        if line[1] < n_median:
            list_nim.append(str(line[0]))
    return list_nim

def findTugas2AboveMean(list, n_mean):
    list_nim = []
    for line in list:
        if line[2] > n_mean:
            list_nim.append(str(line[0]))
    return list_nim

def findNilaiOutlierL(list, n_lowout):
    list_nim = []
    for line in list:
        if line[7] == n_lowout:
            list_nim.append(str(line[0]))
    return list_nim

def findNilaiOutlierH(list, n_highout):
    list_nim = []
    for line in list:
        if line[7] == n_highout:
            list_nim.append(str(line[0]))
    return list_nim

def findNilaiAboveMean(list, n_mean):
    list_nim = []
    for line in list:
        if line[7] > n_mean:
            list_nim.append(str(line[0]))
    return list_nim