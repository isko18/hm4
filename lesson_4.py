# множественное 

# class Учитель:
#     def учить(self)

# class Строитель:
#     def строить

# class Ученик(Учитель, Строитель):...

# c = Ученик
# c.учить()
# c.строить()

# class A:
#     def __init__(self, s) -> None:
#         self.s = s
#     def a(self = 1):
#         print(A)

# class B(A):
#     def a(self = 1):
#         print(B)

# class C(B):
#     def a(self = 1):
#         print(C)
    
# a = C("s")
# a.a()
# print(C.__mro__)


# class A:
#     ...

# class B(A):...

# class C(A):...

# class D(C,B):...

# class A:
#     def __init__(self, name):
#         self.name = name
#         print("run A")


# class B:
#     def __init__(self, age) -> None:
#         super
#         self.age = age

#     def run(self):
#         print("run B")

# class C(A,B):
#     def __init__(self, name, age):
#         A.__init__(self,name)
#         B.__init__(self,age)


# a = C("namr=e")


class O: ... 

class A(O): ... 

class B(O): ... 

class C(O): ... 

class D(O): ... 

class E(O): ... 
 
class K1(A, B, C): ... 

class K2(B, D): ... 

class K3(C, D, E): ... 
 
class Z(K1, K2, K3): ...


