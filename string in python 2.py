row_1 = '+ {:-<13} + {:-^15} + {:->10} +'.format('','','')
row_2 = '| {:^13} | {:^15} | {:^10} |'.format('Họ và tên','Ngay sinh','Gioi tinh')
row_5 = '+ {:-<44} +'.format('')
row_3 = '| {:<13} | {:^15} | {:^10} |'.format('Le Nguyen Anh','11/12/2001','Nam')
row_4 = '+ {:-<13} + {:-^15} + {:->10} +'.format('','','')
print(row_1)
print(row_2)
print(row_5)
print(row_3)
print(row_4)

s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
a = s.strip('a' 'A' 'o').capitalize() + "o"
print(a)