meme_dict = {
            "CRESTA": "la cima de un lugar o el punto mas alto",
            "WEON": "es un termino chileno que se puede ocupar para referirce a una persona tonta o a un amigo",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
#hola

if word in meme_dict.keys():
    print( meme_dict[word])
else:
    print("su palabra no esta 😢!")
   
