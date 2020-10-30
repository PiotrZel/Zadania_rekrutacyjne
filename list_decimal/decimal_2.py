from decimal import Decimal

start = 2
end = 5.5
interval = 0.5
d_list=[]

def dec_list(num1, num2, inter): 
    i = Decimal(num1)
    while i < num2:
        i += Decimal(inter)
        d_list.append(i)
    return d_list

print(dec_list(start, end, interval))
