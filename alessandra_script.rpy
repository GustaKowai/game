###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 1--------------- ##############################################
########################################################################################################################### 


label d1ale1:
    play music "atelier.mp3" volume 0.5
    $ aleDay1 = False
    scene bg atelie
    if jogador1:
        with fadeA
    else:
        with fadeL
    
    n "Você chega em um prédio antigo, em um bairro estranho da cidade, ele ao mesmo tempo parece confortante e assustador, ao passar pela entrada, um sininho toca em cima de você"
    menu:
        "Tem alguém ai?":
            $ alguem = True
            jump a1a
        "Alessandra?":
            jump a1a1

label a1a:
    n "Silêncio"
    menu:
        "Alessandra?":
            jump a1a1
        "Senhorita Mallet?":
            jump a1a1
label a1a1:
    n "Você sente algo estranho, como se estivesse sendo observado."
    n "Quando decide olhar para trás..."
    if alguem:
        "Nunca diga \"Tem alguém ai?\", já assisti filmes de terror o suficiente." 
        "{cps=*0.2}Trás má sorte. {/cps}"
    
    show alessandra default
    with moveinbottom
    if alguem:
        a "To zoando!"
    a "Eae cara, estamos preparados para a missão?"
    a "Só aguardar aqui fora, o transporte já já chega."
    a "Engraçado que você nem percebeu que eu estava escondida atrás da porta quando entrou, gosto de assustar as pessoas as vezes, é engraçado."
    a "Sabe, as vezes tudo que a gente precisa é de um pouco de emoção, vivemos nossas vidas monótonas repetindo o mesmo ciclo dia após dia, é bom as vezes ter um motivo maior para se preocupar com a sua própria vida"
    a "Aposto que você se assustou de verdade, olha a minha cara de louca! To branca igual um vampiro.{w} Não saia desse lugar há anos e quando saia era para comprar miojo ou energético de madrugada no mercadinho 24 horas." 
    
    a "Minha sorte é que a minha fama não chegou aqui nas periferias, ser reconhecida nunca foi um problema aqui, esse é o lugar perfeito"
    n "Uma limousine estaciona em frente ao atelie, e por um momento você se questiona se está vestido adequadamente"
    
    n "Alessandra mexe no vestido dela em algo que você não consegue decifrar" 
    
    show alessandra feliz
    n "De repente, partes do look que estavam escondidas se revelam e ela fica com uma aparencia mais ousada, amedrontadora e claro, estilosa, {w}agora você tem certeza que não está vestido adequadamente para a ocasião"
    a "Vamos! Parece que o Giuseppe já chegou"
    menu:
        "Você tem algo adequado para eu me vestir?":
            jump a1a2
        "A gente não ia só se encontrar com um informante em um local público?":
            jump a1b2
label a1a2:
    a "Ah sim, claro!"
    show alessandra default at offscreenright
    with moveoutright
    n "Ela entra no atelie... {nw}"
    
    show alessandra default at center
    with moveinright
    
    extend "E volta com um vestido tie-dye"
    a "Está na moda."
    n "Você veste o vestido e não se sente na moda..."
    n "Mas já que ela diz..."
    jump a1m1

label a1b2:
    a "Sim! No restaurante de luxo com a reserva mais disputada da cidade, você não tem noção de quantos celulares ligando ao mesmo tempo eu precisei para conseguir isso!"
    jump a1m1

label a1m1:
    a "Bom! agora vamos!"
    n "Vocês entram na limousine, ela leva vocês até um bairro de alta classe" 
    
    scene bg restaurante
    with gatodissolve
    
    n "E para em frente a um estabelecimento que se parece com um palácio"
    show alessandra feliz
    a "Chegamos! Bem vindo ao Ardórsia"
    n "Ao entrar no restaurante, vocês são direcionados a uma mesa um pouco afastada, há uma mulher loira se apresentando em um pequeno palco"
    show alessandra brava
    a "Droga, pensava que a Taylor Swift seria amanhã, nosso amigo traficante escolheu um péssimo dia para o encontro"
    a "O gatinho te passou o briefing da missão? A gente está aqui para trocar esse diamante do jared leto em uma tecnologia importada extremamente letal." 
    
    a "Basicamente ela é capaz de transformar qualquer coisa em tofu, e não sei se você sabe, mas ratos odeiam tofu." 
    
    a "Não é queijo de verdade."
    menu:
        "Jared Leto?":
            jump a1a3
        "Taylor Swift?":
            jump a1b3
