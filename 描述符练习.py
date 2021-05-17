"""
class TempC:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance,value)
    def __delete__(self, instance):
        self.fdel(instance)

class Temperature:
    def __init__(self):
        self._tempf = None
    def gettemp(self):
        return self._tempf
    def settemp(self,value):
        self._tempf = (value*1.3+32)
    def deltemp(self):
        del self._tempf
    x = TempC(gettemp,settemp,deltemp)

c = Temperature()
c.x = 6
print(c._tempf)
print(c.x)
"""                                      #描述符
'''class TempC:
    def __init__(self,value = 10):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        del self.value
class TempF:
    def __init__(self, value=5):
        self.value = value

    def __get__(self, instance, owner):
        return instance.c*1.8+32

    def __set__(self, instance, value):
        instance.c = (value-32) /1.8

    def __delete__(self, instance):
        del self.value

class Temp:
    c = TempC()
    f = TempF()

a = Temp()
#a.c = 20
print(a.f)
#a.f = 57
print(a.c)'''



'''class Mylist:                                    #定制列表
    def __init__(self,*args):
        self.value = [x for x in args]
        self.count = {}.fromkeys(range(len(args)),0)
    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        self.count[item] +=1
        return self.value[item]

a = Mylist(1,2,3,4,5)
print(a[1])
print(a[1])
print(a[1])
print(a.count)
'''
'''class Mytransformlist:                                    #定制列表
    def __init__(self,*args):
        self.value = [x for x in args]
        self.count = {}.fromkeys(range(len(self.value)),0)#[0 for x in args]
    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        self.count[item] +=1
        return self.value[item]
    def __set__(self, instance, value):
        self.value[value]=value
    def __delitem__(self, key):
        del self.value[key]
        self.count.pop(key)

a = Mytransformlist(1,3,5,5,9)
print(a.value)
print(a[1])
print(a[1])
print(a[3])
print(a.count)
del a[0]
#del a[0]
#a[1] = 666
print(a.count)
print(a[0])
print(a.value)'''


def fibs (value):
    a = 0
    b = 1
    while value > a:
        a,b = b,a+b
        yield a
fibss = fibs(20)
for i in fibss:
    print(i)
