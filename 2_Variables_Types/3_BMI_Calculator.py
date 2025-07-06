"""
Here is a mini project for your practice.
BMI(Body Mass Index) Calculator to find whether 
you have a healthy body weight according to your height 🏋️‍♀️"""

weight = float(input("Enter your weight in kilograms: "))       # in kilograms
height = float(input("Enter your height in meters: "))       # in meters

bmi = weight / (height**2)

print(bmi)
