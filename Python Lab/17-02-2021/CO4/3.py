class Rectangle:
    def __init__(self,l,w):
        self.__length = l
        self.__width = w
        self.area=self.__width * self.__length
    def __lt__(self, other):
        if self.area < other.area:
            print('Rectangle with length=',self.__length,'and width=',self.__width,'has the lesser area!')
        elif other.area < self.area:
            print('Rectangle with length=',other.__length,'and width=',other.__width,'has the lesser area!')
        else:
            print('They have equal area!')
l=float(input('Enter length of 1st rectangle: '))
w=float(input('Enter width of 1st rectangle: '))
R1=Rectangle(l,w)
l=float(input('Enter length of 2nd rectangle: '))
w=float(input('Enter width of 2nd rectangle: '))
R2=Rectangle(l,w)
R1<R2