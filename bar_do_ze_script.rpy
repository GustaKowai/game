label barDoZe:
    #play music "bar.wav"  volume 2.0

    if jogador1:
        show screen char_name_screen([nome1],[jogador1])
        $ energia = energiaAzul
        show screen energy_screen([energia],[jogador1])
    else:
        show screen char_name_screen([nome2],[jogador1])
        $ energia = energiaLaranja
        show screen energy_screen([energia],[jogador1])

    scene bg bar
    show ze default

    z "E ai, como posso te ajudar hoje?"

    if energia > 0:
        jump zeAjuda
    else:
        z "Você parece esgotado. Beba um drink e vá para casa."
        if trocaJogadorBar:
            $ trocaJogadorBar = False
            jump changeDay
        $ trocaJogadorBar = True
        jump barDoZe

    label zeAjuda:
        z "Pois bem, o que pretende me mostrar hoje?"
        menu:
            "coisa 1" if zePinga:
                jump barDoZe

    jump trocaPersonagem
    
    label trocaPersonagem:

        if jogador1:
            $ jogador1 = False
        else:
            $ jogador1 = True