# Tests don't pass only because of withspaces differences

from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["34 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["4 + 23"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# Run unit tests automatically
# main()
