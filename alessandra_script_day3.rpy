###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 3--------------- ##############################################
########################################################################################################################### 

label d3ale1:

    play music "atelie_intro.ogg" volume 1.0
    queue music "atelie_loop.ogg"
    $ aleDay3 = False
    scene bg atelie

    if jogador1:
        with fadeA
    else:
        with fadeL

    n "Você chega no ateliê de Alessandra, usando roupas adequadas, de acordo com o convite formal que ela havia feito a você"

    show alessandra default

    a "Ah! Você chegou!"
    n "Ela te aguarda em frente a porta"
    a "Sei que foi meio do nada, falaram que eu poderia convidar quem eu quisesse e como estamos livres de missões, pensei: por que não?"
    menu:
        "Minhas vestes estão adequadas?":
            a "Ah, meio que não. Mas ninguém vai perceber, relaxa!"
            a "As pessoas estarão preocupadas com as exibições"
        "Devo me preparar para algo?":
            a "Sempre bom estar preparado para algo, seja lá o que você queira dizer."
            a "Eu levo tudo que pode ser útil para mim na minha bolsa e em compartimentos secretos do meu vestido, impossível algo me pegar de surpresa."
    a "Bem, estamos indo para o evento de lançamento de um carro, vai ter uma espécie de desfile, exposição, de algumas peças que eu desenhei."
    menu:
        "Maneiro!":
            a "Poisé! "
            a "É sempre bom ver seu trabalho sendo reconhecido, eu sempre me esforço para fazer tudo da forma que deveria ser."
        "E a gente vai roubar o carro, né?":
            a @seria2 "Ah, meio que mancharia um pouco a minha imagem, então evitaremos isso."
            $ roubarCarro = True
            a "Mas não é uma possibilidade descartada!"

    a "Acho que é bom irmos logo, não quero me atrasar"
    n "Alessandra assovia"
    n "Uma lamborghini vira a esquina cantando pneu"
    a "Quero passar uma boa impressão! Meu amigo vai dirigindo"
    if medidasAlteradas:
        a "Só espero que ele não se atrase novamente."
        a "Da última vez deu uma desculpa falando que eu estava no lugar errado..."
        a "Que absurdo, aposto que ficou horas arrumando o cabelo dele."
    menu:
        "Como você conseguiu uma fucking lamborghini?":
            a @smirk "É dele! Mas pode ser minha, a gente fez uma aposta, você vai descobrir no momento certo."
        "Nós três vamos caber nela?":
            a "Puts, não pensei nisso, qualquer coisa você vai no porta malas."

    n "A lamborghini para na frente de vocês, o vidro abaixa"
    show alessandra default at left
    n "Um homem de topete e oculos escuro da um sorrisinho"
    show danran default at right
    a "Danran! Como vai, amigo?"
    n "Ele faz um sinal de joia com a mão"
    a "Ele perdeu uma aposta, ta sem poder falar por um mês"
    n "Ele pega um papel e começa a escrever nele"
    n "Ele mostra o papel, está escrito:{p}\"Ou até eu ganhar a próxima aposta\""
    show alessandra smirk with dissolve
    a "Haha, você acha mesmo que vai ganhar alguma?"
    a "Ele é meio bobinho, não liga."
    show alessandra default with dissolve
    a "Ah, aliás, cabe 3 nesse carro?"
    n "Danran escreve no papel: \"Só se for no porta malas\""
    show alessandra brava2 with dissolve
    a "Droga, é, você vai ter que ir no porta malas, espero que não se importe"
    n "Você vai triste até o porta malas"
    n "Ele é minúsculo, e por algum motivo tem uma cartela de ovos dentro dele"
    show alessandra smirk with dissolve
    a "Tamo brincando contigo, po! tem um espacinho atrás dos bancos, acho que eu consigo me espremer nele, pode ir na frente."
    n "Vocês se acomodam no carro, Danran sai cantando pneu em direção ao evento"

    scene bg evento
    play music "audio/evento.wav" volume 1.0
    n "Após uma viagem longa e repleta de sinais vermelhos cortados, vocês chegam a um grande salão de eventos, isolado"
    n "Há muitos carros de luxo estacionados, limousines chegam e saem deixando pessoas"
    show alessandra sorriso at left
    a "Uau, Isso aqui tá um arraso, concordan Dan?"
    show danran default at right
    n "Dan acena com a cabeça"
    n "Vocês adentram o espaço de de eventos, é gigantesco, tudo está muito bem decorado"
    a "Tantas coisas para fazer, alguma sugestão Dan?"
    n "Dan aponta para o bar"
    show alessandra default with dissolve
    a "Nah, pode ir para lá se você quiser, eu to fora"
    hide danran with moveoutleft
    show alessandra default at center with move 
    a "E você, alguma sugestão?"
    menu:
        "Vamos comer":
            jump a3a4
        "Vamos ver os carros":
            jump a3b4
        "Vamos ver o desfile":
            jump a3c4


