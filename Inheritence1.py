class Father:
    hair_color = "Black"
class Mother:
    eye_color = "Brown"
class Child(Father, Mother):
    hands = 2
child1 = Child()
print(child1.hands)
print(child1.hair_color)
print(child1.eye_color)
