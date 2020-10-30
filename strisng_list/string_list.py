
start=79900
end=80156
code_list=[]

def postal_codes(start, end):
	for i in range (start, end):
		converted_i = str(i)
		code_list.append(f'{converted_i[:2]}-{converted_i[2:]}')
	return(code_list)

print(postal_codes(start, end))