prime = " SIx sEVeN "
print(f"Первоначальная строка: '{prime}', id: {id(prime)}\n")
striped = prime.strip()
print(f"После .strip(): '{striped}', id: {id(striped)}\n")
lowered = striped.lower()
print(f"После .lower(): '{lowered}', id: {id(lowered)}\n")
replaced = lowered.replace(" ", "_")
print(f"После .replace(): '{replaced}', id: {id(replaced)}\n")
print(f"Проверка неизменности первоначальной строки: '{prime}', id: {id(prime)}\n")
