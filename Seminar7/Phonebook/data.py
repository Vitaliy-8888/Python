def get_surname():                         
    sn = input('Введите фамилию: ')
    if sn.isalpha():  # isalpha() - выдаст ошибку, если ввели: число, знаки, символы и т.д.
        return sn
    else:
        print('Введены неверные данные') 
      

def get_name():                           
    n = input('Введите имя: ')
    if n.isalpha():    
        return n
    else:
        print('Введены неверные данные') 
    

def get_phone():                         
    ph = input('Введите номер телефона без разделителей начиная с цифры 8: ')
    if ph.isdigit() and len(ph) == 11:     # isdigit() - выдаст ошибку, если ввели не цифры или количество цифр не равно 11.
        return ph
    else:
        print('Введены неверные данные')  
    

def get_description():                    
    des = input('Введите описание: ')
    if des.isalpha():  
        return des
    else:
        print('Введены неверные данные') 
    