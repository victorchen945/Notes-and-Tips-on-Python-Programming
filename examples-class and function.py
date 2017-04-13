OK=0
age1=40
age2=28

class architect:
    def __init__(self,age1):
        self.age=age1
    def draw(self):
        def ps(self):
            print "architect provides you a rendering"
            return OK
    def model(self):
        def skp(self):
            print "architect gives you a sketchup model"
            return OK
    def callhelp(self):
        civil=civileng()
        print civil.age, "year old civil engineer comes"

class civileng:
    def __init__(self,age2):
        self.age=age2
    def draw(self):
        def cad(self):
            print "civil engineer provides you an engineering drawing"
        return cad
    def calc(self):
        def ansys():
            print "civil engineer gives you an ansys result"
        return ansys
    def callhelp(self):
        global age1
        arch=architect(age1)
        print arch.age, "year old architect comes"
        arch.draw()

def calc():
    def ansys():
        print "civil engineer gives you an ansys result"
    return OK

civ=civileng(age2)
civ.calc()()
civ.callhelp()
    