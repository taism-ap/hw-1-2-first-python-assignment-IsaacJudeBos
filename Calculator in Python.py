print("Welcome to Isaac's glorious python calcultor!")
x = "Y"
while x == "Y":
  value1 = input("Input the first number you would like to use in your calculation!")
  value2 = input("Input the second number you would like to use in your calculation!")
  function = input("Input the function (+,-,*, or /)")
  if function == "+":
    answer = float(value1) + float(value2)
    float_int = input("Would you like you answer to be rounded to the nearest integer? (Please answer with Y for yes or N for no)")
    if float_int == "Y":
      print(int(answer))
    else:
      print(answer)
  elif function == "-":
    answer = float(value1) - float(value2)
    float_int = input("Would you like you answer to be rounded to the nearest integer? (Please answer with Y for yes or N for no)")
    if float_int == "Y":
      print(int(answer))
    else:
      print(answer)
  elif function == "*":
    answer = float(value1) * float(value2)
    float_int = input("Would you like you answer to be rounded to the nearest integer? (Please answer with Y for yes or N for no)")
    if float_int == "Y":
      print(int(answer))
    else:
      print(answer)
  elif function == "/":
    answer = float(value1) / float(value2)
    float_int = input("Would you like you answer to be rounded to the nearest integer? (Please answer with Y for yes or N for no)")
    if float_int == "Y":
      print(int(answer))
    else:
      print(answer)
  else:
    print("You failed to input an actual opertion!")
  x = input("Would you like to continue calculating? (Please answer with Y for yes or N for no)")
print ("Thank you for using Isaac's Python calculator of glory!")
