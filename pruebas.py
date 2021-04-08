import wikipedia,re
from concurrent.futures import ThreadPoolExecutor

#resultado = wikipedia.summary('Daniel Ortega', 1)

class Musica():

    def __init__(self):
        self.r = False
    
    def cambia(self):
        print(self.r)
        

m = Musica()

m.cambia()