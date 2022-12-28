# A. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 
# или x² + 5 = 0 или 10*x² = 0

import random
# k_number = int(input('Please, enter k - degree of a polynomial: '))

def create_and_print_polynominal(ke:int):
    dict_1={}
    poli_str =''
    for i in range(ke+1):
        dict_1[i]=random.randint(-100,100)
        print('{}:{}'.format(i,dict_1[i]))
    for k, v in dict_1.items():
        if k==0:
            if v>0:
                poli_str = f'+{v}{poli_str}'
            elif v<0:
                poli_str = f'{v}{poli_str}'
            else:
                continue
        elif k == 1 and v > 0:
            poli_str = f'+{v}*x{poli_str}' 
        elif k==1 and v<0:
            poli_str = f'{v}*x{poli_str}'
        elif k>1 and k<ke:           
            if v>1:
                poli_str = f'+{v}*x**{k}{poli_str}'
            elif v<-1:
                poli_str = f'{v}*x**{k}{poli_str}'
            elif v==1:
                poli_str = f'+x**{k}{poli_str}'
            elif v==-1:
                poli_str = f'-x**{k}{poli_str}'
        elif k==ke:
            if v==1 or v==-1:
                poli_str = f'x**{k}{poli_str}'
            else:
                poli_str = f'{v}*x**{k}{poli_str}'
        else:
            poli_str = f'{v}*x**{k}{poli_str}'
    return poli_str + "=0"
# print(create_and_print_polynominal(k_number))

# data = open('poli_fail.txt', 'w+')
# data.writelines(create_and_print_polynominal(k_number))


# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
# гененинуем размер случайных полиномов
k1_number =random.randint(1,5)
k2_number=random.randint(1,5)

if k1_number >k2_number:
    k_max = k1_number 
else: k_max= k2_number
print(k1_number, k2_number)
# создаем файл с полиномами
data = open('poli_fail1.txt', 'w')
with open('poli_fail1.txt','w') as data:
    data.write(create_and_print_polynominal(k1_number))
print('\n')
with open('poli_fail2.txt','w') as data:
    data.write(create_and_print_polynominal(k2_number))


content1=''
with open('poli_fail1.txt','r') as data:
    content1=data.readline()

content2=''
with open('poli_fail2.txt','r') as data:
    content2=data.readline()



def find_sum_in_files(equation:str):
    new_koef = {}
    nq = equation.replace(' ','').replace('=0','').replace('+',' ').replace('-',' -').split(' ')
    print(nq)
    for item in nq:
        if 'x**' in item:
            a,b = item.split('x**')
            new_koef[int(b)]=int(item.split('*x')[0])
        elif '*x' in item:
            new_koef[1]=int(item.split('*x')[0]) 
        else:
            new_koef[0]=item
    return new_koef
dict_content1 = find_sum_in_files(content1)
dict_content2 = find_sum_in_files(content2)
for item in dict_content1:
    print('{}:{}'.format(item,dict_content1[item]))
for item in dict_content2:
    print('{}:{}'.format(item,dict_content2[item]))
poli_sum={}
# складываем многочлены
print(f'размер многочлена будет {k_max}')
for i in range(k_max+1):
    poli_sum[i]=int(dict_content1.get(i, 0))+int(dict_content2.get(i,0))
for item in poli_sum:
    print('{}:{}'.format(item,poli_sum[item]))
# создаем строку для записи в суммарный файл
string_sum = ''
def create_polynominal(poli_sum:dict):
    for k, v in poli_sum.items():
        if k==0:
            if v>0:
                string_sum = f'+{v}'
            elif v<0:
                string_sum = v
            else:
                continue
        elif k == 1 and v > 0:
            string_sum = f'+{v}*x{string_sum}' 
        elif k==1 and v<0:
            string_sum = f'{v}*x{string_sum}'
        elif k>1 and k<k_max:           
            if v>1:
                string_sum = f'+{v}*x**{k}{string_sum}'
            elif v<-1:
                string_sum = f'{v}*x**{k}{string_sum}'
            elif v==1:
                string_sum = f'+x**{k}{string_sum}'
            elif v==-1:
                string_sum = f'-x**{k}{string_sum}'
        elif k==k_max:
            if v==1 :
                string_sum = f'x**{k}{string_sum}'
            if v==-1:
                string_sum = f'-x**{k}{string_sum}'
            else:
                string_sum = f'{v}*x**{k}{string_sum}'
        else:
            string_sum = f'{v}*x**{k}{string_sum}'
    return string_sum + "=0"
string_result = create_polynominal(poli_sum)
print(f'String result {string_result}')
with open('sum_fail.txt','w') as data:
    data.write(string_result)