### function can be nested, when i need to call function inside a function
### i can write this:

class civileng1:
    def __init__(self,age2):
        self.age=age2
    def calc(self):
        def ansys(): ###we do not need 'self' inside
            print "civil engineer gives you an ansys result"
        ansys()  #<-----call the inner func in outer func

civ=civileng1(age2)
civ.calc()   #<------call function calc()

#it will print ->"civil engineer gives you an ansys result"

#also i can write in this way:
class civileng2:
    def __init__(self,age2):
        self.age=age2
        def calc(self):
            def ansys(): ###we do not need 'self' inside
                print "civil engineer gives you an ansys result"
            return ansys #<-----we can also return the 'tag' of inner func to call inner func
civ=civileng2(age2)
civ.calc()()  #<------attention! we should write two quotes here
#also print ->"civil engineer gives you an ansys result"

######wrong way!!! #######
class civileng3:
    def __init__(self,age2):
        self.age=age2
        def calc(self):
            def ansys():
                print "civil engineer gives you an ansys result"
            return OK #<----return a int without calling inner func
civ=civileng3(age2)
civ.calc()()  #<------then it is impossible to call inner func\

              #that's because civileng3 is infact an architect and he knows nothing about structure\
              #he can not use ANSYS but he just pretend that he can\
              #he said 'OK' to you, but before the ddl he will deceive you that something is wrong...

              #system will report error: "int is not callable"



    
