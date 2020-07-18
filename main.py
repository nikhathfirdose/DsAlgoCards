# Spanish and French Translator using python

from translate import Translator

spanish_translate = Translator(to_lang="es")
french_translate = Translator(to_lang="fr")

try:
    with open('quote.txt', mode='r') as quote_file:
        # read the file
        quote = quote_file.read()
        # do the translations
        quote_spanish = spanish_translate.translate(quote)
        quote_french = french_translate.translate(quote)
        # create the translated files
        try:
            with open('quote-es.txt', mode='w') as quote_de:
                quote_de.write(quote_spanish)
            with open('quote-fr.txt', mode='w') as quote_fr:
                quote_fr.write(quote_french)
        except IOError as error:
            print('An error ocurred')
            raise (error)
except FileNotFoundError as error:
    print('File not found')
    raise (error)