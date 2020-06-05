# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:30:02 2019

@author: pythor
"""

#class Square():
#    'Square class for area and perimeter'
#    def __init__(self,a=0):
#        self.a=a
#    def s_area(self):
#        return self.a**2
#    def s_perimeter(self):
#        return self.a*4
#    def s_set(self,a):
#        self.a=a
#    def s_get(self):
#        return self.a

#x=Square()
#n=int(input('enter the time to find are & perimeter of sqaure: '))
#for i in range(n):
#    a=int(input('enter the side of square: '))
#    x.s_set(a)
#    print('square side: ',x.s_get())
#    print('square area: ',x.s_area())
#    print('square perimeter: ',x.s_perimeter())

##print('square area: ',x.s_area())
#print('square perimeter: ',x.s_perimeter())
#print('square side: ',x.s_get())
#x.s_set(a)
#print('square side: ',x.s_get())
#print('square area: ',x.s_area())
#x.s_set(10)
#print('square side: ',x.s_get())
#print('square area: ',x.s_area())

#class Circle():
#    'class circle for area and perimeter'
#    pi=3.14
#    def __init__(self,radius=0):
#        self.radius=radius    
#    def c_set(self,radius):
#        self.radius=radius    
#    def c_get(self):
#        return self.radius
#    def c_area(self):
#        v=Circle.pi * self.radius * self.radius
#        return v
#    def c_perimeter(self):
#        return 2 * Circle.pi * self.radius
#    def abc(self,code):
#        self.code=code
#        return self.code

#y=Circle()
#print('Radius of Circle: ',y.c_get())
#print('Circle Area: ',y.c_area())
#print('Circle Perimeter: ',y.c_perimeter())
##
#class Cube():
#    'class cube for total surface area, vol., csa'
#    def __init__(self,edge=0):
#        self.edge=edge
#    def cube_set(self,edge):
#        self.edge=edge
#    def cube_get(self):
#        return self.edge
#    def cube_tsa(self):
#        return 6 * (self.edge ** 2)
#    def cube_csa(self):
#        return 4* (self.edge**2)
#    def cube_vol(self):
#        return self.edge**3

#z=Cube()
#z.cube_set(5)
#print('Total Surface Area: ',z.cube_tsa())
#print('Curved Surface Area: ',z.cube_csa())
#print('Vol. of Cube: ',z.cube_vol())
#print('Edge of cube: ',z.cube_get())
##z.cube_set(7)
###print('Total Surface Area: ',z.cube_tsa())
###print('Curved Surface Area: ',z.cube_csa())
###print('Vol. of Cube: ',z.cube_vol())
###print('Edge of cube: ',z.cube_get())
##
##
#class Rectangle():
#    'Class Rectangle for Area & Perimeter'
#    def __init__(self,rec_len=0,rec_width=0):
#        self.rec_len=rec_len
#        self.rec_width=rec_width
#    def r_set(self,rec_len,rec_width):
#        self.rec_len=rec_len
#        self.rec_width=rec_width
#    def r_get(self):
#        return self.rec_len, self.rec_width
#    def r_area(self):
#        return self.rec_len * self.rec_width
#    def r_perimeter(self):
#        return 2 * (self.rec_len + self.rec_width)
#rec=Rectangle()
#rec.r_set(5,5)
#print('Rectangle: length & width: ',rec.r_get())
#print('Rectangle Area: ',rec.r_area(),'m^2')
#print('Rectangle Perimeter: ',rec.r_perimeter())
#
#class Shapes(Rectangle,Square,Circle,Cube):
#    def __init__(self):
#        Rectangle.__init__(self)
#        Square.__init__(self)
#        Cube.__init__(self)
#        Circle.__init__(self)
#        print('Shapes Constructor Inherit\'s the classes')
#
#alpha=Shapes()
#alpha.s_set(5)
#print('area sq: ',alpha.s_area())
#print('perimeter sq: ',alpha.s_perimeter())
#print('get side sq:',alpha.s_get())
#
#alpha.s_set(10)
#print('area sq: ',alpha.s_area())
#print('perimeter sq: ',alpha.s_perimeter())
#print('get side sq:',alpha.s_get())
#alpha.r_set(3,4)
#print(alpha.r_area())
#print(alpha.r_get())
#alpha.r_set(5,8)
#print(alpha.r_area())
#print(alpha.r_get())

#n=int(input('enter the times to find cube details: '))
#for i in range(n):
#    a=int(input('enter the edge of cube: '))
#    alpha.cube_set(a)
#    print('Cube edge: ',alpha.cube_get())
#    print('Cube Area: ',alpha.cube_csa())
#    print('Cube Total Surface Area: ',alpha.cube_tsa())
#    print('Cube Volume: ',alpha.cube_vol())
#
#
#alpha.cube_set(10)
#print('Cube edge: ',alpha.cube_get())
#print('Cube Area: ',alpha.cube_csa())
#print('Cube Total Surface Area: ',alpha.cube_tsa())
#
#
#
#
#alpha.s_set(7)
#print(alpha.s_area())
#alpha.cube_set(10)
#print(alpha.cube_csa())
#
#
#alpha.r_set(6,7)
#print('Rec_Area',alpha.r_area())
#print(alpha.r_perimeter())
#
#alpha.r_set(6,9)
#print(alpha.r_area())
#print(alpha.r_perimeter())


#alpha.r_set(rec_len=4,rec_width=5)
#print(alpha.r_get())
#print(alpha.r_area())
#alpha.s_set(5)
#print(alpha.s_area())
#print(alpha.abc(123))
#alpha.s_set(7)
#print(alpha.s_area())
#alpha.c_set(7)
#print('Area of Circle: ',alpha.c_area())
#alpha.cube_set(5)
#print('Cube Vol.: ',alpha.cube_vol())



'''
Multi-Level Inheritance
'''

class Pets():
#    dogs=[]
#    print(len(dogs))
    def __init__(self,dogs):
        self.dogs=dogs

class Dog():
    species='mammal'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.is_hungry=True

    def description(self):
        return self.name,self.age

#    def speak(self,sound):
#        return '% says %'%(self.name,sound)

    def eat(self):
        self.is_hungry=False

class Pug(Dog):
    def run(self):
        return "runs:",(self.name)

class Bulldog(Dog):
    def run(self):
        return "runs:",(self.name)

my_dogs=[Bulldog("Tom",6),Pug('Fletcher',7),Dog('Larry',9)]
my_pets=Pets(my_dogs)
print('I have {} dogs.'.format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name,dog.age))
print('And they are all {}s, of course.'.format(dog.species))

are_my_dogs_hungry=False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry=True

if are_my_dogs_hungry:
    print('My dogs are hungry.')
else:
    print('My dogs are not hungry.')




#a=7
#b=5
#c=a+b
#print('the sum of {} & {} is {}'.format(a,b,c))