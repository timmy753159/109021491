class Student:
    def __init__(self, name, id, pp):
        self.studName = name
        self.studId = id
        self.psssss = pp


x = Student("桐人","黑色劍士","艾恩格朗特")
print(x.studName, "\t", x.studId, "\t", x.psssss)
print(Student.__dict__)
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__bases__)



