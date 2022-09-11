# def my_generator():
#     count=0
#     for a in range(5):
#         yield count+a
#         count+=1


# for a in my_generator():
#     print(a)
# print(list(my_generator()))
# a = my_generator()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

class Employees():
    index = 0
    employees = list()
    def __init__(self,*args):
        self.employees = args
    def __add__(self,other):
        temp = []
        for index in range(len(other)):
            temp.append(next(self)+' ' +next(other))
        self.index = 0
        other.index = 0
        return Employees(*temp)

    def __len__(self):
        return len(self.employees)
    def __next__(self):
        if self.index < len(self.employees):
            self.index +=1
            return self.employees[self.index-1]
        else:
            raise StopIteration
    def __iter__(self):
       return self

objs = Employees('mohammed','ahmed','saeed','salah')
objs1 = Employees('ahmed','saeed','salah','ali')
objs3 = objs+objs1
for obj in objs3:
    print(obj)
# print(next(objs))
# print(objs.index)
# print(next(objs))
# print(objs.index)
# print(next(objs))
# print(objs.index)


    
