label desenvolvedores1:
    play music "audio/quartel.wav" volume 2.0
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
        "Largar a garrafa" if not garrafa:
            $ garrafa = True
            jump .escolha1
        "Pegar a garrafa" if garrafa:
            $ garrafa = False
            jump .escolha1
        "Pegar o salgadinho" if not salgadinho:
            $ salgadinho = True
            jump .escolha1
        "Largar o salgadinho" if salgadinho:
            $ salgadinho = False
            jump .escolha1
        
        "Outras coisas":
            jump .escolha2
        "Escolher o dia":
            jump desenvolvedoresChooseDay
        "Quero mudar o player ativo":
            jump desenvolvedoresChoosePlayer
        "Quero mudar a afinidade dos jogadores com as garotas":
            jump desenvolvedoresAfinidade

    menu .escolha2:
        g "O que quer alterar?"
        "Pegar o papel amassado" if not papelAmassado:
            $ papelAmassado = True
            jump .escolha1
        "Largar o papel amassado" if papelAmassado:
            $ papelAmassado = False
            jump .escolha2
        "Pegar o Lenço" if not lenco:
            $ lenco = True
            jump .escolha2
        "Largar o lenço" if lenco:
            $ lenco = False
            jump .escolha2
        "Pegar a chave" if not chavegotica:
            $ chavegotica = True
            jump .escolha2
        "Largar a chave" if chavegotica:
            $ chavegotica = False
            jump .escolha2
        "Pegar o cartão de visita" if not cartaoVisita:
            $ cartaoVisita = True
            jump .escolha2
        "Largar o cartão de visita" if cartaoVisita:
            $ cartaoVisita = False
            jump .escolha2        
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
        "Dia 4 da Katarina":
            jump d4kat1
        "Dia 4 da Alessandra":
            jump d4ale1
        "Final da demo":
            jump demoFinal
        "Investigação noturna":
            jump investigacao
        "Bar do zé":
            jump barDoZe
        "Quero mudar mais variáveis":
            jump desenvolvedoresChooseThings
        "Quero mudar o player ativo":
            jump desenvolvedoresChoosePlayer
                
label desenvolvedoresAfinidade:
    menu:
        "Aumentar a afinidade da Alessandra com o player azul":
            $ a.azul += 1
            "A afinidade entre eles agora é [a.azul]"
            jump desenvolvedoresAfinidade
        "Aumentar a afinidade da Katarina com o player azul":
            $ k.azul += 1
            "A afinidade entre eles agora é [k.azul]"
            jump desenvolvedoresAfinidade
        "Aumentar a afinidade da Alessandra com o player laranja":
            $ k.laranja += 1
            "A afinidade entre eles agora é [k.laranja]"
            jump desenvolvedoresAfinidade
        "Aumentar a afinidade da Katarina com o player laranja":
            $ k.laranja += 1
            "A afinidade entre eles agora é [k.laranja]"
            jump desenvolvedoresAfinidade
        "Diminuir a afinidade da Alessandra com o player azul":
            $ a.azul -= 1
            "A afinidade entre eles agora é [a.azul]"
            jump desenvolvedoresAfinidade
        "Diminuir a afinidade da Katarina com o player azul":
            $ k.azul -= 1
            "A afinidade entre eles agora é [k.azul]"
            jump desenvolvedoresAfinidade
        "Diminuir a afinidade da Alessandra com o player laranja":
            $ k.laranja -= 1
            "A afinidade entre eles agora é [k.laranja]"
            jump desenvolvedoresAfinidade
        "Diminuir a afinidade da Katarina com o player laranja":
            $ k.laranja -= 1
            "A afinidade entre eles agora é [k.laranja]"
            jump desenvolvedoresAfinidade
        "Pronto":
            jump desenvolvedoresChooseThings
