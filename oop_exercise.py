class Trinagle:
    def __init__(self,base,height):
        self.base = base
        self.height =height

    def calculate_area(self):
        Area = 0.5*self.base*self.height
        print("Area",Area)

t1 =Trinagle(10,23)
t1.calculate_area()
t2 =Trinagle(10,33)
t2.calculate_area()
    