##Rota da comida##

label a3a4:
    n "Vocês vão em direção à mesa das comidas, tudo parece muito caro e bem preparado"
    show alessandra surpresa with dissolve
    a "Caramba, eu tinha esquecido que comidas poderiam ser boas assim."
    if jogador1 and jogador1Ale1:
        a "Aliás, lembra aquele negócio que eu tinha te falado no restaurante?
Da comida de lá ter um gosto familiar e tal"
    elif not jogador1 and jogador2Ale1:
        a "Aliás, lembra aquele negócio que eu tinha te falado no restaurante?
Da comida de lá ter um gosto familiar e tal"
    else: 
        "Aliás, acho que preciso te contar uma coisa"
    show alessandra seria with dissolve
    a "Por todo esse tempo que eu fiquei sumida, eu não estava no meu ateliê, como eu sempre digo."
    a "Eu fui raptada, encarcerada e passei X anos da minha vida dentro de um quarto."
    a "Eles não faziam nada comigo, apenas me alimentavam, a comida não era ruim, mas o gosto ficou guardado na minha mente"
    show alessandra triste with dissolve
    a "Você não deve imaginar o quanto é agoniante passar anos da sua vida enclausurada em um quarto"
    menu:
        "Por que fizeram isso?":
            show alessandra default with dissolve
            a "Eu já fui uma pessoa muito importante, poderiam ter feito pior, eu acho que tive sorte."
        "Como você saiu de lá?":
            show alessandra seria with dissolve
            a "Eu cansei, descobri falhas deles, matei um por um, fugi."
            a "Lógico que não acabei com todos, ainda vivo com a sensação de estar sendo perseguida."
    n "No momento em que Alessandra diz isso, você percebe um ponto vermelho de um laser na testa dela"
    n "Você a empurra, um tiro passa por vocês e atinge uma pessoa ao fundo"
    show alessandra medo2 with dissolve
    #Aqui a musiva poderia mudar né?
    n "Uma confusão generalizada começa, vocês escutam tiros, pessoas correndo e gritando"
    n "Você percebe alguns seguranças mortos, pessoas com roupas táticas andam no meio da multidão, atirando em quem entre no caminho"
    n "Eles estão indo diretamente até vocês."
    n "Você olha para Alessandra, ela está em choque"
    n "Você percebe uma certa inconformidade no olhar assustado dela"
    show alessandra brava with dissolve
    a "I-isso não pode ficar assim, isso n-não pode ficar assim"
    n "Você percebe que o lugar seguro mais próximo de vocês é a cozinha."
    menu:
        "Vamos para a cozinha!":
            show alessandra seria
            n "Alessandra parece acordar de um transe, ela agarra no seu braço e corre até a cozinha"
        "O que a gente faz?":
            show alessandra seria
            n "Alessandra olha ao redor"
            n "Ela percebe que o lugar seguro mais próximo de vocês é a cozinha"
            n "Ela agarra no seu braço e corre até lá"
    n "Vocês chegam à cozinha, desviando de balas"
    show alessandra brava with dissolve
    menu:
        "Algo para mim?":
            n "Você tenta chamar por ela algumas vezes, mas ela parece não te ouvir."
            n "A melhor alternativa parece ser procurar por algo"
            jump a3m1
        "Procurar algo na cozinha":
            jump a3m1
