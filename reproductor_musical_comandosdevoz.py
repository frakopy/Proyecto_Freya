from pygame import mixer, display
import pygame
from threading import Thread
import os,time,random, re, random
import speech_recognition as sr
import pyttsx3


class reproducor_musical():

    def __init__(self):
        self.reproduciendo_musica = True 
        self.proceso = ''
        self.MUSIC_END = pygame.USEREVENT + 1
        self.posicion_cancion = 0
        self.asistente = pyttsx3.init()
        self.asistente.setProperty('rate', 130 )#Modificamos la velocidad de la voz para que no hable muy rapido

    def asistente_habla(self,texto):
        self.asistente.say(texto)
        self.asistente.runAndWait()
    
    def escuchar_orden(self):
        with sr.Microphone() as source:
            try:
                self.audio = recognizer.listen(source, timeout=1)
                self.palabras_escuchadas = recognizer.recognize_google(self.audio, language='es-ES').lower()
                return self.palabras_escuchadas
            except:
                self.palabras_escuchadas = ''
                return self.palabras_escuchadas

    def musica_a_escuchar(self):

        self.musica_seleccionada = ''
        self.patron = 'electrónica|programar|relajante|salsa|reggaetón|vallenato' 
        
        while not self.musica_seleccionada:
            self.asistente_habla('¿Que tipo de música te gustaria escuchar?')
            print('Escuchando orden sobre el tipo de Música que deseas reproducir...')

            with sr.Microphone() as source:
                try:
                    self.audio = recognizer.listen(source, timeout=1)
                    self.musica_seleccionada = recognizer.recognize_google(self.audio, language='es-ES').lower()
                    
                    self.musica_seleccionada = re.findall(self.patron, self.musica_seleccionada)
                    
                    if self.musica_seleccionada:
                        self.musica_seleccionada = self.musica_seleccionada[0]#obtenemos solo el primer elmento en caso que hayan mas
                        return self.musica_seleccionada
                    else:
                        self.asistente_habla('Lo siento no cuento con ese tipo de música por el momento')
                        
                except:
                    self.asistente_habla('No indicaste un tipo de música válido, por favor repite')
                    self.musica_seleccionada = ''

    def crear_lista_reproducion(self, tipo_musica):

        self.dir_electronicas = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Electronica'
        self.dir_programacion = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Programing_Music'
        self.dir_relajantes = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Relajante_Concentracion'
        self.dir_salsa = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Salsa variada'
        self.dir_reggaeton = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Reggeton nuevo'
        self.dir_vallenato = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/vallenato'

        self.dir_canciones = {
                    'electrónica':self.dir_electronicas,
                    'programar':self.dir_programacion,
                    'relajante':self.dir_relajantes,
                    'salsa':self.dir_salsa,
                    'reggaetón':self.dir_reggaeton,
                    'vallenato':self.dir_vallenato,
                    }

        self.DIRECTORIO = self.dir_canciones[tipo_musica]
        self.rutas_musicas = []

        for ruta, carpetas, archivos in os.walk(self.DIRECTORIO):
                for archivo in archivos:
                    self.ruta_cancion = os.path.join(ruta,archivo)
                    self.rutas_musicas.append(self.ruta_cancion)

        #Desordenamos la lista para que podamos crear una lista de reproduccion cada vez
        #que le indiquemos a Helena que nos reproduzca un tipo de música
        random.shuffle(self.rutas_musicas)

        return self.rutas_musicas
    

    def reproducir_musica(self, paht_musics):
        #Despues de que iniciamos la reproduccion de una cancion tenemos que modificar el atributo de la clase 
        #que se llama reproduciendo musica para mantener el control de la reproduccion 
        self.reproduciendo_musica = True
        
        try:
            mixer.init()
            display.init()#Esto es necesario para el manejo de los eventos de lo contrario el programa se rompe
            mixer.music.load(paht_musics[self.posicion_cancion])
            #mixer.music.queue(paht_musics[1])#opcional para agregar una cancion en cola
            mixer.music.set_volume(0.7)
            mixer.music.play()
            mixer.music.set_endevent(self.MUSIC_END)

            while True:
                for event in pygame.event.get():#Recorremos constantemente los eventos para enterarnos cuando la cancion finalice
                    if event.type == self.MUSIC_END:#Verificamos si la canción ha finalizado
                        if path_musics[self.posicion_cancion] == path_musics[-1]:
                            print('Ya nos encontramos en el ultimo elemento de la lista de reproducción')
                        else:
                            self.posicion_cancion += 1
                            mixer.music.load(path_musics[self.posicion_cancion])
                            mixer.music.play()
                            #mixer.music.queue(paht_musics[2])#opcional para agregar una cancion en cola
                
                if self.reproduciendo_musica == False:
                    break
                
                elif self.proceso == "pausa":
                    mixer.music.pause()
                    self.proceso = ""
                
                elif self.proceso == "continuar":
                    mixer.music.unpause()
                    self.proceso = ""
                
                elif self.proceso == "siguiente":
                    if path_musics[self.posicion_cancion] == path_musics[-1]:
                        print("No es posible reproducir la siguiente cancion por que nos encontramos en la ultima.")
                        self.proceso = ""
                    else:
                        self.posicion_cancion += 1
                        mixer.music.load(path_musics[self.posicion_cancion])
                        mixer.music.play()
                        self.proceso = ""
                    
                elif self.proceso == "anterior":
                    if path_musics[self.posicion_cancion] == path_musics[0]:
                        print("No es posible reproducir la cancion anterior por que nos encontramos en la primera.")
                        self.proceso = ""
                    else:
                        self.posicion_cancion -= 1
                        mixer.music.load(path_musics[self.posicion_cancion])
                        mixer.music.play()
                        self.proceso = ""
                
                elif self.proceso == "finalizar":
                    mixer.music.stop()
                    mixer.quit()
                    self.proceso = ""
                    break

        except Exception as e:
            print(e)


if __name__ == "__main__":

    recognizer = sr.Recognizer()#Creamos la instacia para escuchar el audio via el microfono

    musica = reproducor_musical()#Creamos la intancia de la clase reproducir_musical

    def cargar_cancion(paht_musics):
        hilo = Thread(target=musica.reproducir_musica, args=(paht_musics, ), daemon= True)
        hilo.start()

    while True:
        print('Escuchando...')
        #Llamamos al metodo escuchar_orden para obtener el texto de lo que hablamos
        texto = musica.escuchar_orden()
        
        if texto:
            print(texto)
            if 'pausa' in texto:
                musica.proceso = 'pausa'

            elif 'continuar' in texto:
                musica.proceso = 'continuar'
            
            elif 'siguiente' in texto:
                musica.proceso = 'siguiente'
            
            elif 'anterior' in texto:
                musica.proceso = 'anterior'

            elif 'iniciar' in texto:
                genero_musica = musica.musica_a_escuchar()#Llamamos a la funcion que nos evalua si indicamos un tipo de música valido para reproducir
                path_musics = musica.crear_lista_reproducion(genero_musica)#llamamos a la funcion que nos retorna el path donde esta el tipo de música que deseamos escuchar
                cargar_cancion(path_musics)#Finalmente reproducimos la lista de música de acuerdo al tipo de música que indicamos        

            elif 'finaliza' in texto:
                musica.proceso = 'finalizar' #Finalizamos la reproducción 
                break #Rompemos el while para que finalice el programa
