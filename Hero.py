class Hero:
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




x = Hero("桐人","男性","黑色劍士","艾恩格朗特","星爆氣流斬")
y = Hero("雅絲娜","女性","公車娜","艾恩格朗特","光之劍擊")
z = Hero("克萊因","男性","風林火山會長","艾恩格朗特","無")


print(x.studName, "\t", x.studGender, "\t", x.studProfession, "\t", x.studFrom, "\t", x.studSkill)
print(y.studName, "\t", y.studGender, "\t", y.studProfession, "\t", y.studFrom, "\t", y.studSkill)
print(z.studName, "\t", z.studGender, "\t", z.studProfession, "\t", z.studFrom, "\t", z.studSkill)


x.showInfo()
y.showInfo()
z.showInfo()