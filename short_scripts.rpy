########################################################################################################################### 
######################################----------Troca de jogador--------###################################################
########################################################################################################################### 

label whereToGo:
    play music "audio/quartel.wav" volume 2.0
    scene bg quartel
    with gatodissolve
    $ JogadorAtivo = 0
    if jogador1:
        $ jogador1 = False
        show screen char_name_screen([nome2],[jogador1])
    else:
        $ jogador1 = True
        show screen char_name_screen([nome1],[jogador1])
    if katDay1 or aleDay1:
        if jogador1:
            "E agora {color=#1338BE}[nome1]{/color}, para onde vamos?"
        else:
            "E agora {color=#F56300}[nome2]{/color}, para onde vamos?"
    menu:
        "Para o escritório da Katarina" if katDay1:
            jump d1kat1
        "Para o Ateliê da Alessandra" if aleDay1:
            jump d1ale1

        "Para o escritório da Katarina" if katDay2:
            jump d2kat1
        "Para o Ateliê da Alessandra" if aleDay2:
            jump d2ale1

        "Para o escritório da Katarina" if katDay3:
            jump d3kat1
        "Para o Ateliê da Alessandra" if aleDay3:
            jump d3ale1
    
    jump investigacao #irei deixar comentado enquanto a parte noturna está em desenvolvimento.
    jump changeDay                                    
####################################################################################################################### 
###################################-----------Troca de Dia-----------##################################################
####################################################################################################################### 
label changeDay:
    
    play music "audio/quartel.wav" volume 2.0
    scene bg quartel
    with Fade(0.5, 1.0, 0.5)
    "É melhor descansarem durante o resto da noite..."
    #"A pontuação de vocês hoje foi:{p=0.1}[nome1]: [k.azul],[a.azul]{p=0.1}[nome2]: [k.laranja],[a.laranja]"
    if (k.azul+a.azul >= k.laranja+a.laranja):
        $ jogador1 = False
    if (k.azul+a.azul <= k.laranja+a.laranja):
        $ jogador1 = True
    #determina quem jogou melhor e coloca ele para jogar primeiro no dia seguinte
    if day2:
        $ day3 = True
        $ katDay3 = True
        $ aleDay3 = True
        $ day2 = False
    if day1:
        $ day2 = True
        $ katDay2 = True
        $ aleDay2 = True
        $ day1 = False
    #"As variáveis atuais são:" 
    #"day1[day1], day2[day2], day3[day3]" 
    #"katDay1[katDay1], katDay2[katDay2], katDay3[katDay3]"
    #"aleDay1[aleDay1], aleDay2[aleDay2], aleDay3[aleDay3]"
    #if day3:
    #jump demoFinal
    jump whereToGo
####################################################################################################################### 
###################################----------Final da Demo-----------##################################################
#######################################################################################################################
label demoFinal:
    show gatovaldo default
    g "Vocês terminaram a demo! Espero que tenham se divertido."
    g "Para saberem, {color=#1338BE}[nome1]{/color} fez \n[k.azul] de 12 pontos disponíveis com a Katarina \ne [a.azul] de 12 pontos disponíveis com a Alessandra"
    
    g "E {color=#F56300}[nome2]{/color} fez \n[k.laranja] de 12 pontos disponíveis com a Katarina \ne [a.laranja] de 12 pontos disponíveis com a Alessandra"
    g "Espero que tenham se divertido, em breve teremos mais missões."
    jump credits