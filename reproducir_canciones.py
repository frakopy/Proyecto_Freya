import os,time,random, re, random
import vlc


class Musica():

    def __init__(self):

        self.reproduciendo = False
        self.cambiar_tipo_musica = False
        self.finalizar_musica= False

    def play_list_musics(self,rutas_musicas):

        self.media_player = vlc.MediaListPlayer()
        self.player = vlc.Instance()
        self.media_list = self.player.media_list_new()

        for musica in rutas_musicas:
            self.media = self.player.media_new(musica)
            self.media_list.add_media(self.media)

        self.media_player.set_media_list(self.media_list)
        
    
        self.media_player.play()

        time.sleep(1)#Para que de tiempo de realizar la reproduccion de la música

        #creamos este bucle para que el programa no se cierre y que por lo tanto no finalice la
        #reproduccion, cuando desde el main pedimos un nuevo tipo de musica entonces asignamos
        #el valor de True a la variable cambiar_tipo_musica para que entre en el if y rompa el while
        while True:
            if self.cambiar_tipo_musica:
                #La siguiente variable la cambiamos a False para que no entre automaticamente ya que en 
                #el main la cambiamos a True, entonces sino le modificamos el valor entrara automaticamente
                #en el While ya que seguira siendo True por eso antes de romper el bucle le cambiamos el valor
                self.cambiar_tipo_musica =False
                break
            
            elif self.finalizar_musica:
                break



    def get_path_musics(self,texto,Helena):
        
        self.patron = 'electrónica|programar|relajante|salsa|reggaetón|vallenato' 
        self.clave = re.findall(self.patron,texto)
        
        #preguntamos si la variable clave (una lista) contiene información 
        if self.clave:
            self.clave = self.clave[0]#obtenemos solo el primer elmento en caso que hayan mas
        else:
            #en caso contrario retornamos una lista vacia par que finalice la función
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

        #Desordenamos la lista para que podamos crear una lista de reproduccion cada vez
        #que le indiquemos a Helena que nos reproduzca un tipo de música
        random.shuffle(self.rutas_musicas)

        #retornamos la lista ya desordenada para que siempre se repdozca en un orden diferente
        return self.rutas_musicas
        


if __name__ == "__main__":

    DIRECTORIO = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Programing_Music'
    rutas_musicas = []

    for ruta, carpetas, archivos in os.walk(DIRECTORIO):
            for archivo in archivos:
                ruta_cancion = os.path.join(ruta,archivo)
                rutas_musicas.append(ruta_cancion)
    
    musica = Musica()
    musica.play_list_musics(rutas_musicas)



