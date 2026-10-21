message = [
"Уважаемый гость, ",
"ваша бронь №", "948311", " успешно подтверждена.",
" Категория номера: ", "Стандарт,", " Улучшенный,", " На двоих.",
" Дата заезда: ", "14 октября", ".",
" Ждём вас! ",
]
def msg_concat():
    return (message[0] + message[1] + message[2] + message[3] + message[4] + message[5] + message[6] + message[7] + message[8] + message[9] + message[10])
print(msg_concat())
def msg_format():
    return ("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}"
        .format(*message))
def msg_fstring():
    return (f"{message[0]}{message[1]}{message[2]}{message[3]}{message[4]}{message[5]}{message[6]}{message[7]}{message[8]}{message[9]}{message[10]}")
repeats = 100_000
timeit_concat = timeit.timeit(msg_concat, number=repeats)
timeit_format = timeit.timeit(msg_format, number=repeats)
timeit_fstring = timeit.timeit(msg_fstring, number=repeats)
print("\nПри 100.000 повторов:")
print(f"Конкатенация: {timeit_concat:.3f} с")
print(f".format(): {timeit_format:.3f} с")
print(f"f-строка: {timeit_fstring:.3f} с")
print(f"\nformat медленнее f-строки в {timeit_format / timeit_fstring:.2f} раз")
