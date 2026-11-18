

def is_armstrong_number(number):
    str_num = str(number)
    k = len(str_num)
    
    suma = sum(int(digito) ** k  for digito in str_num)
    
    return suma == number