label a3m1:
    n "Você começa a procurar por algo que possa ser útil, e acha algumas coisas"
    menu:
        "Pegar um lança chamas":
            jump a3a7
        "Pegar facas de arremesso":
            jump a3b7

label a3a7:
    n "Você pega um maçarico potente que equivale a um lança chamas"
    n "Ele tem um interruptor que define o modo em que ele está"
    n "Você muda do modo \"Flambar\" para o modo \"Incendiar\""
    a "Uma ajudinha aqui?"
    n "Alessandra percebe o seu lança chamas, ela dá um sorriso e faz um sinal de aprovação com a cabeça"
    show alessandra smirk
    a "Vamos nessa."
    n "Vocês saem da cozinha, Alessandra parece ter matado alguns dos mercenários já"
    a "Atrás de você!"
    hide alessandra
    $ mercenarioFogo = True
    image mercenario = "mercenario.png"
    image mercenario center = Image("mercenario.png")
    show mercenario center
    $ acaojogo = "lançar chamas"
    $ tirosNecessarios = 0
    jump start_minigame

label a3a7acertou:
    n "Você vira de costas e, antes que um deles consiga te acertar uma facada, você liga o lança chamas"
    n "O mercenário grita enquanto é queimado até a morte"
    $ ajudou = True
    jump a3m2

label a3a7errou:
    n "Alessandra rapidamente acerta um tiro nele"
    a "Não vou estar sempre aqui para te proteger, toma cuidado."
    jump a3m2

label a3b7:
    n "Você pega algumas facas de cozinha que parecem aerodinamicas o suficiente para serem arremessadas"
    a "Uma ajudinha aqui?"
    show alessandra smirk
    n "Alessandra percebe as facas, ela dá um sorriso e faz um sinal de aprovação com a cabeça"
    a "Boa escolha."
    n "Vocês saem da cozinha, Alessandra parece ter matado alguns dos mercenários já"
    n "Você percebe mais alguns flanqueando vocês"
    $ mercenarioFaca = True
    image mercenario = "mercenario.png"
    image mercenario center = Image("mercenario.png")
    show mercenario center
    $ acaojogo = "arremessar facas"
    $ tirosNecessarios = 3
    jump start_minigame

label a3b7pontos:
    hide mercenario
    if fable_minigame_score == 1:
        n "Você arremessa suas facas, erra a maioria, mas uma acerta um dos mercenários bem na testa"
        n "Ele cai morto, Alessandra da um jeito nos outros que estavam ali"
    if fable_minigame_score == 2:
        n "Você aremessa suas facas, uma acerta no pescoço de um dos mercenários, outra perfura o olho de um deles"
        n "Eles caem mortos, Alessandra da um jeito nos outros que estavam ali"
    if fable_minigame_score == 3:
        n "Você arremessa suas facas, uma delas acerta uma granada de um dos mercenários, que explode, matando outros dois"
        n "Pedaços deles voam e caem perto de vocês, Alessandra da um jeito no outro que estava ali"
        $ ajudou = True
    if fable_minigame_score == 4:
        n "Você aremessa suas facas magistralmente, todas elas acertam as cabeças dos mercenários que flanqueavam vocês"
        show alessandra assustada
        n "Eles caem mortos, Alessandra parece assustada com a sua habilidade"
        $ ajudou = True
    if fable_minigame_score == 0:
        n "Você não acertou nenhuma faca, voce talvez não devesse ser permitido manusear nem mesmo uma faca de mantega"
        n "Felizmente a Alessandra consegue dar um jeito em todos os mercenários próximos"
        a "Você deveria escolher algo que você sabe usar."
    show alessandra eyeroll with dissolve
    a "Eu não aguento mais isso..."
    jump a3m2

##Rota da exposição de carros##

