class IplWatcher:
    Tv = "Star Sports"
class Sports(IplWatcher):
    Team = "Cricket"
class Kitbag(IplWatcher):
    items = ("Gloves", "Pad")
sports1 = Sports()
kit1 = Kitbag()
print(sports1.Tv)
print(sports1.Team)
print(kit1.items)
