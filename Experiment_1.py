#Числа и строки
x = 676
a = x + x
b = x * 2
c = "Test_1"
d = "_".join(["Test", "1"])
print(a == b, a is b) #Равенство - True, Идентичность - False
print(c == d, c is d) #Равенство - True, Идентичность – False

#None
a = None
b = []
print(a is None) #True
print(b is None) #False
