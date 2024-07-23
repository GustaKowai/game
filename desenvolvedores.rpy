label desenvolvedores1:
    play music "quartel.wav" volume 2.0
    scene bg quartel
    with Fade(0.5, 1.0, 0.5)
    
    g "Olá desenvolvedores."
    jump desenvolvedoresChoosePlayer

label desenvolvedoresChoosePlayer:
    menu:
        g "Qual o jogador ativo?"
        "Azul":
            $ jogador1 = True
            show screen char_name_screen([nome1],[jogador1])
        "Laranja":
            $ jogador1 = False
            show screen char_name_screen([nome2],[jogador1])

label desenvolvedoresChooseThings:
    menu .escolha1:
        g "O que quer alterar?"
        "Pegar o xadrez" if not xadrez: 
            $ xadrez = True
            jump .escolha1
        "Largar o xadrez" if xadrez: 
            $ xadrez = False
            jump .escolha1
        "Pegar o vestido tiedye" if not vestidotiedye: 
            $vestidotiedye = True
            jump .escolha1
        "Largar o vestido tiedye" if vestidotiedye: 
            $vestidotiedye = False
            jump .escolha1
        "Pegar o tofu" if not tofu: 
            $tofu = True
            jump .escolha1
        "Largar o tofu" if tofu: 
            $tofu = False
            jump .escolha1
        "Outras coisas":
            jump .escolha2
        "Escolher o dia":
            jump desenvolvedoresChooseDay
        "Quero mudar o player ativo":
            jump desenvolvedoresChoosePlayer

    menu .escolha2:
        g "O que quer alterar?"
        "Quero ver as anteriores":
            jump .escolha1
        "Mais coisas":
            jump .escolha2
        "Escolher o dia":
            jump desenvolvedoresChooseDay
        "Quero mudar o player ativo":
            jump desenvolvedoresChoosePlayer

label desenvolvedoresChooseDay:
    menu:
        "Dia 1 da Katarina":
            jump d1kat1
        "Dia 1 da Alessandra":
            jump d1ale1
        "Dia 2 da Katarina":
            jump d2kat1
        "Dia 2 da Alessandra":
            jump d2ale1
        "Dia 3 da Katarina":
            jump d3kat1
        "Dia 3 da Alessandra":
            jump d3ale1
        "Quero mudar mais variáveis":
            jump desenvolvedoresChooseThings
        "Quero mudar o player ativo":
            jump desenvolvedoresChoosePlayer
                
