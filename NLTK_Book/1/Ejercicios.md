# Ejercicios NLTK Book - Capítulo 1

## Ejercicios "Your turn"

### 1. Enter a few more expressions of your own. You can use asterisk (*) for multiplication and slash (/) for division, and parentheses for bracketing expressions.

```python
# Expresiones matemáticas
(5 + 3) * 2
10 / (2 + 3)
7 * (4 - 1) + 6 / 2
```
```python
# Salida de los comandos
16.0
2.0
24.0
```

### 2. Try searching for other words; to save re-typing, you might be able to use up-arrow, Ctrl-up-arrow or Alt-p to access the previous command and modify the word being searched.
You can also try searches on some of the other texts we have included. For example, search Sense and Sensibility for the word affection, using text2.concordance("affection"). Search the book of Genesis to find out how long some people lived, using text3.concordance("lived"). You could look at text4, the Inaugural Address Corpus, to see examples of English going back to 1789, and search for words like nation, terror, god to see how these words have been used differently over time. We've also included text5, the NPS Chat Corpus: search this for unconventional words like im, ur, lol. (Note that this corpus is uncensored!)

```python
# Búsquedas en textos de NLTK Book
from nltk.book import *
text2
text2.concordance("affection")
text3
text3.concordance("lived")
text4
text3.concordance("nation")
text3.concordance("god")
text5
text5.concordance("lol")
```
```python
# Salida de los comandos
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908

<Text: Sense and Sensibility by Jane Austen 1811>
Displaying 25 of 79 matches:
, however , and , as a mark of his affection for the three girls , he left them
t . It was very well known that no affection was ever supposed to exist between
deration of politeness or maternal affection on the side of the former , the tw
d the suspicion -- the hope of his affection for me may warrant , without impru
hich forbade the indulgence of his affection . She knew that his mother neither
rd she gave one with still greater affection . Though her late conversation wit
 can never hope to feel or inspire affection again , and if her home be uncomfo
m of the sense , elegance , mutual affection , and domestic comfort of the fami
, and which recommended him to her affection beyond every thing else . His soci
ween the parties might forward the affection of Mr . Willoughby , an equally st
 the most pointed assurance of her affection . Elinor could not be surprised at
he natural consequence of a strong affection in a young and ardent mind . This 
 opinion . But by an appeal to her affection for her mother , by representing t
 every alteration of a place which affection had established as perfect with hi
e will always have one claim of my affection , which no other can possibly shar
f the evening declared at once his affection and happiness . " Shall we see you
ause he took leave of us with less affection than his usual behaviour has shewn
ness ." " I want no proof of their affection ," said Elinor ; " but of their en
onths , without telling her of his affection ;-- that they should part without 
ould be the natural result of your affection for her . She used to be all unres
distinguished Elinor by no mark of affection . Marianne saw and listened with i
th no inclination for expense , no affection for strangers , no profession , an
till distinguished her by the same affection which once she had felt no doubt o
al of her confidence in Edward ' s affection , to the remembrance of every mark
 was made ? Had he never owned his affection to yourself ?" " Oh , no ; but if 

<Text: The Book of Genesis>
Displaying 25 of 38 matches:
ay when they were created . And Adam lived an hundred and thirty years , and be
ughters : And all the days that Adam lived were nine hundred and thirty yea and
nd thirty yea and he died . And Seth lived an hundred and five years , and bega
ve years , and begat Enos : And Seth lived after he begat Enos eight hundred an
welve years : and he died . And Enos lived ninety years , and begat Cainan : An
 years , and begat Cainan : And Enos lived after he begat Cainan eight hundred 
ive years : and he died . And Cainan lived seventy years and begat Mahalaleel :
rs and begat Mahalaleel : And Cainan lived after he begat Mahalaleel eight hund
years : and he died . And Mahalaleel lived sixty and five years , and begat Jar
s , and begat Jared : And Mahalaleel lived after he begat Jared eight hundred a
and five yea and he died . And Jared lived an hundred sixty and two years , and
o years , and he begat Eno And Jared lived after he begat Enoch eight hundred y
 and two yea and he died . And Enoch lived sixty and five years , and begat Met
 ; for God took him . And Methuselah lived an hundred eighty and seven years , 
 , and begat Lamech . And Methuselah lived after he begat Lamech seven hundred 
nd nine yea and he died . And Lamech lived an hundred eighty and two years , an
ch the LORD hath cursed . And Lamech lived after he begat Noah five hundred nin
naan shall be his servant . And Noah lived after the flood three hundred and fi
xad two years after the flo And Shem lived after he begat Arphaxad five hundred
at sons and daughters . And Arphaxad lived five and thirty years , and begat Sa
ars , and begat Salah : And Arphaxad lived after he begat Salah four hundred an
begat sons and daughters . And Salah lived thirty years , and begat Eber : And 
y years , and begat Eber : And Salah lived after he begat Eber four hundred and
 begat sons and daughters . And Eber lived four and thirty years , and begat Pe
y years , and begat Peleg : And Eber lived after he begat Peleg four hundred an

<Text: Inaugural Address Corpus>
Displaying 8 of 8 matches:
 th And I will make of thee a great nation , and I will bless thee , and make 
 four hundred years ; And also that nation , whom they shall serve , will I ju
beget , and I will make him a great nation . But my covenant will I establish 
ll surely become a great and mighty nation , and all the nations of the earth 
D , wilt thou slay also a righteous nation ? Said he not unto me , She is my s
 son of the bondwoman will I make a nation , because he is thy seed . And Abra
 hand ; for I will make him a great nation . And God opened her eyes , and she
ghty : be fruitful and multiply ; a nation and a company of nations shall be o

Displaying 25 of 231 matches:
                     In the beginning God created the heaven and the earth . An
 face of the deep . And the Spirit of God moved upon the face of the waters . A
ved upon the face of the waters . And God said , Let there be light : and there
 be light : and there was light . And God saw the light , that it was good : an
aw the light , that it was good : and God divided the light from the darkness .
ded the light from the darkness . And God called the light Day , and the darkne
 the morning were the first day . And God said , Let there be a firmament in th
vide the waters from the waters . And God made the firmament , and divided the 
above the firmame and it was so . And God called the firmament Heaven . And the
the morning were the second day . And God said , Let the waters under the heave
the dry land appe and it was so . And God called the dry land Earth ; and the g
gether of the waters called he Se and God saw that it was good . And God said ,
Se and God saw that it was good . And God said , Let the earth bring forth gras
seed was in itself , after his ki and God saw that it was good . And the evenin
 the morning were the third day . And God said , Let there be lights in the fir
ight upon the ear and it was so . And God made two great lights ; the greater l
 the nig he made the stars also . And God set them in the firmament of the heav
 divide the light from the darkne and God saw that it was good . And the evenin
the morning were the fourth day . And God said , Let the waters bring forth abu
in the open firmament of heaven . And God created great whales , and every livi
nd every winged fowl after his ki and God saw that it was good . And God blesse
ki and God saw that it was good . And God blessed them , saying , Be fruitful ,
 the morning were the fifth day . And God said , Let the earth bring forth the 
arth after his ki and it was so . And God made the beast of the earth after his
epeth upon the earth after his ki and God saw that it was good . And God said ,

<Text: Chat Corpus>
Displaying 25 of 822 matches:
ast PART 24 / m boo . 26 / m and sexy lol U115 boo . JOIN PART he drew a girl w
ope he didnt draw a penis PART ewwwww lol & a head between her legs JOIN JOIN s
a bowl i got a blunt an a bong ...... lol JOIN well , glad it worked out my cha
e " PART Hi U121 in ny . ACTION would lol @ U121 . . . but appearently she does
30 make sure u buy a nice ring for U6 lol U7 Hi U115 . ACTION isnt falling for 
 didnt ya hear !!!! PART JOIN geeshhh lol U6 PART hes deaf ppl here dont get it
es nobody here i wanna misbeahve with lol JOIN so read it . thanks U7 .. Im hap
ies want to chat can i talk to him !! lol U121 !!! forwards too lol JOIN ALL PE
k to him !! lol U121 !!! forwards too lol JOIN ALL PErvs ... redirect to U121 '
 loves ME the most i love myself JOIN lol U44 how do u know that what ? jerkett
ng wrong ... i can see it in his eyes lol U20 = fiance Jerketts lmao wtf yah I 
cooler by the minute what 'd I miss ? lol noo there too much work ! why not ?? 
 that mean I want you ? U6 hello room lol U83 and this .. has been the grammar 
 the rule he 's in PM land now though lol ah ok i wont bug em then someone wann
flight to hell :) lmao bbl maybe PART LOL lol U7 it was me , U83 hahah U83 ! 80
ht to hell :) lmao bbl maybe PART LOL lol U7 it was me , U83 hahah U83 ! 808265
082653953 K-Fed got his ass kicked .. Lol . ACTION laughs . i got a first class
 . i got a first class ticket to hell lol U7 JOIN any texas girls in here ? any
 . whats up U155 i was only kidding . lol he 's a douchebag . Poor U121 i 'm bo
 ??? sits with U30 Cum to my shower . lol U121 . ACTION U1370 watches his nads 
 ur nad with a stick . ca u U23 ewwww lol *sniffs* ewwwwww PART U115 ! owww spl
ACTION is resisting . ur female right lol U115 beeeeehave Remember the LAst tim
pm's me . charge that is 1.99 / min . lol @ innocent hahah lol .... yeah LOLOLO
 is 1.99 / min . lol @ innocent hahah lol .... yeah LOLOLOLLL U12 thats not nic
s . lmao no U115 Check my record . :) Lol lick em U7 U23 how old r u lol Way to
```

