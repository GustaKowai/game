# The script of the game goes in this file.

# The game starts here.

label start:

    
    play music "audio/quartel.wav"  volume 2.0
    scene bg quartel

    n "Antes de começarmos..."


    #Inicia o minigame do tiro. Ficará aqui enquanto eu não souber onde colocar.
    #jump start_minigame

    python:
        nome1 = renpy.input("Qual o nome do jogador azul?")
        nome1 = nome1.strip() or "Azul"
        nome2 = renpy.input("Qual o nome do jogador laranja?")
        nome2 = nome2.strip() or "Laranja"
    if nome1 == nome2:
        n "Vocês estão de brincadeira comigo? {p} Por favor, escolha um nome melhor."
        python:
            nome2 = renpy.input("Qual o nome do jogador laranja?")
            nome2 = nome2.strip() or "Laranja"
    if nome1 == nome2:
        with vpunch
        n "Ok!{w} Vocês que se virem para saber quem é quem!"
        $ doppelganger = True
        achieve Doppelganger

    if nome1 == "GAMSo" or nome2 == "GAMSo":
        play sound "honk.ogg"
        "HONK"
        $ gamsoGamer = True
        achieve GAMSo_gamer
    define azul = Character("[nome1]",color="#1338BE",what_prefix='{color=#1338BE}', what_suffix='{/color}')
    define laranja = Character("[nome2]",color="#f56300",what_prefix='{color=#f56300}', what_suffix='{/color}')

    if nome1 == "wwssadadzx" or nome2 == "wwssadadzx":
        jump desenvolvedores1

    "Quem irá ser o primeiro a jogar?{w} Recomendamos uma conversa amigável para decidir, porém vocês podem usar de maneiras diferentes."

    "Só por favor, precisamos de ambos os jogadores vivos para dar continuidade"

    menu:
        "[nome1] começa":
            $jogador1 = True
            show screen char_name_screen([nome1],[jogador1])
            jump jogadorAzul
        
        "[nome2] começa":
            $jogador1 = False
            show screen char_name_screen([nome2],[jogador1])
            jump jogadorLaranja

    

    
    


    ########################################################################################################################### 
    #####################################--------------FIM-----------------####################################################
    ########################################################################################################################### 

    
#------função usada no final do dia para determinar quanta afeição o personagem ganhou com a Alessandra:

            # if jogador1:
            #     $a.azul += JogadorAtivo
            # else:
            #     $a.laranja += JogadorAtivo

#------função usada no final do dia para determinar quanta afeição o personagem ganhou com a Katarina:

            # if jogador1:
            #     $k.azul += JogadorAtivo
            # else:
            #     $k.laranja += JogadorAtivo
    # This ends the game.

    return

########################################################################################################################### 
############################### -------------Splashcreen------------------################################################# 
########################################################################################################################### 


image splash = "splash.png"
image splash1 = "splash/1.png"
image splash2 = "splash/2.png"
image splash3 = "splash/3.png"
image splash4 = "splash/4.png"
image splash5 = "splash/5.png"
image splash6 = "splash/6.png"

label splashscreen:
    play music "introMusic.ogg"
    scene black
    with Pause(1)

    play sound "honk.ogg"
    show text "GAMSo apresenta..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    play sound "honk.ogg"
    show splash5 with dissolve
    with Pause(0.1)

    play sound "honk.ogg"
    show splash3 with dissolve
    with Pause(0.1)
    
    play sound "honk.ogg"
    show splash4
    with Dissolve(1)
    
    play sound "honk.ogg"
    show splash1 with dissolve
    with Pause(1)
    
    play sound "honk.ogg"
    show splash6 with dissolve
    with Pause(1.5)
    stop music fadeout 1.5

    $ persistent.watch_Intro = True
    scene black with dissolve
    with Pause(1)

    return
