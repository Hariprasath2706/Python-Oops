class IplWatcher:
    def __init__(self, Tv, mobile, stadium):
        self.Tv = Tv
        self.mobile = mobile
        self.stadium = stadium
    def get_Tv(self):
        return self.Tv
    def get_mobile(self):
        return self.mobile
    def get_stadium(self):
        return self.stadium
    def set_Tv(self, Tv):
        self.Tv = Tv
    def set_mobile(self, mobile):
        self.mobile = mobile
    def set_stadium(self, stadium):
        self.stadium = stadium
Ipl1 = IplWatcher("Star Sports Tamil", "Jio Hotstar", 60000)
print("Tv:", Ipl1.get_Tv())
print("Mobile:", Ipl1.get_mobile())
print("Stadium Capacity:", Ipl1.get_stadium())
Ipl1.set_Tv("Sony Sports")
Ipl1.set_mobile("Jio Cinema")
Ipl1.set_stadium(40000)
print("\nAfter update:")
print("Tv:", Ipl1.get_Tv())
print("Mobile:", Ipl1.get_mobile())
print("Stadium Capacity:", Ipl1.get_stadium())
