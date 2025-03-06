#Name: Ryan Pool
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def doubleCost (self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
perfume = Store(100, 40, 10)
lego = Store(200, 60, 40)
blanket = Store(400, 10, 8)

#3. Print the stock of all three objects and the cost of the second store item.
print(f"Stock of perfume: {perfume.stock}")
print(f"Stock of lego: {lego.stock}")
print(f"Stock of blanket: {blanket.stock}")
print(f"The cost of lego: {lego.cost}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
lego.doubleCost()

print(f"The new cost of lego: {lego.cost}")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
blanket.stock = 100
print(f"The new stock of the blanket is: {blanket.stock}")

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del perfume

try:
    print(f"The weight of perfume is: {perfume.weight}")
except:
    print("perfume does not exist")