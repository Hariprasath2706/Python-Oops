class IplWatcher:
    def __init__(self, Tv, mobile, stadium):
        print("This is the constructor!")
        self.Tv = Tv
        self.mobile = mobile
        self.stadium = stadium
    def __del__(self):
        print("Destructor is called. Object is deleted!")
Ipl1 = IplWatcher("Star Sports", "JioHotstar", 40000)
print("TV Channel:", Ipl1.Tv)
print("Mobile:", Ipl1.mobile)
print("Stadium:", Ipl1.stadium)
del Ipl1.stadium
print("\nAfter deleting 'stadium':")
print("TV Channel:", Ipl1.Tv)
print("Mobile:", Ipl1.mobile)
