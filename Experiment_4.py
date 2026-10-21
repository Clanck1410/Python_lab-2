#Число
x = 67
y = 10**14
z = 10**42
sx = sys.getsizeof(x)
sy = sys.getsizeof(y)
sz = sys.getsizeof(z)
print(f"Размер X: {sx}\nРазмер Y: {sy}\nРазмер Z: {sz}")

#Строка
x = 'rofl'
y = 'rooofl'
z = 'rooooooofl'
sx = sys.getsizeof(x)
sy = sys.getsizeof(y)
sz = sys.getsizeof(z)
print(f"Размер X: {sx}\nРазмер Y: {sy}\nРазмер Z: {sz}")