label a3b4:
    n "Vocês vão até a exposição de carros"
    n "Vocês não entendem muito de carros, eles parecem carros, como todos os outros"
    show alessandra seria with dissolve
    if jogador1:
        a "Sabe, [nome1], eu sei que hoje deveria ser um dia de confraternização, mas eu não consigo me sentir assim" 
    else:
        a "Sabe, [nome2], eu sei que hoje deveria ser um dia de confraternização, mas eu não consigo me sentir assim"
    show alessandra seria2 with dissolve
    a "Minhas missões são cada vez mais perigosas, eu sinto como se eu estivesse sendo mandada para a morte"
    a "Eu sei que o intuito de estarmos aqui é lutar, mas eu já lutei demais"
    show alessandra triste
    a "Eu acho que vou sair"
    menu:
        "Não! Por que?":
            a "Eu me sinto perseguida"
            show alessandra seria2 with dissolve
            a "Você não sabe pelo o que eu tive que passar nos últimos anos"
            show alessandra triste with dissolve
            a "Eu só não aguento mais."
            a "Sinto como se estivesse cada vez mais perto do responsável por..."
        "Falta tão pouco!":
            a "Eu sei, e isso é o que me preocupa"
            menu:
                "Você está com medo dos ratos?":
                    a "Os ratos? Não! Esses ratos são bobos, eu dou um pau neles, meu medo é..."
                "Mas você luta tão bem" if jogador1 and jogador1Ale2:
                    a "Eu sei! Mas não sei até que tipo de ameaça minhas habilidades são úteis, receio que enfrentaremos..."
                "Mas você luta tão bem" if not jogador1 and jogador2Ale2:
                    a "Eu sei! Mas não sei até que tipo de ameaça minhas habilidades são úteis, receio que enfrentaremos..."
                "Mas você é tão inteligente" if jogador1 and jogador1Ale1:
                    a "Eu sei! Mas não sei até que tipo de ameaça minhas habilidades são úteis, receio que enfrentaremos..."
                "Mas você é tão inteligente" if not jogador1 and jogador2Ale1:
                    a "Eu sei! Mas não sei até que tipo de ameaça minhas habilidades são úteis, receio que enfrentaremos..."

    n "Antes que Alessandra termine, você percebe um ponto vermelho de um laser na testa dela"
    n "Você a empurra, um tiro passa por vocês e atinge uma pessoa ao fundo"
    show alessandra medo2 with dissolve
    #Aqui a musiva poderia mudar né?
    n "Uma confusão generalizada começa, vocês escutam tiros, pessoas correndo e gritando"
    n "Você percebe alguns seguranças mortos, pessoas com roupas táticas andam no meio da multidão, atirando em quem entre no caminho"
    n "Eles estão indo diretamente até vocês."
    n "Você olha para Alessandra, ela está em choque"
    n "Você percebe uma certa inconformidade no olhar assustado dela"
    show alessandra brava with dissolve
    a "I-isso não pode ficar assim, isso n-não pode ficar assim"
    n "Você percebe que o lugar seguro mais próximo de vocês são os carros"
    menu:
        "Entra em um carro!":
            $ carrosSeparados = True
            jump a3a10
        "Vamos para esse carro!":
            $ carrosJuntos = True
            jump a3b10
label a3a10:
    n "Alessandra parece acordar de um transe, ela corre até um dos carros e entra nele"
    hide alessandra with moveoutleft
    n "Ela abre o teto solar, tira duas pistolas do vestido e começa a atirar nos mercenários"
    n "Você corre até outro carro"
    menu:
        "Procurar por algo":
            n "É um carro para exposição, não tem absolutamente nada de especial escondido dentro dele"
            menu:
                "ligar o carro":
                    jump a3b11
        "Ligar o carro":
            jump a3b11

label a3b10:
    n "Alessandra parece acordar de um transe, ela corre até um dos carros junto de você e entra nele"
    n "Sem dizer uma palavra, ela tira duas pistolas do vestido, abre o teto solar e começa a atirar nos mercenários"
    menu:
        "Procurar por algo":
            n "É um carro para exposição, não tem absolutamente nada de especial escondido dentro dele"
            menu:
                "ligar o carro":
                    jump a3b11
        "Ligar o carro":
            jump a3b11


