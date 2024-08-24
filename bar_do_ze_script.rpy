label barDoZe:
    play music "audio/cassino.wav"  volume 2.0
    define trocaJogadorBar = False
    define inventarioAtual = []
    if jogador1:
        show screen char_name_screen([nome1],[jogador1])
        $ inventarioAtual = inventarioAzul
        $ energia = energiaAzul
        show screen energy_screen([energia],[jogador1])
    else:
        show screen char_name_screen([nome2],[jogador1])
        $ inventarioAtual = inventarioLaranja
        $ energia = energiaLaranja
        show screen energy_screen([energia],[jogador1])

    scene bg bar
    show ze default

label conversaBar:

    z "E ai, como posso te ajudar hoje?"

    if energia > 0:
        show screen energy_screen([energia],[jogador1])
        jump zeAjuda
    else:
        z "Você parece esgotado. Beba um drink e vá para casa."
        if trocaJogadorBar:
            $ trocaJogadorBar = False
            jump changeDay
        $ trocaJogadorBar = True
        jump conversaBar

    label zeAjuda:
        z "Pois bem, o que pretende me mostrar hoje?"
        menu:
            "coisa 1" if "miniPinga" in inventarioAtual:
                $ inventarioAtual.remove("miniPinga")
                $ energia -= 1
                z "To vendo que vc trouxe uma miniPinga!"
                jump conversaBar
            "Coisa 2":
                z "Você não trouxe nada?!"
                $ energia -= 1
                jump conversaBar

    jump trocaPersonagem
    
    label trocaPersonagem:

        if jogador1:
            $ jogador1 = False
        else:
            $ jogador1 = True