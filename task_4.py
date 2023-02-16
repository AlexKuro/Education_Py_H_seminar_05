""" 
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
"""

f1 = open('file_task_4_1.txt', 'r')
st1 = f1.readline()
f1.close()

print(f"\nТекст из файла - '{st1}'\n")
st2 = ''
st3 = ''
st4 = ''
t = len(st1)
d = j = 0
coun = 0
fl = True


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


print(encoder(st1))
