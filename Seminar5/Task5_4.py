# Задача 5_4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file5_4.txt', 'r') as file:          # откываем файл и получаем исходные данные 
    tekst = file.readline()                    


def compress_data(tekst):                   # функция зжатия данных
    result_compress = ''                    
    count = 1
    for i in range(len(tekst)-1):           # проходим по длине текста 
        if tekst[i] == tekst[i+1]:          
            count += 1                      
        else:
            result_compress += str(count) + tekst[i]     # добавляем элементы в строку
            count = 1
    if count > 1 or (tekst[len(tekst)-2] != tekst[-1]):     # если предпоследний элемент не равен последнему
        result_compress += str(count) + tekst[-1]           
    return result_compress


def decompress_data(tekst):			    # функция восстановления данных
    number  = ''                        
    result_decompress = ''			   
    for i in range(len(tekst)):         # проходим по длине текста
        if tekst[i].isdigit():          # проверяем, если элемент это цифра 
            number += tekst[i]          
        else:
            result_decompress += tekst[i] * int(number)     #  умножаем элемент на число и добавляем в строку
            number  = ''                   
    return  result_decompress


with open('compress_data.txt', 'w') as file:        # записываме в файл сжатые данные
    file.write(f'{compress_data(tekst)}')

with open('decompress_data', 'w') as file:          # записываме в файл восстановление данные
    file.write(f'{decompress_data(compress_data(tekst))}')


print(f"Сжатые данные: {compress_data(tekst)}")
print(f"Восстановленнные данные: {decompress_data(compress_data(tekst))}")


