#Phương thức capitalize() trả về chuối có ký tự đầu tiên viết hoa, các ký tự còn lại viết thường
c = 'hello world'.capitalize()
print(c)

#Method upper() trả về chuỗi các ký tự viết hoa
u = 'hello'.upper()
print(u)

#Method lower() trả về chuỗi các ký tự viết thường
l = 'HELLO'.lower()
print(l)

#Method swapcase() trả về chuỗi các ký tự viết hoa thành viết thường, viết thường thành viết hoa
sc = 'HeLlO'.swapcase()
print(sc)

#Method title() Trả về một chuỗi với định dạng tiêu đề, có nghĩa là các từ sẽ được viết hoa chữ cái đầu tiên, còn lại là viết thường
t = "hello world".title()
print(t)

#Method center(width,[fillchar])
c = 'abc'.center(10,'*')
print(c)

t = 'ố ồ'.encode(encoding='utf-8',errors='strict')
print(t)

#Method rjust, ljust
rjust = 'abc'.rjust(12,'*')
print(rjust)
ljust = 'abc'.ljust(12,'*')
print(ljust)

#Method join() List
join = ' '.join(['a','b','c'])
print(join)
#Method join() tuple
join= ' '.join(('a', 'b', 'c'))
print(join)

#Method replace()
replace = 'Hello world'.replace('Hello', 'Hi')
print(replace)
replace = 'Hello world'.replace('Hello', 'Hi', 1)
print(replace)
replace = 'Hello world'.replace('Hello', 'Hi',0)
print(replace)

#Method strip()
strip = '1232abc3231223123'.strip('123')
print(strip)
lstrip = '123321abc123321'.lstrip('123')
print(lstrip)
rstrip = '123321abc123321'.rstrip('123')
print(rstrip)

#Method removeprefix() xóa ký tự đầu chuỗi
removeprefix = 'tttabctttt'.removeprefix('tt')
print(removeprefix)

#Method removesuffix() xóa ký tự cuối chuỗi
removesuffix = 'tttabcttt'.removesuffix('tt')
print(removesuffix)