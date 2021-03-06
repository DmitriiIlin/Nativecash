
class NativeCash():
    def __init__(self,sz):
        self.size=sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits=[0]*self.size

    def hash_fun(self, key):
        # в качестве value поступают строки
        input_string=str(key)
        index=sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))%self.size
        return index
    
    def index_finder(self,key):
        #Вспомогательный метод-находит необходимый индекс
        key=str(key)
        index=self.hash_fun(key)
        count=0
        result=[]
        flag=False
        while self.slots[index]!=str(key):
            if index<self.size-1:
                index+=1
            else:
                index=0
            count+=1
            if count>self.size:
                flag=False
                result.append(index)
                result.append(flag)
                return result 
        if count<=self.size:
            flag=True
        result.append(index)
        result.append(flag)
        return result
        

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        key=str(key)
        result=self.index_finder(key)
        return result[1]
   

    def put(self, key, value):
        # гарантированно записываем 
        # значение value по ключу key
        if None in self.slots and value!=None:
            index=self.hash_fun(key)
            while self.slots[index]!=None:
                if index<self.size-1:
                    index+=1
                else:
                    index=0
            self.slots[index]=str(key)
            self.values[index]=value
        elif None not in self.slots and value!=None:
            index=self.hits.index(min(self.hits))
            self.hits[index]=0
            self.slots[index]=str(key)
            self.values[index]=value
        else:
            pass

    def get(self, key):
        # возвращает value для key, 
        # или None если ключ не найден
        key=str(key)
        if self.is_key(key)==True:
            index=self.index_finder(key)[0]
            self.hits[index]+=1
            data=self.values[index]
            return data
        else:
            return None    
    

"""a=NativeCash(5)
a.put("первый",34)
a.put("второй",4)
a.put("третий",424)
a.put("четвертый",43)
a.put("пятый",24)
print(a.slots)
print(a.values)
print(a.hits)
print(a.get("первый"))
print(a.get("четвертый"))
print(a.get("второй"))
print(a.get("третий"))
print(a.hits)
a.put("замена",999)
print("_______")
print(a.slots)
print(a.values)
print(a.is_key("первый"))
print(a.is_key("пятый"))
print(a.is_key("замена"))"""