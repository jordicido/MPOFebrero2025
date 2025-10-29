import os

def replace_word(path, word_to_replace, new_word):
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")
    if len(word_to_replace) == 0:
        raise ValueError("La palabra a reemplazar no puede ser vacía")

    with open(path, "r") as file:
        text = file.read()
        text = text.replace(word_to_replace, new_word)

    with open(path, "w") as file:
        file.write(text)


path = input("Qué archivo quieres censurar?\n")
word_to_replace = input("Qué palabra quieres censurar?\n")
new_word = input("Por qué palabra quieres sustituirla?\n")

try:
    replace_word(path, word_to_replace, new_word)
except Exception as e:
    print(e)