class Student:
    def __init__(self, name, gender, id, aaa, cl):
        self.studName = name
        self.studGender = gender
        self.studId = id
        self.studFrom = aaa
        self.studCl = cl
    
    def showInfo(self):
        print(self.studName)
        print(self.studGender)
        print(self.studId)
        print(self.studFrom)
        print(self.studCl)




x = Student("桐人","男性","c8763","艾恩格朗特","星爆系")
y = Student("雅絲娜","女性","74147414","艾恩格朗特","公車系")
z = Student("克萊因","男性","10101010","艾恩格朗特","單身系")



x.showInfo()
y.showInfo()
z.showInfo()