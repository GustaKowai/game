#######----Escolha de onde investigar -----################
default escolhido = []
default energiaAzul = 0
default energiaLaranja = 0
default itemInvestigado = ""
default inventarioLaranja = []
default inventarioAzul = []


#Cria a função que adiciona os itens nos respectivos inventários
init python:
    def adicionarItem(itemInvestigado):
        if jogador1:
            inventarioAzul.append(itemInvestigado)
        else:
            inventarioLaranja.append(itemInvestigado)
        itemInvestigado = ""

label investigacao:
    play music "audio/abandoned.ogg" volume 2.0
    scene bg quartel
    with gatodissolve
    default energia = 4
    $ energia = 4
    if day1 == True and katDayinv == True and aleDayinv == True:
        n "Agora durante a noite vocês terão a chance de investigar um pouco mais sobre nossas novatas."
        n "Para isso vocês terão um sistema de Energia, que é mostrado na parte superior direita da tela"
        show screen energy_screen([energia],[jogador1]) with moveinbottom
        n "Cada ação feita consumirá um de energia, se a energia chegar a zero vocês não poderão mais investigar."
        n "A energia de cada jogador é medida separadamente, porém os itens que são coletados são armazenados em conjunto."
        n "A energia também é usada no Bar do Zé. Lá vocês poderão pedir mais informações sobre algo que encontraram de interessante."
        n "Lembrem-se de guardar um pouco de energia para conversar com o Zé, ele é uma pessoa difícil."
        n "Nos próximos dias eu {color=#ff0000}não explicarei novamente{/color}, portanto espero que tenham entendido."
    
    $ JogadorAtivo = 0
    if jogador1:
        $ jogador1 = False
        show screen char_name_screen([nome2],[jogador1])
        show screen energy_screen([energia],[jogador1])
    else:
        $ jogador1 = True
        show screen char_name_screen([nome1],[jogador1])
        show screen energy_screen([energia],[jogador1])
    if katDayinv or aleDayinv:
        if jogador1:
            "E agora {color=#1338BE}[nome1]{/color}, para onde vamos?"
        else:
            "E agora {color=#F56300}[nome2]{/color}, para onde vamos?"
    menu:
        "Para o escritório da Katarina" if katDayinv:
            play music "audio/escritorio.wav" volume 1.0
            jump d1kat1inv
        "Para o Ateliê da Alessandra" if aleDayinv:
            play music "audio/atelie_intro.ogg" volume 1.0
            queue music "audio/atelie_loop.ogg"
            jump d1ale1inv
    
    hide screen energy_screen
    jump barDoZe

    ##################---Investigações---######################

    ####################----Katarina----########################

    label d1kat1inv:
        $ katDayinv = False
        scene bg escritorio
        if energia > 0:
            show screen energy_screen([energia],[jogador1])
            if jogador1:
                azul "Onde irei investigar?"
            else:
                laranja "Onde irei investigar?"
            menu:
                set escolhido
                "Planta Carnívora":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar1k
                "Tabuleiro de xadrez" if (xadrez):
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar2k
                "Palito de picolé":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar3k
                "Revista antiga":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar4k
                "Garrafa de vodka" if (garrafa):
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar5k
                "Rifle de precisão":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar6k
                "Salgadinho" if (salgadinho):
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar7k

                "Já vi o suficiente":
                    n "Você considera que já viu o suficiente"
                    $escolhido.remove("Já vi o suficiente")
                    if jogador1:
                        $ energiaAzul = energia
                    else:
                        $ energiaLaranja = energia
                    jump investigacao
        n "A investigação de hoje termina por aqui"
        jump investigacao

    ################----Alessandra----#######################

    label d1ale1inv:
        $ aleDayinv = False
        scene bg atelie

        if energia > 0:
            show screen energy_screen([energia],[jogador1])

            if jogador1:
                azul "Onde irei investigar?"
            else:
                laranja "Onde irei investigar?"

            menu:
                set escolhido
                "Carta":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar1a
                "Vestido Tie-Dye" if (vestidotiedye):
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar2a
                "Coleção de CDs do Slipknot":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar3a
                "Capacete de moto":
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar4a
                "Um tofu" if (tofu):
                    $ energia -= 1
                    show screen energy_screen([energia],[jogador1])
                    jump lugar5a
                "Já vi o suficiente":
                    n "Você considera que já viu o suficiente"
                    if jogador1:
                        $ energiaAzul = energia
                    else:
                        $ energiaLaranja = energia

                    jump investigacao


        n "A investigação de hoje termina por aqui"
        jump investigacao