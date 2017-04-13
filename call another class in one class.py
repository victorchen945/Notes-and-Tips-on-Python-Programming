###when we need to call one class in another class###

age1=40
age2=39

class architect:
    def __init__(self,age1):
        self.age=age1
    def callhelp(self):
        global age2
        civil=civileng(age2)  ###call class civileng
        print "a ",civil.age, "years old civil engineer comes"

class civileng:
    def __init__(self,age2):
        self.age=age2
    def callhelp(self):
        global age1
        arch=architect(age1)  ###call class architect
        print "a ",arch.age, "years old architect comes"
        arch.draw()

civ=civileng(age2)
civ.callhelp()

""" 
it will print the running result:
a 40 years old architect comes


    
