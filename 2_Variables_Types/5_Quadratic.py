"""
Here is a mini project for your practice.

Quadratic Formula is used to find the solutions (roots) of a quadratic equation.
A quadratic equation is any equation in the form: ax**2+bx+c=0
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)