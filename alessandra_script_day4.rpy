###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 4--------------- ##############################################
########################################################################################################################### 

label d4ale1:
    play music "atelie_intro.ogg" volume 1.0
    queue music "atelie_loop.ogg"
    $ aleDay4 = False
    $ day4 = False
    scene bg atelie
    if jogador1:
        with fadeA
    else:
        with fadeL
    
    n "Você vai até o ateliê de Alessandra, a porta está fechada"
    menu:
        "Bater na porta":
            n "Você dá um socão na porta"
            n "A sua mão dói bastante."
        "Bater à porta":
            n "Você bate à porta, e aguarda por uma resposta"
            n "Mas ninguém atende."
        "Bater a porta":
            n "Você abre a porta, e fecha ela com tudo, causando um estrondo."
            n "Você para por um instante e reflete sobre o que acabou de fazer."

    n "No final das contas, a porta estava destrancada."
    n "Você a abre."
    n "Tudo está uma bagunça, você encontra roupas rasgadas, projetos em pedacinhos."
    n "Não há ninguém."
    menu:
        "Investigar escritório de Alessandra":
            jump a4a1
        "Investigar o salão":
            jump a4b1

label a4a1:
    n "Você vai até um pequeno escritório no canto do salão, a porta está trancada."
    if chavegotica:
        n "Você se lembra de uma pequena chave gótica que foi encontrada nos CDs da Alessandra"
        n "Ela parece combinar bem com a porta"
        n "Você utiliza uma pequena chave que havia encontrado, ela destranca a porta."
        n "Diferentemente do restante do recinto, o escritório parece em ordem."
        n "Há um grande quadro de evidências nele, com pistas que você não compreende a princípio."
        n "Porém, no centro dele, há uma grande foto de Gatovaldo, sendo cortado por um grande X vermelho."
    else:
        n "Você tenta forçá-la, mas ela parece ser bastante resistente."
    jump a4m1

label a4b1:
    n "Você começa a investigar o grande salão do ateliê."
    n "No meio de tantas roupas destroçadas, há um manequim que se destaca por ainda estar de pé."
    n "Nele, há um look visceralmente impactante"
    n "É um desperdício Alessandra não estar utilizando-o hoje, e é difícil entender por que ele é a única coisa intacta ali"
    n "Você percebe nele uma pequena etiqueta dourada com seu nome:"
    n "{i}{color=#f00}V{/color}endetta, {color=#f00}N{/color}oncompliance, {color=#f00}M{/color}urder.{/i}"
    n "É um nome um tanto dramático." 
    n "Você reflete sobre o motivo de Alessandra fazer um design exclusivo somente para o dia da revolta."
    n "Parece não fazer muito sentido."
    jump a4m1

label a4m1:
    n "Seu telefone começa a tocar."
    n "É o Gatovaldo, ele exige que você volte imediatamente para a base."
    $ finalale = True
    jump finalale4



label finalale4:    
    if jogador1:
        $ jogador1ale4 = True
    else:       
        $ jogador2ale4 = True
    jump finalale1