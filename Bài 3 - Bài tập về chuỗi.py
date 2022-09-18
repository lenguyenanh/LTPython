#a) Đảo ngược 1 chuỗi, s="hello" -> olleh
s = 'hello'
a = s[::-1]
print(a)

#b)Đảo ngược các từ trong chuỗi "how are you"-> "you are how"
s = "how are you".split()
s.reverse()
s = ' '.join(s)
print(s)

#c) Kiểm tra 1 chuỗi có đối xứng hay k?
s = 'abceeecba'
if s[::-1] == s:
	print("Có đối xứng")
else:
	print("KO đối xứng")

