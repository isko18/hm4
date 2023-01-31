class Pop:
    def __init__(self,name) -> None:
        self.name = name
class Bop:
    def __init__(self,age) -> None:
        self.age = age
class Vop:
    def a():
        pass
class Top:
    def b():
        pass
class Cop(Pop,Bop,Vop,Top):
    def __init__(self, name,age) -> None:
        Pop.__init__(self,name)
        Bop.__init__(self,age)
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
isko = Isko("Islam",18)
print(isko)
