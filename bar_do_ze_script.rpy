label barDoZe:
    $ aleDayinv = True
    $ katDayinv = True
    play music "audio/cassino.wav"  volume 2.0
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
    if jogador1:
        with fadeA
    else:
        with fadeL

label conversaBar:
    if energia > 0:
        show screen energy_screen([energia],[jogador1])
        jump zeAjuda
    else:
        z "Hum..."
        z "Você parece esgotado. Beba um drink e vá para casa."
        jump fimdobar
        

label zeAjuda:
    z "Pois bem, o que pretende me mostrar hoje?"
    menu:
        "coisa 1" if "miniPinga" in inventarioAtual:
            $ inventarioAtual.remove("miniPinga")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barminipinga
        "Na verdade nada, só quero ir dormir.":
            if energia > 0:
                z "Tem certeza? Você ainda me parece ter energia."
                menu:
                    "sim":
                        z "Okay então, bom descanço."
                        jump fimdobar
                    "Não, acho que quero te mostrar mais algumas coisas.":
                        z "Então não me faça perder tempo por favor."
                        jump conversaBar

label trocaPersonagem:
    if jogador1:
        $ jogador1 = False
    else:
        $ jogador1 = True
    jump barDoZe
label fimdobar:
    n "Você vai para a casa descansar"
    scene bg bar
    show ze default
    if trocaJogadorBar:
        $ trocaJogadorBar = False
        hide screen energy_screen
        jump changeDay
    $ trocaJogadorBar = True
    jump trocaPersonagem

label barminipinga:
    z "To vendo que vc trouxe uma mini Pinga!"
    z "Essa é das boas. Parece feita de planta carnívora."
    z "Onde arranjou? Faz tempo que não vejo uma assim..."
    z "Analisando melhor o rótulo, parece de fabricação caseira."
    z "Mas é uma receita de família, da para ver pela assinatura."
    z "Só o cheiro disso aqui é capaz de desmaiar um elefante. Tem mais álcool aqui do que no negócio que a gente ta usando para lavar as mãos."
    z "Ela é boa. Com certeza foi feita por alguém habilidoso."
    jump conversaBar