#######----Escolha de onde investigar -----################
default lugar1true = True
default lugar2true = True
default lugar3true = True
default lugar4true = True
default lugar5true = True
default lugar6true = True

label investigacao:
    play music "abandoned.ogg" volume 2.0
    scene bg quartel
    with gatodissolve
    default energia = 6
    if day1 == True and katDay1inv == True and aleDay1inv == True:
        n "Agora durante a noite vocês terão a chance de investigar um pouco mais sobre nossas novatas."
        n "Para isso vocês terão um sistema de Energia, que é mostrado na parte superior direita da tela"
        n "Cada ação feita consumirá um de energia, se a energia chegar a zero vocês não poderão mais investigar."
        n "A energia de cada jogador é medida separadamente, porém os itens que são coletados são armazenados em conjunto."
        n "A energia também é usada no Bar do Zé. Lá vocês poderão pedir mais informações sobre algo que encontraram de interessante."
        n "Lembrem-se de guardar um pouco de energia para conversar com o Zé, ele é uma pessoa difícil."
        n "Nos próximos dias eu não explicarei novamente, portanto espero que tenham entendido."
    
    $ JogadorAtivo = 0
    if jogador1:
        $ jogador1 = False
        show screen char_name_screen([nome2],[jogador1])
    else:
        $ jogador1 = True
        show screen char_name_screen([nome1],[jogador1])
    if katDay1inv or aleDay1inv:
        if jogador1:
            "E agora {color=#1338BE}[nome1]{/color}, para onde vamos?"
        else:
            "E agora {color=#F56300}[nome2]{/color}, para onde vamos?"
    menu:
        "Para o escritório da Katarina" if katDay1inv:
            jump d1kat1inv
        "Para o Ateliê da Alessandra" if katDay1inv:
            jump d1ale1inv
    
    jump barDoZe

    ##################---Investigações---######################

    label d1kat1inv:
        $ katDay1inv = False

        if energia >= 0:

            if jogador1:
                azul "Onde irei investigar?"
            else:
                laranja "Onde irei investigar?"

            menu:
                "Lugar 1" if lugar1true:
                    $ energia -= 1
                    jump lugar1
                "Lugar 2" if lugar2true:
                    $ energia -= 1
                    jump lugar2
                "Lugar 3" if lugar3true:
                    $ energia -= 1
                    jump lugar3
                "Lugar 4" if lugar4true:
                    $ energia -= 1
                    jump lugar4
                "Lugar 5" if lugar5true:
                    $ energia -= 1
                    jump lugar5
                "Lugar 6" if lugar6true:
                    $ energia -= 1
                    jump lugar6
                "Já vi o suficiente":
                    jump investigacao

        jump investigacao

    label lugar1:
        $ lugar1true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    
    label lugar2:
        $ lugar2true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    
    label lugar3:
        $ lugar3true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    
    label lugar4:
        $ lugar4true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    
    label lugar5:
        $ lugar5true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    
    label lugar6:
        $ lugar6true = False
        "Você investiga o lugar 1"
        jump d1kat1inv
    