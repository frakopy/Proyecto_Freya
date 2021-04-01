import os, time,re
import pyttsx3
import speech_recognition as sr
from reproducir_canciones import canciones


class ProcesarOrden():

    def escuchar_orden(FREYA,MICROFONO):
        lista_ordenes= ['música']
        comandos = 'música|whatsapp|abrir programas|hora'
    
        FREYA.habla_freya('¿Cual es su orden?')

        while True:
            try:
                texto = MICROFONO.escuchar(FREYA)
                comando = re.findall(comandos, texto)[0]
                break
            except:
                FREYA.habla_freya('No escuche la orden puede repetirla por favor')
        
        if comando == 'música':
            canciones(MICROFONO,FREYA)
            
class AsistenteFreya():

    def __init__(self):
        self.freya = pyttsx3.init()
        self.freya.setProperty('rate', 130 )#Modificamos la velocidad de la voz para que no hable muy rapido
    

    def habla_freya(self,texto):
        self.freya.say(texto)
        self.freya.runAndWait()

    def repetir_orden(self):
        self.freya.say("Lo siento no entendi su orden, ¿puede repetir por favor?")
        self.freya.runAndWait()


class Microfono():

    def __init__(self):
        self.r = sr.Recognizer()

    def escuchar(self,FREYA):
        
        while True:
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source, duration=0.5)
                self.audio = self.r.listen(source)

                try:
                    self.texto = self.r.recognize_google(self.audio, language='es-ES')
                    if self.texto:
                        return self.texto
                    else:
                        FREYA.habla_freya('Lo siento, no se escucho lo que dijiste, habla mas alto por favor')
                except Exception as e:
                    print(e)
                    FREYA.habla_freya('Lo siento, no se escucho lo que dijiste, habla mas alto por favor')


if __name__ == '__main__':

    #Instanciamos la clase AsistenteFreya y le indicamos que saludo.
    saludo_freya = 'Hola mi nombre es Freya, estoy para servirle ingeniero'
    FREYA = AsistenteFreya()
    FREYA.habla_freya(saludo_freya)

    #Instanciamos la clase Microfono para poder escuchar las ordenes
    MICROFONO = Microfono()

    #Llamamos al metodo escuchar_orden de la clase ProcesarOrden
    ProcesarOrden.escuchar_orden(FREYA,MICROFONO)


