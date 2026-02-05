import string
import nltk
import re

from nltk import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer


# Descarga del paquete punkt_tab para tokenización.
nltk.download('punkt_tab')
# Descarga de WordNet para lematización.
nltk.download('wordnet')

def main():

    # Carga del archivo txt.
    with open('resources/2591-0.txt', encoding='utf-8', errors= 'ignore') as f:
        raw = f.read()

    # Tokenización y creación del objeto Text.
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    # Guardado del texto original en un archivo.
    with open('output/output_original.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(text)))
    # Imprime las primeras 100 palabras del texto.
    print(text[:100])
    print("Tokenizado completo. Guardado en output/output_original.txt")


    # Eliminacion de puntuación.

    # Puntuaction incluye el apóstrofe especial ’
    punctuation = string.punctuation + "’"
    # Deteccion de caracteres de puntuación usando expresiones regulares.
    re_punc = re.compile('[%s]' % re.escape(punctuation))
    # Eliminación de la puntuación de las palabras del texto.
    stripped = [re_punc.sub('', w) for w in text]
    # Guardado de las palabras sin puntuación en un archivo.
    with open('output/output_stripped.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(stripped)))
    # Imprime las primeras 100 palabras sin puntuación.
    print(stripped[:100])
    print("Puntuación eliminada. Guardado en output/output_stripped.txt")

    # Conversión a minúsculas.

    # Conversión de palabras a minúsculas.
    # Stripped puede ser reemplazada por text si se
    # desea conservar la puntuación.
    lw_text = [word.lower() for word in stripped]
    # Guardado de las palabras en minúsculas en un archivo.
    with open('output/output_lowercase.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(lw_text)))
    # Imprime las primeras 100 palabras en minúsculas.
    print(lw_text[:100])
    print("Convertido a minúsculas. Guardado en output/output_lowercase.txt")


    # Ejemplo con re.

    # Búsqueda de todas las palabras que contienen 'cat'.
    cat_words_re = re.compile(r'.*cat.*')
    # Filtrado de palabras que coinciden con la expresión regular
    # 'cat' dentro del array de minusculas.
    cat_words = [w for w in lw_text if cat_words_re.match(w)]
    # Guardado de las palabras que contienen 'cat' en un archivo.
    with open('output/output_cats.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(cat_words)))
    # Imprime las primeras 100 palabras que contienen 'cat'.
    print(cat_words[:100])
    print("Palabras que contienen 'cat' encontradas. Guardado en output/output_cats.txt")


    # Porter Stemming
    # Algoritmo basado en reglas para reducir las palabras a su raíz.
    porter = PorterStemmer()
    # Aplicación del stemming a las palabras en minúsculas.
    porter_stemmed = [porter.stem(word) for word in lw_text]
    # Guardado de las palabras con Porter Stemming en un archivo.
    with open('output/output_porter_stemmed.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(porter_stemmed)))
    # Imprime las primeras 100 palabras con Porter Stemming.
    print(porter_stemmed[:100])
    print("Porter Stemming aplicado. Guardado en output/output_porter_stemmed.txt")

    # Snowball Stemming
    snowball = nltk.stem.SnowballStemmer('english')
    # Aplicación del stemming a las palabras en minúsculas.
    snowball_stemmed = [snowball.stem(word) for word in lw_text]
    # Guardado de las palabras con Snowball Stemming en un archivo.
    with open('output/output_snowball_stemmed.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(snowball_stemmed)))
    # Imprime las primeras 100 palabras con Snowball Stemming.
    print(snowball_stemmed[:100])
    print("Snowball Stemming aplicado. Guardado en output/output_snowball_stemmed.txt")

    # WordNet Lemmatization
    lemmatizer = nltk.WordNetLemmatizer()
    # Aplicación de la lematización a las palabras en minúsculas.
    lemmatized = [lemmatizer.lemmatize(word, pos='v') for word in lw_text]
    # Guardado de las palabras lematizadas en un archivo.
    with open('output/output_lemmatized.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(list(lemmatized)))
    # Imprime las primeras 100 palabras lematizadas.
    print(lemmatized[:100])
    print("Lematización aplicada. Guardado en output/output_lemmatized.txt")




if __name__ == '__main__':
        main()

