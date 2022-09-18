#1.1) 
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')
print('\t\tUp above the world so high,')
print('\t\tLike a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are')

#1.2) 
import sys
print (sys.version)
print (sys.version_info)

#1.3) 
from datetime import datetime
print('Current date time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

#1.4) 
import math
r = float(input('Nhập bán kính hình tròn: '))
area = math.pi * r * r
print(area)

#1.5) 
firstName = input('Input first name: ')
lastName = input('Input last name: ')
print('Full name: ', lastName, firstName)

#1.6) 
n = input("Nhập danh sách cần tách : ")
list = n.split(" ")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#1.7) 
fileName = input('Input file name: ')
f = fileName.split('.')
print(f[-1])

#1.8) 
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

#1.9) 
exam_st_date = (11,12,2014)
print(f'{exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')

#1.10) 
n = int(input('Nhập n: '))
sum = int(f'{n}')+int(f'{n}{n}')+int(f'{n}{n}{n}')
print(sum)

#1.11) 
print(abs.__doc__)

#1.12) 
import calendar
mon = int(input('Input month: '))
year = int(input('Input year: '))
print(calendar.month(year, mon))

#1.13) 
print('a string that you "don\'t" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example')

#1.14) 
from datetime import date
d1 = date(2014,7,2)
d2 = date(2014,7,11)
print(str((d2-d1).days) + ' ngày')

#1.15) 
from math import pi
r = 6
v = 4/3 * pi * r * r * r
print(v)

#1.16) 
soGoc = 17
n = int(input('Nhập n: '))
hieu = n - soGoc
if n >= soGoc:
    print(hieu * 2)
elif n < soGoc:
    print(abs(hieu))
    
#1.17) 
n = int(input('Nhập n: '))
if abs(1000 - n) <= 100 or abs(2000 - n) <= 100:
    print('Số đã nhập nằm trong khoảng 100 của 1000 hoặc 2000')
else:
    print('Số đã nhập nằm ngoài khoảng 100 của 1000 hoặc 2000')
    
#1.18) 
n1 = int(input('Nhập n1: '))
n2 = int(input('Nhập n2: '))
n3 = int(input('Nhập n3: '))

if n1 == n2 == n3:
    print((n1+n2+n3)*2)
else:
    print(n1+n2+n3)
    
#1.19) 
str = input('Input string: ')
if str[:2] == "Is":
    print(str)
else:
    print('Is' + str)

#1.20) 
str = input('Input string: ')
n = int(input('Nhập n: '))
print(str * n) 

#1.21) 
n = int(input('Nhập n: '))
if n & 1 == 0: 
    print('Số chẵn')
else:
    print('Số lẻ')

#1.22) 
arr = [1,2,3,4,5,6,4,4,4,4]
count = 0
for i in arr:
    if i == 4:
        count += 1
print(count)

#1.23) 
str = input('Nhập chuỗi muốn copy: ')
lenString = 2
n = int(input('Nhập n: '))
if len(str) >= lenString:
    print(str[:2]*n)
else:
    print(str*n)

#1.24) 
vowel = 'aeiou'
letter = input('Nhập ký tự muốn ktra: ')
if letter in vowel:
    print('True')
else:
    print('False')

#1.25) 
list = [1, 5, 8, 3]
n = int(input('Nhập n muốn kiểm tra: '))
if n in list:
    print('True')
else:
    print('False')
    
#a+b
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
sum = "a + b: {s}".format(s = a + b)
print(sum)

#a/b
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
kq = "a / b: {s}".format(s = a / b)
print(kq)

#a^b
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
kq = "a ^ b: {s}".format(s = a ** b)
print(kq)

#Diện tích hình chữ nhật
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
kq = "a ^ b: {s}".format(s = a * b)
print(kq)

#3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
n = int(input('Nhập n: '))
for num in range(2,n+1):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)

#5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy) 
#Dùng đệ quy
n = int(input('Nhập n: '))
def check_Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return check_Fibonacci(n-1) + check_Fibonacci(n-2)
print('F({}) = {}'.format(n,check_Fibonacci(n)))

#6. Tính tổng n số Fibonacci đầu tiên
#Dùng đệ quy
def sum(n) :
	f =[0] * (n+1)
	f[1] = 1
	sum = f[0] + f[1]
	for i in range(2,n+1) :
		f[i] = f[i-1] + f[i-2]
		sum = sum + f[i]	
	return sum
n = int(input('Nhập n: '))
print("Tổng n số Fibonacci đầu tiên là: {}".format(sum(n)))

