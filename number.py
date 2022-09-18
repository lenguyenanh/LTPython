a = 7.5
print(a)
print(type(a))

#Lấy toàn bộ thư viện từ decimal
from decimal import*

#Lấy tối đa 30 chữ số phần nguyên và phần số thập phân decimal
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))
d = Decimal(10) / 3
print(d)
print(type(d))

print(3 * '7')