label a1a3:
    a "É, poxa, ele já fez parte de um visual que eu desenhei para ele, aquele cara da banda 30 minuto para o fim do mundo ou sei lá o que, é o que daremos em troca pela arma"
    jump a1m2
label a1b3:
    a "Hoje é sexta, pensei que colocariam alguém de mais prestígio tipo o calcinha preta."
    jump a1m2
label a1m2:
    n "Você prefere não questionar, isso já tem sido uma noite bem estranha"
    show alessandra default
    a "O quão desrespeitoso seria pedir a comida antes do nosso querido colega chegar? Estou faminta."
    menu:
        "Ele provavelmente não está nem ai para a comida":
            jump a1a4
        "Seria extremamente desrespeitoso e você com certeza acabaria com o nosso plano inteirinho por conta dessa sua atitude egoísta":
            jump a1b4
        "*Chamar o garçom* Eu não me importo.":
            jump a1c4
label a1a4:
    n "Ela chama o garçom"
    show alessandra default at right
    with move
    show garcom default at left
    with moveinleft
    
    gar "Pois não?"
    a "Gostaria de um frango picatta com uma salada ao lado, para ele pode ser a mesma coisa"
    hide garcom
    with moveoutleft
    jump a1m3
    
label a1b4:
    a "Você me faz lembrar o motivo de eu ter me isolado, conviver com pessoas é difícil quando elas pouco se importam em tratar os outros com o mínimo de respeito, mas quer saber? Eu to cagando!"
    jump a1a4
label a1c4:
    n "O garçom se aproxima da mesa"
    show alessandra default at right
    with move
    show garcom default at left
    with moveinleft
    gar "Pois não?"
    n "Você faz o pedido para a mesa, mas não tem a menor ideia do que está pedindo, é um menu complexo"
    hide garcom
    with moveoutleft
    jump a1m3
    
label a1m3:
    show alessandra brava at center
    with move
    a "Que tédio"
    a "Lugares como esse me fazem lembrar do motivo de eu ter sumido dos holofotes, cheio de pessoas mesquinhas, que se acham superiores por simplesmente terem conseguido uma reserva."
    a "Eu vou ser bem sincera, a comida daqui nem é a melhor da cidade, e não estou dizendo que prefiro fast food ou um prato feito, existem lugares chiques que preparam pratos muito melhores e que tem um atendimento incomparavel ao daqui." 
    
    a "mas por algum motivo essa bodega aqui recebe todo o holofote" 
    
    a "Se não tivesse sido a escolha pessoal do nosso colega eu teria outras 20 melhores opções de restaurantes para escolher"
    show alessandra default
    a "Mas, já que estamos aqui, aguardemos..."
    menu:
        "Vamos jogar verdade ou desafio enquanto isso":
            jump a1a5
        "Vamos pedir uma música":
            jump a1b5
label a1a5:
    a "Verdade ou desafio? Pelo amor, eu te desafio a ir até aquele garçom ali e falar que ele está servindo horrores"
    
    menu:
        "Aceitar":
            jump a1a6
        "Recusar":
            jump a1b6
    
label a1b5:
    a "Ótima ideia!"
    
    n "*Ela pega um papel e uma caneta e começa a escrever alguma coisa*"
    
    a "Toma! Leva isso para ela"
    n "Você leva o papel para a mulher no palco, ela lê e sai correndo chorando"
    show alessandra feliz
    a "Kkkkkk boa! Meus ouvidos já estavam se cansando"
    menu:
        "O que estava escrito?":
            jump a1a8
        
        "Por que você não gosta dela?":
            jump a1b8
