import data        


def get_abonent():              # добавляем введенные данные в список
    abonent = []
    abonent.append(data.get_surname())
    abonent.append(data.get_name())
    abonent.append(data.get_phone())
    abonent.append(data.get_description())
    return abonent



# print(get_abonent())                  
              
