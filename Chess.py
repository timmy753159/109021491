class Chess:
    def __init__(self, name, gender, profession, aaa, skill):
        self.studName = name
        self.studGender = gender
        self.studProfession = profession
        self.studFrom = aaa
        self.studSkill = skill
    
    def showInfo(self):
        print(self.studName)
        print(self.studGender)
        print(self.studProfession)
        print(self.studFrom)
        print(self.studSkill)




x = Chess("紅色","國王","皇后","主教","騎士")
y = Chess("黃色","將","象","士","馬")
z = Chess("綠色","帥","相","仕","马")


print(x.studName, "\t", x.studGender, "\t", x.studProfession, "\t", x.studFrom, "\t", x.studSkill)
print(y.studName, "\t", y.studGender, "\t", y.studProfession, "\t", y.studFrom, "\t", y.studSkill)
print(z.studName, "\t", z.studGender, "\t", z.studProfession, "\t", z.studFrom, "\t", z.studSkill)


x.showInfo()
y.showInfo()
z.showInfo()