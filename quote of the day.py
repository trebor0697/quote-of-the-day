import random

quotes = ["NO SE PUEDE ENCONTRAR LA PAZ EVITANDO LA VIDA.\n\t - VIRGINIA WOOLF", "HEMOS SIDO PUESTOS AQUÍ PARA APRENDER LECCIONES QUE NOS CONVERTIRÁN EN ALMAS MÁS COMPLETAS\n\t - ERIC PEARL", "VIVIR EN AMOR IMPLICA RENACER EN AMOR\n\t - VANESSA AGUILAR"]

randomQuoteOfTheDay = random.randint(1, 30) #1 - 30


if (randomQuoteOfTheDay > 0 and randomQuoteOfTheDay < 11):
    print (quotes[0])

elif (randomQuoteOfTheDay > 10 and randomQuoteOfTheDay < 21):
    print (quotes[1])
    
else:
    print (quotes [2])
