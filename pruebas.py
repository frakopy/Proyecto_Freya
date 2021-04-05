import vlc, time, os

media_player = vlc.MediaListPlayer()
player = vlc.Instance()
media_list = player.media_list_new()

musicas = ['Fuego.mp3','Baila.mp3','Bomba.mp3']

for musica in musicas:
    media = player.media_new(musica)
    media_list.add_media(media)

media_player.set_media_list(media_list)

media_player.play()

time.sleep(1)

current_state = str(media_player.get_state())

while current_state == 'State.Playing':
    current_state = str(media_player.get_state())
    print('Reproducioendo musica!!!')