### 3. Pick another pair of words and compare their usage in two different texts, using the similar() and common_contexts() functions.

```python
# Contextos comunes
text2 
text2.common_contexts(["hope", "affection"])
```

```python
# Salida del comando
the_of of_. of_and
```

### 4. How many times does the word lol appear in text5? How much is this as a percentage of the total number of words in this text?

```python
# Frecuencia y porcentaje de "lol" en text5
text5
text5.count("lol")
len(set(text5)) / len(text5)
```

```python
# Salida de los comandos
<Text: Chat Corpus>
704
0.13477005109975562
```

## Ejercicios

### ☼ Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).
```python
# Entradas
18 * 9 + 7 / (8 - 2)
2 * 4 + 7
4 + 8 + 2 + 9 * 3
```

```python
# Salida
163.16666666666666
15
41
```

### ☼ Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?
```python
# Entrada
26 ** 100
```
```python
# Salida
3142930641582938830174357788501626427282669988762475256374173175398995908420104023465432599069702289330964075081611719197835869803511992549376
```

### ☼ The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?

```python
# Entradas
['Monty', 'Python'] * 20
3 * sent1
```

```python
# Salida
['Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python']
['Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.']
```

### ☼ Review 1 on computing with language. How many words are there in text2? How many distinct words are there?
 ```python
# Entrada
text2
len(text2)
len(set(text2))
```
```python
# Salida
<Text: Sense and Sensibility by Jane Austen 1811>
141576
6598
```

### ☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?

Humor es más diverso léxicamente que romance. Superando a romance en diversidad léxica por aproximadamente 12%.

### ☼ Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
```python
text2
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
```

### ☼ Find the collocations in text5.
```python
# Entrada
text5
text5.collocations()
```

```python
# Salida
wanna chat; PART JOIN; MODE #14-19teens; JOIN PART; PART PART;
cute.-ass MP3; MP3 player; JOIN JOIN; times .. .; ACTION watches; guys
wanna; song lasts; last night; ACTION sits; -...)...- S.M.R.; Lime
Player; Player 12%; dont know; lez gurls; long time
```


### ☼ Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation
set(text4) — convierte la secuencia de tokens en un conjunto, eliminando duplicados (queda cada token una sola vez).

len() — cuenta cuántos elementos únicos hay en ese conjunto.