def main():
  userInput = input("Expression: ")
  num1, operator, num2 = userInput.split(" ")
  num1 = float(num1)
  num2 = float(num2)

  global result

  match operator:
    case "+":
      result = num1 + num2
      # print(f"{result:.1f}")
    case "-":
      result = num1 - num2
      # print(f"{result:.1f}")
    case "*":
      result = num1 * num2
      # print(f"{result:.1f}")
    case "/":
      result = num1 / num2
      # print(f"{result:.1f}")
  print(f"{result:.1f}")

main()