import os, time,re, datetime, random
import pyttsx3, pyjokes, wikipedia
import speech_recognition as sr
from reproducir_canciones import Musica
from concurrent.futures import ThreadPoolExecutor

ejecutor = ThreadPoolExecutor(max_workers=2)
recognizer = sr.Recognizer()

class ProcesarOrden():

    def escuchar_orden(self):

        with sr.Microphone() as source:
            self.audio = recognizer.listen(source)
        try:
            self.texto = recognizer.recognize_google(self.audio, language='es-ES').lower()
            self.texto = self.texto.lower()
            return self.texto
        except Exception as e:
            self.texto = ''
            return self.texto

    def ejecuta_orden(self,texto):
        
        #Despues de escuchar la orden intentamos procesarla si se cumplen alguna de las siguiente condiciones
        if 'música' in texto and 'pausa' not in texto and 'siguiente' not in texto and \
            'anterior' not in texto and 'finaliza' not in texto and 'play' not in texto:
            self.musica = Musica()
            self.path_musics = self.musica.get_path_musics(self.texto,Helena)
            if self.path_musics:
                ejecutor.submit(self.musica.play_list_musics,self.path_musics,self.escuchar_orden)
        
        elif 'hora' in texto:
            h = datetime.datetime.now()
            hora = h.strftime('%H')
            minutos = h.strftime('%M')
            segundos = h.strftime('%S')

            Helena.habla_Helena(f'Son las {hora} horas con {minutos} minutos y {segundos} segundos')
        
        elif 'broma' in texto:
            list_jokes = (pyjokes.get_jokes(language='es'))
            joke = random.randint(0, len(list_jokes) - 1)
            Helena.habla_Helena(list_jokes[joke])

        elif 'quién es' in texto:
            wikipedia.set_lang("es") 
            buscar = texto.replace('quién es', '')
            resultado = wikipedia.summary(buscar, 1)
            Helena.habla_Helena(resultado)

        elif 'hasta pronto' in texto:
            Helena.habla_Helena('Hasta luego, fue un placer atenderte')
            exit()
            
class AsistenteHelena():

    def __init__(self):
        self.Helena = pyttsx3.init()
        self.Helena.setProperty('rate', 130 )#Modificamos la velocidad de la voz para que no hable muy rapido
    

    def habla_Helena(self,texto):
        self.Helena.say(texto)
        self.Helena.runAndWait()

    def saludo_Helena(self):
        self.hora = int(datetime.datetime.now().strftime('%H'))
        if self.hora < 12:
            saludo_Helena = 'Buenos dias mi nombre es Helena, estoy para servile'
            self.habla_Helena(saludo_Helena)
        elif self.hora >= 12 and self.hora < 18:
            saludo_Helena = 'Buenas tardes mi nombre es Helena, estoy para servile'
            self.habla_Helena(saludo_Helena)
        elif self.hora >= 18:
            saludo_Helena = 'Buenas noches mi nombre es Helena, estoy para servile'
            self.habla_Helena(saludo_Helena)

    def repetir_orden(self):
        self.Helena.say("Lo siento no entendi su orden, ¿puede repetir por favor?")
        self.Helena.runAndWait()


if __name__ == '__main__':

    #Instanciamos la clase AsistenteHelena y le indicamos que saludo.
    Helena = AsistenteHelena()
    Helena.saludo_Helena()

    #Instanciamos la clase procesar orden
    orden = ProcesarOrden()

    while True:
        #Llamamos al metodo escuchar_orden para obtener el texto de lo que hablamos
        texto = orden.escuchar_orden()
        #llamamos a la funcion ejecuta_orden para que intente procesar la orden
        orden.ejecuta_orden(texto)


