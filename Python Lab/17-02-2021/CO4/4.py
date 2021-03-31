class Time:
    def __init__(self,hh=0,mm=0,ss=0):
        self.__hour=hh
        self.__minute=mm
        self.__second=ss
    def __add__(self,other):
        second=int((self.__second + other.__second)%60)
        minute=int((self.__minute + other.__minute)%60 + ((self.__second + other.__second)/60))
        hour=int((self.__hour + other.__hour)%24 + (self.__minute + other.__minute)/60)
        print('Time[hh:mm:ss] ',hour,':',minute,':',second)
T1=Time(12,25,45)
T2=Time(16,45,56)
T1 + T2