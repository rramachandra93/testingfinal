class Class:
    def __init__(self,val=1):
        self.__first=val
    def setsecond(self,val):
        self.__second=val

obj1=Class()
obj2=Class(2)
obj2.setsecond(3)
obj3=Class(4)
obj3.__third=7
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
x = '\''
print(len(x))
print(x)
print(ord('a'))
print(chr(120))
print(3 * 'abc' + 'xyz')
print('Mike' > "Mikey")
print(float("1,3"))