label a3b11:
    if roubarCarro:
        a "Liga o carro logo!"
        if jogador1:
            azul "Achei que iríamos evitar roubar carros"
        else:
            laranja "Achei que iríamos evitar roubar carros"
        a "Eu avisei que não era uma possibilidade descartada!"
    n "Você liga o carro, Alessandra continua atirando, mas são muitos, até que você tem uma ideia."
    hide alessandra
    image carroPrimeiraPessoa = "carroPrimeiraPessoa.png"
    $ mercenariosCarro = True
    image mercenario = "mercenario.png"
    image mercenario center = Image("mercenario.png")
    show mercenario center
    show carroPrimeiraPessoa
    $ acaojogo = "acelerar"
    $ tirosNecessarios = 5
    jump start_minigame

label a3a12pontos:
    hide mercenario
    if fable_minigame_score == 0:
        n "Você acelera com o carro em direção aos mercenários mas não acerta nenhum."
    else:
        n "Você acelera com o carro em direção aos mercenários e atropela [fable_minigame_score] deles."
        if fable_minigame_score > 4:
            $ ajudou = True
    
    if carrosSeparados:
        n "Alessandra parece gostar da sua ideia, ela fecha o teto solar e acelera em disparada com o carro"
        n "Ela atropela alguns dos mercenários que você deixou para trás"
        n "Precisamos dar o fora daqui!"
    if carrosJuntos:
        n "Eles atiram em você, sorte sua que uma das inovações do carro que está sendo exposto é a sua incrível blindagem"
        n "Alessandra continua atirando, vocês conseguem matar a maioria deles"
        a "A gente tem que vazar!"
    
    n "Vocês correm com os carros pelo evento procurando por uma saída do enorme galpão"
    n "As saídas parecem blindadas, tentar atravessar elas com os carros seria suicídio" 
    n "O combustível dos carros começa a acabar"
    if carrosSeparados:
        n "Vocês descem dos carros e procuram por abrigo"
    if carrosJuntos:
        n "Vocês descem do carro e procuram por abrigo"
    hide carroPrimeiraPessoa
    show alessandra brava
    a "Merda, a gente ta fudido"
    jump a3m2

##Rota do desfile##

label a3c4:
    n "Vocês vão até o desfile"
    n "As pessoas desfilando vestem roupas vermelhas e brancas, com detalhes rasgados e assimétricos"
    show alessandra triste
    n "Alessandra não parece muito feliz muito feliz com suas criações"
    menu:
        "Por que está assim?":
            a "Foi um doloroso processo criativo."
        "Você não gostou do que fez?":
            a "Pode parecer que não, mas eu me sinto orgulhosa por tudo isso"
    a "Algo tem me atormentado, há um tempinho já..."
    a "O nome dessa coleção é \"Souvenirs de Prison\""
    a "É sobre uma época sombria da minha vida, a qual superei recentemente"
    menu:
        "O que isso significa?":
            a "Eu prefiro o nome em português mesmo, é \"Memórias do Cárcere\""
            jump a3a14
        "Entendi...":
            jump a3a14

