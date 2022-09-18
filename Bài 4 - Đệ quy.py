def giai_thua(n):
	s = 1
	for i in range(1, n + 1):
		s *= i
	return s
n = int(input('Nhập n: '))
print(giai_thua(n))
print("a")