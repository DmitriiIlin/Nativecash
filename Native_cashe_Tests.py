import Native_cashe,unittest,random,string

def string_generator(size=8):
    #Ф-ция генерирует случайную строку длиной size
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def key_data(size=11):
    #Ф-ция создает список случайных строк, количеством size и находит значения хеш функций (index)
    data_output=[]
    data=[]
    hash_data=[]
    for _ in range(0,size):
        key=string_generator()
        data.append(key)
        hash=sum(ord(key[i])**(i+1) for i in range(len(key)))%size
        if hash not in hash_data:
            pass
        else:
            while hash in hash_data:
                if hash<size-1:
                    hash+=1
                else:
                    hash=0
        hash_data.append(hash)
        data.append(hash)
        data_output.append(data)
        data=[]
    return data_output

def key(data,size=11):
    #Возвращает массив данных ключей
    key=[]
    for i in range(0,size):
        key.append(data[i][0])
    return key

def values(data, size=11):
    #Возвращает массив данных value
    values=[]
    for i in range(0,size):
        values.append(data[i][1])
    return values

def conflicts(data,size=11):
    #Генерация кол-ва вызовой ключей
    hits=[0]*size
    data_key=key(data)
    for _ in range(0,size**2):
        hit=random.choice(data_key)
        hits[data_key.index(hit)]+=1
    return hits    


class Native_cashe_Tests(unittest.TestCase):
    #Тесты для Native_cashe

    def test_conflicts(self,size=11):
        #Тест коллизий и проверка схемы вытеснения
        Array_cashe=Native_cashe.NativeCash(size)
        data_for_array_cashe=key_data()
        data_for_array_cashe_conflicts=conflicts(data_for_array_cashe)
        for i in range(size):
            Array_cashe.put(key(data_for_array_cashe)[i],values(data_for_array_cashe)[i])
        for i in range(0,size):
            for j in range(0,data_for_array_cashe_conflicts[i]):
                Array_cashe.get(key(data_for_array_cashe)[i])
        for i in range(0,size):
            self.assertEqual(key(data_for_array_cashe)[i] in Array_cashe.slots, Array_cashe.slots[i] in key(data_for_array_cashe))
            self.assertEqual(values(data_for_array_cashe)[i] in Array_cashe.values, Array_cashe.values[i] in values(data_for_array_cashe)) 
        print(Array_cashe.slots)
        print(Array_cashe.values)
        print(Array_cashe.hits)
        print("-----------------------------------------------")
        key_to_insert=string_generator()
        hash_to_insert=sum(ord(key_to_insert[i])**(i+1) for i in range(len(key_to_insert)))%size
        position_to_replase=min(data_for_array_cashe_conflicts)
        print(position_to_replase)
        print(data_for_array_cashe_conflicts)
        keys=key(data_for_array_cashe)
        val=values(data_for_array_cashe)
        print(keys)
        print(val)
        index=data_for_array_cashe_conflicts.index(position_to_replase)
        print(index)
        new_data=[]
        new_data.append(key_to_insert)
        new_data.append(hash_to_insert)
        data_for_array_cashe[index]=new_data
        print("-----------------------------------------------")
        print(key(data_for_array_cashe))
        print(values(data_for_array_cashe))
        Array_cashe.put(key_to_insert,hash_to_insert)
        for i in range(0,size):
            self.assertEqual(key(data_for_array_cashe)[i] in Array_cashe.slots, Array_cashe.slots[i] in key(data_for_array_cashe))
            self.assertEqual(values(data_for_array_cashe)[i] in Array_cashe.values, Array_cashe.values[i] in values(data_for_array_cashe)) 
    

      



"""Z=key_data()
print(Z)
print(key(Z))
print(values(Z))
a=Native_cashe.NativeCash(11)
for i in range(len(a.slots)):
    a.put(key(Z)[i],values(Z)[i])
print(a.slots)
print(a.values)
print(a.hits)
print(conflicts(Z,11))"""

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()