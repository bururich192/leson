from math import sqrt


class Triangle():
    def __init__(self,x,y,x1,y1,x2,y2):
        self.x=x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def per(self):
        self.a=sqrt((self.x - self.x1)**2 +(self.y - self.y1)**2)
        self.b=sqrt((self.x - self.x2)**2 +(self.y - self.y2)**2)
        self.c=sqrt((self.x1 - self.x2)**2 +(self.y1 - self.y2)**2)
        p=self.a+self.b+self.c
        return p
    def sqr(self):
        p=0.5*self.per()
        s=sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
tri=Triangle(int(input("Введите x")),int(input("Введите y")),int(input("Введите x1")),int(input("Введите y1")),int(input("Введите x2")),int(input("Введите y2")))
print(tri.per())
print(tri.sqr())
#Строка это вход а столб это нейрон