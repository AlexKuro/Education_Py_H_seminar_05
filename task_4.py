""" 
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
"""
def encoder(st1):
    st2 = ''
    st3 = ''
    st4 = ''
    for st in st1:
        if st != st2:
            coun = 0
            st4 += st3
            st2 = st

        if st == st2:
            coun += 1
            st3 = str(coun) + st2
    st4 += st3
    return st4


def decoding(st2):
    coun = ''
    st3 = ''
    for st in st2:
        if st.isdigit():
            coun += st
        else:
            st3 += st * int(coun)
            coun = ''
    return st3


f1 = open('file_task_4_1.txt', 'r')
st1 = f1.readline()
f1.close()

print(f"\nТекст из файла --------> {st1}")
encod = encoder(st1)
print(f"\nСжатие данных ---------> {encod}")
decod = decoding(encod)
print(f"\nВосстановления данных -> {decod}\n")
