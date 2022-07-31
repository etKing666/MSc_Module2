# Demonstration of exception handling by Body Mass Index (BMI) calculation

print("""Body Mass Index (BMI) Calculation
Note: Please use metric system.""")

try:
    # Because inputs are always string, we are typecasting them to int:
    weight = float(input("Please enter your weight (kg): "))
    height = float(input("Please enter your height (m): "))
    BMI = weight / (height ** 2)

except ValueError:
    print("Please enter a valid value.")

except (TypeError, ZeroDivisionError):
    print("Please enter a correct type of value and do not enter zero(0).")

except:
    print("An error occured. Please try again.")

if BMI > 25.0:
    print(f"Your BMI is {BMI} and you are overweight.")
elif BMI <= 24.9 and BMI >= 18.5:
    print(f"Your BMI is {BMI} and your weight is normal!")
else:
    print(f"Your BMI is {BMI} and you are underweight.")
