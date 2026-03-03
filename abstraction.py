from abc import ABC, abstractmethod

class Match(ABC):
    @abstractmethod
    def commentry(self):
        pass

    @abstractmethod
    def dressingroom(self):
        pass

    @abstractmethod
    def audience(self):
        pass
    
class IplMatch(Match):
    def commentry(self):
        print("The commentry is in Tamil")

    def dressingroom(self):
        print("The dressing room is good")

    def audience(self):
        print("The audience is more than we expected")
        
ipl = IplMatch()
ipl.commentry()
ipl.dressingroom()
ipl.audience()

ipl2 = IplMatch()
ipl2.commentry = "The commentry is in English"
ipl2.dressingroom = "The dressing room is too good"
ipl2.audience = "The audience is less than we epected"
print(ipl2.commentry)
print(ipl2.dressingroom)
print(ipl2.audience)
