class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def cmp(self,obj):
        if self.area()>obj.area():
            print('Rectangle with length =',self.length,'and breadth =',self.breadth,'has the greater area')
        elif self.area()<obj.area():
            print('Rectangle with length =',obj.length, 'and breadth =', obj.breadth, 'has the greater area')
        else:
            print('They have equal area!')
r1=Rectangle(9,3)
r2=Rectangle(3,4)
r1.cmp(r2)
