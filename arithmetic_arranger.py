def arithmetic_arranger(problems, solved=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  op = [i.split(" ")[1] for i in problems]
  if "*" in op or "/" in op:
    return "Error: Operator must be '+' or '-'."
  a1 = [i.split(" ")[0] for i in problems]
  a2 = [i.split(" ")[2] for i in problems]
  for i in a1:
    try:
      int(i)
    except:
      return "Error: Numbers must only contain digits."
    if len(i) > 4:
      return "Error: Numbers cannot be more than four digits."
  for i in a2:
    try:
      test = int(i)
    except:
      return "Error: Numbers must only contain digits."
    if len(i) > 4:
      return "Error: Numbers cannot be more than four digits."
      
  answer = ""
  
  for i in range(len(problems)):
    if len(a1[i]) < len(a2[i]):
      answer += (" " * abs(len(a1[i])-len(a2[i])))
    answer += ("  ")
      
    answer += (a1[i] + "    ")
    
  answer += "\n"
  for i in range(len(problems)):
    answer += (op[i] + " ")

    if len(a1[i]) > len(a2[i]):
      answer += (" " * abs(len(a1[i])-len(a2[i])))
    
    answer += (a2[i] + "    ")
    
  answer += "\n"
  for i in range(len(problems)):
    answer += ("-" * (max(len(a1[i]), len(a2[i])) + 2) + "    ")
  answer += "\n"

  if solved:
    solutions = [eval(problems[i]) for i in range(len(problems))]
    for i in range(len(problems)):
      answer += (" " * (max(len(a1[i]), len(a2[i])) + 2 - len(str(solutions[i]))))
      answer += (str(solutions[i]) + "    ")
  return answer

# print version:
# def arithmetic_arranger(problems, solved=False):
#   if len(problems) > 5:
#     return "Error: Too many problems."
#   op = [i.split(" ")[1] for i in problems]
#   if "*" in op or "/" in op:
#     return "Error: Operator must be '+' or '-'."
#   a1 = [i.split(" ")[0] for i in problems]
#   a2 = [i.split(" ")[2] for i in problems]
#   for i in a1:
#     try:
#       int(i)
#     except:
#       return "Error: Numbers must only contain digits."
#     if len(i) > 4:
#       return "Error: Numbers cannot be more than four digits."
#   for i in a2:
#     try:
#       test = int(i)
#     except:
#       return "Error: Numbers must only contain digits."
#     if len(i) > 4:
#       return "Error: Numbers cannot be more than four digits."
  
#   for i in range(len(problems)):
#     if len(a1[i]) < len(a2[i]):
#       print(" " * abs(len(a1[i])-len(a2[i])), end="")
#     print("  ", end="")
      
#     print(a1[i], end="    ")
    
#   print()
#   for i in range(len(problems)):
#     print(op[i] + " ", end="")

#     if len(a1[i]) > len(a2[i]):
#       print(" " * abs(len(a1[i])-len(a2[i])), end="")
    
#     print(a2[i], end="    ")
    
#   print()
#   for i in range(len(problems)):
#     print("-" * (max(len(a1[i]), len(a2[i])) + 2), end="    ")
#   print()

#   if solved:
#     solutions = [eval(problems[i]) for i in range(len(problems))]
#     for i in range(len(problems)):
#       print(" " * (max(len(a1[i]), len(a2[i])) + 2 - len(str(solutions[i]))), end="")
#       print(solutions[i], end="    ")
#   print()
#   return