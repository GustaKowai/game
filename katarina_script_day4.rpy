###########################################################################################################################        
######################################### # ----------Katarina------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 4--------------- ##############################################
########################################################################################################################### 

label d4kat1:
    play music "audio/escritorio.wav" volume 1.0
    $ katDay4 = False
    $ day4 = False
    scene bg recepcao
    if jogador1:
        with fadeA
    else:
        with fadeL

    n "Você chega ao prédio de Katarina, e vai até o escritório."
    n "Aparentemente não há ninguém, mas a porta da recepção está aberta."
    menu:
        "Katarina?":
            n "Você ouve uma voz robótica vindo da mesa de Cláudia"
            "Voz robótica" "Katarina não se encontra, por favor, deixe seu recado, e tente novamente mais tarde."
            n "Aparentemente é alguma assistente virtual."
            n "Talvez Cláudia tenha sido substituída, mas é estranho que isso tenha acontecido tão repentinamente."
        "Cláudia?":
            n "Você ouve uma voz robótica vindo da mesa de Cláudia"
            "Voz robótica" "Prazer! Eu sou a Cláudia, como posso te ajudar?"
            n "Definitivamente não é a Cláudia que você conhece, você prefere ignorar."
    scene bg escritorio
    n "Ao adentrar o escritório, tudo parece normal."
    n "Mas realmente não há ninguém."
    menu:
        "Investigar mesa de Cláudia":
            jump k4a1
        "Investigar escritório de Katarina":
            jump k4b1

label k4a1:
    show bg recepcao
    n "Você vai até a mesa da Cláudia, as gavetas parecem vazias, mas o computador está ligado."
    n "Ele está bloqueado"
    if cartaoVisita:
        n "Por sorte, você se lembra de que possivelmente tem a senha."
        n "Ao tentar o código atrás do cartão de visita, o computador é desbloqueado."
        n "O e-mail está aberto no navegador, em uma mensagem com o nome"
        n "\"Desligamento\"."
        n "Nele, há um documento anexo, e uma pequena mensagem de Katarina à Cláudia."
        pag "Querida Cláudia, estou passando por um momento difícil, e cheguei a conclusão de que a sua demissão seria o melhor para nós duas, principalmente para você."
        pag "Obrigado por todos esses anos, e por também ser a minha psicóloga, por mais que eu acredite que isso tenha pirado nós duas."
        pag "Você continuará sendo paga até que encontre um emprego, fiz recomendações a algumas amigas, acredito que não ficará desempregada por muito tempo,"
        pag "mas preciso que pegue as suas coisas e saia do escritório imediatamente."
        pag "Peço perdão, mas tem que ser assim."
        pag "Atenciosamente, Katarina Kabrera."
        nvl clear
    else:
        n "Parece que não há muito mais a ser feito."
    jump k4m1

label k4b1:
    scene bg escritorio
    n "Você vai até o escritório de Katarina, ele parece em ordem."
    n "O computador está ligado, as luzes estão acesas, é como se Katarina tivesse saído às pressas."
    if jogador1:
        if k.azul > 10:
            jump k4a2
        else:
            jump k4b2 
    else:
        if k.laranja > 10:
            jump k4a2
        else:
            jump k4b2
            
label k4a2:
    n "Você não deixa de notar um grande álbum na mesa, com fotos de Katarina e seu pai"
    n "Ao seu lado, há um revólver, com apenas uma bala no barril."
    n "Você prefere não pensar muito sobre isso."
    jump k4m1

label k4b2:
    n "Você não nota nada de diferente, é um escritório excêntrico."
    jump k4m1

label k4m1:
    n "Seu telefone começa a tocar."
    n "É o Gatovaldo, ele exige que você volte imediatamente para a base."
    $ finalkat = True
    jump finalkat4

label finalkat4:    
    if jogador1:
        $ jogador1kat4 = True
    else:       
        $ jogador2kat4 = True
    jump finalale1