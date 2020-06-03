from itertools import product
from math import floor


def splitter(lst, input_string):
    out = list()
    for k in lst:
        out.append(input_string[:k])
        input_string = input_string[k:]
        if input_string[:k] == "":
            break
    return out


def combinations(target):
    numbers_to_use = [1, 2]
    output = []
    lst = []
    for n in range(floor(target/2),target+1):
        numbers = product(numbers_to_use, repeat=n)
        lst.append(list(numbers))
    for i in lst:
        for j in i:

            if sum(j) == target:
                output.append(j)
    return output


elements=['H', 'B', 'C', 'N', 'O', 'F', 'P', 'S', 'K', 'V', 'Y', 'I', 'W', 'U', 'HE', 'LI', 'BE', 'NE', 'NA', 'MG', 'AL', 'SI', 'CL', 'AR', 'CA', 'SC', 'TI', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']


def chem_name(string):
    string = string.upper()
    comb = combinations(len(string))
    output = list()
    out = list()

    for i in comb:
        k = (splitter(i, string))
        out.append(k)

    for i in out:
        if set(i).issubset(elements):
            output.append(i)

    if len(output)>0:
        output = output[0]
        for n, i in enumerate(output):
            if len(i)>1:
                i[1].lower()
                output[n] = i[0]+i[1].lower()
        return output
    else:
        return False


f = open('20k.txt ', 'r+')
lines = [line for line in f.readlines()]
f.close()
word_list =list(map(lambda s: s.strip(), lines))
with open("words.txt", "w") as txt_file:
    for n,i in enumerate(word_list):
        print(n)
        try:
            i = i.upper()
            k = chem_name(i)
            if k:
                fin_list.append(k)
        except MemoryError:
            txt_file.write(str(fin_list))
            fin_list = []


    txt_file.write(str(fin_list))
