from googletrans import Translator

trans = Translator()
wynik = trans.translate('experience', dest='pl')

print(wynik.text)