label a3a14:
    n "Você começa a perceber os detalhes dos designs de Alessandra, as manchas de sangue, os buracos de bala, os rasgos"
    a "É... Não foi tão violento assim, tomei diversas liberdades artísticas no processo criativo dessa coleção."
    a "O que me preocupa é que..."
    a "Acho que alguns fantasmas insistem em me assombrar"
    n "Você passa a perceber os detalhes de uma maneira diferente, os buracos de bala parecem mais realistas, o sangue mais real"
    n "Uma das modelos desfilando cai no chão, \"Que atuação!\", você pensa, todas as angústias internas de Alessandra sendo representadas por roupas"
    n "Quando você se liberta de seus pensamentos e olha para ela, você a vê aterrorizada"
    show alessandra medo1
    a "E-estão..."
    n "Ela te agarra e se joga no chão contigo"
    n "Um tiro, que deveria ter te acertado, passa por ti"
    n "Pessoas vestindo roupas táticas começam a invadir o saguão, atirando em tudo que entre no caminho"
    n "Eles estão indo diretamente até vocês."
    show alessandra medo2
    n "Você olha para Alessandra, ela está em choque"
    n "Você percebe uma certa inconformidade no olhar assustado dela"
    show alessandra assustada
    a "I-isso não pode ficar assim, isso n-não pode ficar assim"
    show alessandra seria
    n "Alessandra parece acordar de um transe, ela procura por cobertura e te puxa para lá"
    a "Toma."
    n "Ela te dá uma espingarda, que de alguma forma estava anexada em algum módulo secreto de seu vestido"
    a "A gente consegue."
    show alessandra smirk
    n "Ela te diz com confiança, enquanto tira duas pistolas de seu vestido e abre fogo contra os mercenários"
    $ mercenariosShotgun = True
    image mercenario = "mercenario.png"
    image mercenario center = Image("mercenario.png")
    show mercenario center
    $ acaojogo = "atirar"
    $ tirosNecessarios = 5
    jump start_minigame

label a3a14pontos:
    hide mercenario
    if fable_minigame_score == 6:
        n "Você mira e acerta cada um dos mercenários como se o tempo não existisse, eles caem um por um"
        $ ajudou = True
    if fable_minigame_score == 5:
        n "Você se esforça e atira com precisão, acertando a maioria dos mercenários."
        n "A espingarda que Alessandra te dá parece modificada, seus tiros arrancam pedaços violentamente desses assassinos, o que torna esse serviço muito mais fácil"
        n "Mas que também tem um custo mental igualmente alto"
        $ ajudou = True
    if fable_minigame_score > 0 and fable_minigame_score < 5:
        n "Você atira contra os mercenários, eles são rápidos e habilidosos, mas você consegue acertar alguns deles, [int(fable_minigame_score/2)] tiro(s) pega(m) de raspão em ti"
        n "A espingarda que Alessandra te dá parece modificada, seus tiros arrancam pedaços violentamente desses assassinos, o que torna esse serviço muito mais fácil"
        n "Mas que também tem um custo mental igualmente alto"
    if fable_minigame_score == 0:
        n "Você está muito assustado com a situação, e não consegue acertar nenhum dos mercenários."
        n "3 tiros de acertam de raspão, você está bastante machucado"
        n "Alessandra te arrasta para uma cobertura melhor, alguns mercenários ainda estão vivos, e continuam atirando em vocês"
        a "Meu Deus! Você está bem? Espera aí."
        n "Ela tira um kit de primeiros socorros do vestido e começa a limpar suas veridas e a suturar seus machucado"
        n "Dói, mas você se sente relativamente melhor"
        n "Alessandra definitivamente é habilidosa com agulhas"
        a "A gente precisa te tirar daqui"
    n "Alessandra te puxa para uma cobertura mais segura"
    a "São muitos, a gente tá quase conseguindo, fica firme."
    jump a3m2

label a3m2:
    n "Danran aparece, ele acaba com os últimos mercenários que restavam"
    d "Alê, você está bem?"
    n "Ele corre até Alessandra e abraça ela"
    a "Estou sim, eu sempre esperei por isso, mas nunca de fato acreditei que aconteceria."
    a "Você voltou a falar, que aposta eu perdi?"
    d "Que hoje não ia chover"
    n "Dan aponta para a janela, está caindo um toró"
    a "Ah, droga."
    d "A polícia está vindo, a gente tem que ir"
    d "Eu conheço uma saída que nos leva até o meu carro"
    n "Vocês correm até o carro, e voltam para a cidade"
    n "No caminho, silêncio. O clima é tenso, e ninguém diz uma palavra"
    n "Eles te deixam na sua casa, Alessandra olha para você, e com um rosto abatido"
    a "A gente se vê amanhã."

    if jogador1:
        $ jogador1Ale3 = True
    else:       
        $ jogador2Ale3 = True
    if ajudou:
        achieve atentado
    jump finalale1 