#7 Tính tổng căn bậc 2 của n số nguyên đầu tiên 
import math 
n = int(input('Nhập n: '))
def tinhTong():
    sum = 0
    for i in range(1, n+1):
        sum += math.sqrt(i)
    return sum
print('Tổng là: {}'.format(tinhTong()))

#8 Giải phương trình bậc 2: ax2 + bx + c=0
import math

def giaiPT(a, b, c):
	delta = b * b - 4 * a * c
	
	if delta > 0:
		print('x1 = ', (-b + math.sqrt(abs(delta)))/(2 * a))
		print('x2 = ', (-b - math.sqrt(abs(delta)))/(2 * a))
	
	elif delta == 0:
		print('x1 = x2 = ', -b / (2 * a))
	
	else:
		print(- b / (2 * a), " + i", math.sqrt(abs(delta)))
		print(- b / (2 * a), " - i", math.sqrt(abs(delta)))

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))

if a == 0:
		print("Vui lòng nhập a khác 0!")
else:
	giaiPT(a, b, c)

#10 In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
n = int(input("Nhập vào số cột: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or i == n or j == i:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()
    
#9 Tính n!
n = int(input('Nhập n:'))
def tinhGiaiThua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt
tinhGiaiThua(n)

#11 Đổi giờ - phút – giây
seconds = float(input('Nhập vào số giây: '))
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print('%d:%d:%d'%(hour,minutes,seconds))

#12. Cho một mảng số nguyên: (nên viết 2-3 cách) 
#a) Xuất tất cả các số lẻ không chia hết cho 5
array = [1,2,3,4,5,6,7,8,9,10,55]
for i in range(len(array)):
    if array[i] % 2 != 0 and array[i] % 5 != 0:
        print(array[i], end=" ")

#c) Tìm số nguyên tố lớn nhất 
arr = [1,2,3,4,5,6,7,8,9,10,55]
newList = []
for num in arr: 
 if num > 1: 
   for i in range(2,num): 
     if (num % i) == 0: 
       break 
   else: 
    newList.append(num)
print('List prime number: ', newList)
print('Max number: ', max(newList))

#e) Tính trung bình các số lẻ 
array = [1,2,3,4,5,6,7,8,9,10,55]
sum = 0
count = 0
for i in range(len(array)):
    if array[i] % 2 != 0:
        sum += array[i]
        count += 1
avg = sum / count
print(avg)

#f Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng 
array = [1,2,3,4,5,6,7,8,9,10,55]
tich = 1
for i in range(len(array)):
    if array[i] % 2 != 0 and array[i] % 3 != 0:
        tich *= array[i] 
print(tich)

#g Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
array = [1,2,3,4,5,6,7,8,9,10,55]
vitri1 = int(input('Nhập vị trí 1: '))
vitri2 = int(input('Nhập vị trí 2: '))
array[vitri1], array[vitri2] = array[vitri2], array[vitri1]
print(array)

#h) Đảo ngược trật tự các phần tử của danh sách 
array = [1,2,3,4,5,6,7,8,9,10,55]
array = array[::-1]
print(array)

#i) Xuất tất cả các số lớn thứ nhì của danh sách 
array = [1,2,3,4,5,6,7,8,9,10,55,55,2,3]

#Xóa các phần tử giống nhau
array2 = list(set(array))

#Sắp xếp từ nhỏ đến lớn
array2.sort()
print(array2[-2])

#j) Tính tổng các chữ số của tất cả các số trong danh sách 
array = [1,2,3,4,5,6,7,8,9,10,55,55,2,3]
new_array = []
for i in array:
    sum = 0
    #Duyệt các phần tử trong số ví dụ 55 => 5,5
    for d in str(i):
        sum += int(d)
    new_array.append(sum)
print(new_array)

#k) Đếm số lần xuất hiện của một số trong danh sách 
array = [1,2,3,4,5,6,7,8,9,10,55,55,2,3]
print('Danh sách: ',array)
n = int(input('Nhập số muốn đếm: '))
count = 0
for i in array:
    if(i == n):
        count += 1
print('{} xuất hiện {} lần'.format(n,count))

#l) Xuất các số xuất hiện n lần trong danh sách 
array = [1,2,3,4,5,6,7,8,9,10,22,22,2,3]
for i in set(array):
    c = array.count(i)
    print(f'{i} xuất hiện {c} lần')

#m) Xuất các số xuất hiện nhiều lần nhất trong danh sách
array = [1,2,3,4,5,6,7,8,9,10,22,22,2,3]
a = max(set(array), key = array.count)
print(a)