class Student():
    name =  "heng"
    age = 20
    def Stu(self):
        self.name = 'aa'
        self.age = 18
        print('我叫{0}'.format(self.name))
        print('我今年{0}'.format(self.age))
yueyue = Student()
print(yueyue.age)
yueyue.Stu()
print(yueyue.age)
