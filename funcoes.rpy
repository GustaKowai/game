###Funções usadas no jogo:

#Função de alteração de afeto, com exibição de imagem e som.
init python:
    def muda_afeto(pontos):
        global JogadorAtivo
        JogadorAtivo += pontos
        if pontos > 0:
            renpy.sound.play("certo.wav")
            renpy.show("mais",[top_right])
            renpy.pause(0.2)
            renpy.hide("mais")
        if pontos < 0:
            renpy.sound.play("errado.wav", relative_volume=2.5)
            renpy.show("menos",[top_right])
            renpy.pause(0.2)
            renpy.hide("menos")
        return pontos
    
#Esse transform vai ficar aqui junto pois ele só é usado aqui.
transform top_right:
    xalign 0.95
    yalign 0.1

# Sons das falas dos personagens

init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_2(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 2.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_3(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 3.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")


    def beep_4(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 4.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_5(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 5.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_6(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 6.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_7(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 7.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def beep_8(event, **kwargs):
        if event == "show":
            renpy.music.play("bip 8.wav", channel="textSound", loop=True, relative_volume=0.5)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

###Transição de musicas

init python:

    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)

#Cria a função que adiciona os itens nos respectivos inventários
init python:
    def adicionarItem(itemInvestigado):
        if jogador1:
            inventarioAzul.append(itemInvestigado)
            renpy.notify("Adquirido: "+itemInvestigado)
        else:
            inventarioLaranja.append(itemInvestigado)
            renpy.notify("Adquirido: "+itemInvestigado)
        itemInvestigado = ""
