import matplotlib.pyplot as plt

'''
# enkel metode
x = [0, 1, 2, 3, 4, 5]
y = [2, 5, 8, 11, 14, 17]

plt.plot(x, y) # oppretter et plott
plt.show() # viser plot, dette gjør vi på to forskjellige linjer slik at vi kan ha flere grafer i samme diagram
'''


x = [0, 1, 2, 3, 4, 5]
y = []

for tall in x:
    y.append(3*tall + 2)

print(x) # printer listene med tallene 
print(y)

plt.scatter(x, y) # oppretter et plott
plt.show() # viser plot, dette gjør vi på to forskjellige linjer slik at vi kan ha flere grafer i samme diagram


'''# annen metode

x = []
y = []

def f(x):
    return 3*x + 2

for i in range(6):
    y.append(i)
    y.append(f(i)) # alt; 3*i + 2

plt.plot(x, y)
plt.show()'''

