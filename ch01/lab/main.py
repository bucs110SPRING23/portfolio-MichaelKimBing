#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 8
cost_per_class = (cost_per_week/classes_per_week)
print("This is how much I spend per class:", cost_per_class)
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B
import random
myrandomlist = [3, "atoms", 9.172, "steak", 5.63, 5, "molecules", 3.14, "parsely", "butter", 19, 828.927320, "salt"]
roulette_of_mystery = random.choice(myrandomlist)
print(roulette_of_mystery)
