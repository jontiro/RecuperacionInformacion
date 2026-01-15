import nltk

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




if __name__ == '__main__':
        main()

