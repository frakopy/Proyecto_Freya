import os,time,random, re
import vlc
import speech_recognition as sr

recognizer = sr.Recognizer()

class Musica():

    def play_list_musics(self,rutas_musicas, escucha_orden):

        self.media_player = vlc.MediaListPlayer()
        self.player = vlc.Instance()
        self.media_list = self.player.media_list_new()

        for musica in rutas_musicas:
            self.media = self.player.media_new(musica)
            self.media_list.add_media(self.media)

        self.media_player.set_media_list(self.media_list)

        self.media_player.play()

        time.sleep(1)

        #creamos este bucle para que el programa no se cierre y que por lo tanto no finalice la
        #reproduccion hasta que se lo ordenemos al llamar a la funcion que modifica el valor de 
        #la variable finalizar la cual esta siendo evaluada constantemente en el bucle While
        while True:
            #La funcion escucha_orden se la recibimos por parámetro
            self.orden = escucha_orden()
            print(self.orden)
            if 'siguiente' in self.orden :
                self.media_player.next()        
            elif 'anterior' in self.orden :
                self.media_player.previous()
            elif 'pausa' in self.orden:
                self.media_player.pause()
            elif 'play' in self.orden:
                self.media_player.play()
            elif 'finaliza' in self.orden:
                self.media_player.stop()
                break


    def get_path_musics(self,texto,Helena):

        try:
            self.patron = 'electrónica|programar|relajante|salsa|reggaetón|vallenato'
            self.clave = re.findall(self.patron,texto)[0]
        except Exception as e:
            print(e)
            Helena.habla_Helena('Repite por favor el tipo de música que deseas escuchar')
            self.rutas_musicas = []
            return self.rutas_musicas#Hacemos este return para que finalice la funcion y no ejecute el codigo de abajo

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
                    'vallenato':self.dir_vallenato
                    }

        self.DIRECTORIO = self.dir_canciones[self.clave]
        self.rutas_musicas = []

        for ruta, carpetas, archivos in os.walk(self.DIRECTORIO):
                for archivo in archivos:
                    self.ruta_cancion = os.path.join(ruta,archivo)
                    self.rutas_musicas.append(self.ruta_cancion)

        return self.rutas_musicas
        