label a1a6:
    hide alessandra
    show garcom default
    n "Você vai até o garçom..."
    n "Vocês dois se olham em silêncio por alguns segundos"
    if jogador1:
        azul "Você está servindo horrores"
    else:
        laranja "Você está servindo horrores"
    n "Ele não parece entender"
    gar "Críticas favor encaminhar à gerencia."
    hide garcom
    with moveoutright
    n "Ele sai andando em passos rápidos enxugando lágrimas nos olhos disfarçadamente"
    show alessandra surpresa
    a "Ué?? o que aconteceu? Você não falou que ele estava bem vestido?"
    a "Amei o uniforme do pessoal daqui, não entendi como alguém poderia se magoar com um elogio"
    a "Mas tudo bem, você fez o desafio, agora eu te conto uma verdade, é assim que funciona né?"
    a "Vamos lá... {w} É... "
    a "sei lá, {w}eu tenho medo de ficar sozinha..."
    show alessandra triste
    a "..."
    n "Vocês ficam em silêncio por alguns segundos"
    jump a1m4
label a1b6:
    a "Haha, eu ganhei então, né?"
    a "Agora você tem que me contar uma verdade sobre você"
    menu:
        "Eu tenho medo de tubarões":
            jump a1a7
        "Eu já quebrei os meus dois braços e minhas duas pernas":
            jump a1b7
        "Estou com o aluguel atrasado":
            jump a1c7
        "Secretamente eu gosto dos filmes do Adam Sandler":
            jump a1d7
label a1a7:
    a "E quem não tem? Bobinho... Esses bichos foram criados para fazer as pessoas borrarem as calças."
    n "Ela não sabe que você perdeu os seus pais em um ataque de tubarão dois anos atrás"
    jump a1m4
label a1b7:
    a "Nossa, você está mais remendado do que muitas roupas com que trabalhei, espero que isso não venha a nos atrapalhar."
    n "Você se arrepende de ter revelado isso"
    jump a1m4
label a1c7:
    a "Que pena, quando tudo isso acabar você pode vir morar comigo." 
    
    a "Eu te arrumo um cantinho no depósito do ateliê para você dormir, só leva o colchão e o repelente de insetos."
    n "Você prefere dormir na rua"
    jump a1m4
label a1d7:
    a "Acho que essa foi a pior coisa que você poderia ter me contado"
    n "Ainda bem que ela não sabe que o seu filme favorito dele é 'Cada Um Tem a Gêmea Que Merece'"
    jump a1m4
label a1m4:
    show alessandra assustada
    a "Eita, acho que ele chegou"
    n "Você olha para trás, e vê um homem parrudo, amedrontador, usando roupas formais, de óculos escuros, se aproximando da mesa de vocês"
    a "A gente ta fudido, olha o tamanho desse cara"
    n "Ele se aproxima em passos pesados"
    show alessandra medo1
    a "Eu vou para o banheiro e você lida com isso, tudo bem?"
    n "Alessandra está suando frio, ela parece muito nervosa, ele está cada vez mais perto"
    show alessandra medo2
    a "Cara, por que eu fui me meter nisso? {w} Aquilo é uma arma?{w} Eu vou desmaiar"

    n "Ele chega até a mesa de vocês e..."
    n "Ele passa reto"
    show alessandra surpresa
    a "..."
    show alessandra feliz
    a "Ah, acho que era o segurança..."
    traf "Oieeeee"
    show alessandra confusa
    a "O que foi isso?"
    traf "Oieeee"
    a "De onde está vindo isso??"
    n "Você percebe que, enquanto se distraiam e cagavam nas calças, uma pessoa de estatura baixa usando roupas rosas sentou-se à mesa com vocês"
    show alessandra default at right
    with move
    show traficante default at left
    
    traf "Oiee"
    jump finalale1
label finalale1:
    if jogador1:
        $ a.azul += JogadorAtivo
    else:
        $ a.laranja += JogadorAtivo
    jump whereToGo
