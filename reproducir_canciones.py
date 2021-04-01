import os,time,random, re

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

    electronicas = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Electronica')
    programacion = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Programing_Music')
    relajantes = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Relajante_Concentracion')
    salsa = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Salsa variada')
    reggaeton = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/Reggeton nuevo')
    vallenato = os.listdir('D:/A_PYTHON/Documentacion_Python/Musica para estudiar/vallenato')

    canciones = {
                        'electrónica':electronicas,
                        'programar':programacion,
                        'relajante':relajantes,
                        'salsa':salsa,
                        'reggaetón':reggaeton,
                        'vallenato':vallenato
                        }

    canciones_a_reproducir = canciones[clave]
    cancion = random.choice(canciones_a_reproducir)
    
    for ruta, carpetas, archivos in os.walk("D:\A_PYTHON\Documentacion_Python\Musica para estudiar"):
            if cancion in archivos:
                ruta_cancion = os.path.join(ruta,cancion)
                break

    os.startfile(ruta_cancion)







