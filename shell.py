import GenZX as gen

while True:
    command = input("$GenZX >> ")
    result, error = gen.run('<stdin>', command)
    if error: print(error.as_string())
    else: print(result)