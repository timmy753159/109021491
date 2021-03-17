class Book:
    def __init__(self, name, page, id, aaa, cl):
        self.studName = name
        self.studPage = page
        self.studId = id
        self.studFrom = aaa
        self.studCl = cl
    
    def showInfo(self):
        print(self.studName)
        print(self.studPage)
        print(self.studId)
        print(self.studFrom)
        print(self.studCl)




x = Book("桐人傳","8763","c8763","艾恩格朗特","傳記")
y = Book("雅絲娜使用手冊","763","74147414","艾恩格朗特","工具書")
z = Book("克萊因戰計","1","10101010","艾恩格朗特","白紙")



x.showInfo()
y.showInfo()
z.showInfo()