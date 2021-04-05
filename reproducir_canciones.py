import os,time,random, re
import vlc

def play_list(rutas_musicas,MICROFONO, FREYA):

    media_player = vlc.MediaListPlayer()
    player = vlc.Instance()
    media_list = player.media_list_new()

    for musica in rutas_musicas:
        media = player.media_new(musica)
        media_list.add_media(media)

    media_player.set_media_list(media_list)

    media_player.play()

    time.sleep(1)

    while True:
        instruccion = MICROFONO.escuchar(FREYA).lower()
        if 'pausa' in instruccion:
            media_player.pause()
        elif 'play' in instruccion:
            media_player.play()
        elif 'siguiente' in instruccion:
            media_player.next()
        elif 'anterior' in instruccion:
            media_player.previous()
        elif 'stop' in instruccion:
            media_player.stop()
        elif 'finaliza' in instruccion:
            break


def canciones(MICROFONO,FREYA):
    #Invocamos al metodo habla_freya para que nos pregunte por el tipo de musica
    FREYA.habla_freya('¿Que tipo de música quisiera escuchar?')
    
    while True:
        try:
            #Convertimos a minuscula todo el texto que nos devuelva la funcion escuchar
            genero = MICROFONO.escuchar(FREYA).lower()
            patron = 'electrónica|programar|relajante|salsa|reggaetón|vallenato'
            clave = re.findall(patron,genero)[0]
            break
        except Exception as e:
            print(e)
            FREYA.habla_freya('Repite por favor el tipo de música que deseas escuchar')

    dir_electronicas = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Electronica'
    dir_programacion = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Programing_Music'
    dir_relajantes = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Relajante_Concentracion'
    dir_salsa = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Salsa variada'
    dir_reggaeton = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Reggeton nuevo'
    dir_vallenato = 'D:/A_PYTHON/Documentacion_Python/Musica para estudiar/vallenato'

    dir_canciones = {
                'electrónica':dir_electronicas,
                'programar':dir_programacion,
                'relajante':dir_relajantes,
                'salsa':dir_salsa,
                'reggaetón':dir_reggaeton,
                'vallenato':dir_vallenato
                }

    DIRECTORIO = dir_canciones[clave]
    rutas_musicas = []

    for ruta, carpetas, archivos in os.walk(DIRECTORIO):
            for archivo in archivos:
                ruta_cancion = os.path.join(ruta,archivo)
                rutas_musicas.append(ruta_cancion)

    #Llamamos a la funcion que reproducira la lista de canciones
    play_list(rutas_musicas,MICROFONO, FREYA)
    






