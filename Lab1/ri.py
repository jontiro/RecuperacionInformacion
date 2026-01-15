import string
import nltk
import re

nltk.download('punkt_tab')

def main():

    # Carga del archivo txt.
    with open('resources/2591-0.txt', encoding='utf-8', errors= 'ignore') as f:
        raw = f.read()

    # Tokenización y creación del objeto Text.
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    # Imprime las primeras 100 palabras del texto.
    print(text[:100])


    # Eliminacion de puntuación.

    # Puntuaction incluye el apóstrofe especial ’
    punctuation = string.punctuation + "’"
    # Deteccion de caracteres de puntuación usando expresiones regulares.
    re_punc = re.compile('[%s]' % re.escape(punctuation))
    # Eliminación de la puntuación de las palabras del texto.
    stripped = [re_punc.sub('', w) for w in text]
    # Imprime las primeras 100 palabras sin puntuación.
    print(stripped[:100])


    # Conversión a minúsculas.

    # Conversión de palabras a minúsculas.
    # Stripped puede ser reemplazada por text si se
    # desea conservar la puntuación.
    lw_text = [word.lower() for word in stripped]
    # Imprime las primeras 100 palabras en minúsculas.
    print(lw_text[:100])


    # Ejemplo con re.

    # Búsqueda de todas las palabras que contienen 'cat'.
    cat_words_re = re.compile(r'.*cat.*')
    # Filtrado de palabras que coinciden con la expresión regular
    # 'cat' dentro del array de minusculas.
    cat_words = [w for w in lw_text if cat_words_re.match(w)]
    # Imprime las primeras 100 palabras que contienen 'cat'.
    print(cat_words[:100])



if __name__ == '__main__':
        main()

