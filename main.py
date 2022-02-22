import os, time,re, datetime, random
import pyttsx3, pyjokes, wikipedia
import speech_recognition as sr
from reproducir_canciones import Musica
from concurrent.futures import ThreadPoolExecutor
from AbrirCerrarProgramas.openClose import open_programs, close_programs

#Creamos nuestra piscina de Threads para usarlo en la llamada a las funciones
ejecutor = ThreadPoolExecutor(max_workers=5)

#Creamos el objeto de tipo Recognizer para reconocer la voz
recognizer = sr.Recognizer()

#Configuramos el lenguaje que se usara para el modulo wikipedia
wikipedia.set_lang("es")

class ProcesarOrden():

    def control_reproduccion(self, comando):
        if 'siguiente' in comando :
            musica.media_player.next()
        elif 'anterior' in comando :
            musica.media_player.previous()
        elif 'pausa' in comando:
            print('He pausado la musica...')
            musica.media_player.pause()
        elif 'reinicia' in comando:
            musica.media_player.play()
        elif 'finaliza' in comando:
            musica.media_player.stop()
            musica.finalizar_musica = True


    def escuchar_orden(self):
        #Es importtante cerrar el Microfono de la computadora despues de hablar ya que de lo contrario si se continua escuchando la
        #Ruido recognozer seguira esperando recibir mas información y nunca retornara el texto has que haya silencio total, el parámetro
        #de time out funciona para que recognizer deje de esperar mas información segundos despues de escuchar silencio, en nuestro caso 1 segundo
        try:
            with sr.Microphone() as source:
                try:
                    recognizer.adjust_for_ambient_noise(source)#To avoid ambient noise problem
                    self.audio = recognizer.listen(source, timeout=3)
                    self.palabras_escuchadas = recognizer.recognize_google(self.audio, language='es-ES').lower()
                    return self.palabras_escuchadas
                except:
                    self.palabras_escuchadas = ''
                    return self.palabras_escuchadas
        except Exception as e:
            print(e)
            print()
            print('Please check your microphone settings...')

    def ejecuta_orden(self,texto):

        #Esta funcion se utiliza para controlar la repoduccion de una cancion (pausar, siguiente, anterior, finalizar reproducción...)
        self.control_reproduccion(texto)
        #musica.control_media_player = texto
        #print(musica.control_media_player)

        #Despues de escuchar la orden intentamos procesarla si se cumplen las siguiente condiciones
        if 'música' in texto and 'pausa' not in texto and 'siguiente' not in texto and \
            'anterior' not in texto and 'finaliza' not in texto and 'reinicia' not in texto:
            
            #llamamos a la funcion get_path_musicas para obtener un listado de rutas de las
            #canciones que vamos a reproducir
            self.path_musics = musica.get_path_musics(texto,Helena)

            if self.path_musics and not musica.reproduciendo:
                Helena.habla_Helena('Procedo a ejecutar su orden')
                ejecutor.submit(musica.play_list_musics,self.path_musics)
                #Para no permitir que se reproduzca otro tipo de musica si ya hay una en curso
                musica.reproduciendo = True
                texto = ''
            
            elif musica.reproduciendo and self.path_musics:
                musica.cambiar_tipo_musica = True
                musica.media_player.stop()
                ejecutor.submit(musica.play_list_musics,self.path_musics)
                texto = ''

        elif 'hora' in texto:
            h = datetime.datetime.now()
            hora = h.strftime('%H')
            minutos = h.strftime('%M')
            segundos = h.strftime('%S')

            Helena.habla_Helena(f'Son las {hora} horas con {minutos} minutos y {segundos} segundos')
            texto = ''
        
        elif 'broma' in texto:
            list_jokes = (pyjokes.get_jokes(language='es'))
            joke = random.randint(0, len(list_jokes) - 1)
            Helena.habla_Helena(list_jokes[joke])
            texto = ''

        elif 'quién es' in texto:
            Helena.habla_Helena('Un momento, estoy buscando esa información')
            buscar = texto.replace('quién es', '')
            resultado = wikipedia.summary(buscar, 1)
            Helena.habla_Helena(resultado)
            texto = ''
        
        elif 'inicia programa' in texto:
            Helena.habla_Helena('Hola ingeniero Francisco, Abriendo programas')
            open_programs()
            texto = ''
            Helena.habla_Helena('Se finalizó con la orden de abrir programas')

        elif 'cierra programa' in texto:
            Helena.habla_Helena('De acuerdo ingeniero Francisco, Cerrando programas')
            close_programs()
            texto = ''
            Helena.habla_Helena('Se finalizó con la orden de cerrar programas')

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
            saludo_Helena = 'Buenos dias mi nombre es Helena, estoy para servirle'
            self.habla_Helena(saludo_Helena)
        elif self.hora >= 12 and self.hora < 18:
            saludo_Helena = 'Buenas tardes mi nombre es Helena, estoy para servirle'
            self.habla_Helena(saludo_Helena)
        elif self.hora >= 18:
            saludo_Helena = 'Buenas noches mi nombre es Helena, estoy para servirle'
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

    #Creamos la instancia de la clase Musica, para utilizarla mas adelante en la reproduccion de
    #musicas cuando se lo ordenemos al asistente (Helena)
    musica = Musica()

    while True:
        print('Escuchando...')
        #Llamamos al metodo escuchar_orden para obtener el texto de lo que hablamos
        texto = orden.escuchar_orden()
        #llamamos a la funcion ejecuta_orden para que intente procesar la orden
        if texto:
            print(texto)
            orden.ejecuta_orden(texto)

