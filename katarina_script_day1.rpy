###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 1--------------- ##############################################
########################################################################################################################### 

label d1kat1:
    play music "escritorio.mp3" volume 0.5
    $ katDay1 = False
    scene bg recepcao
    if jogador1:
        with fadeA
    else:
        with fadeL
    n "*Você entra em uma sala de recepção com uma decoração atípica"

    n "Há uma parede cheia de cabeças de animais empalhados, com os olhos trocados por pedras preciosas"

    n "Em um balcão extravagante, próximo a duas espingardas rosas cruzadas entre o símbolo da marca de rações de katarina"

    n "Uma simpática recepcionista te atende"
    show claudia default at left
    with dissolve
    c "Boa tarde! Como posso te ajudar?"
    menu:
        "Katarina.":
            jump k1a1
        "Boa tarde, a senhorita Katarina encontra-se no recinto?":
            jump k1b1
label k1a1:
    c "KATARINA!"
    n "A recepcionista grita, mas não obtem nenhuma resposta"
    c "Peço perdão, só um instante, ela provavelmente deve estar em uma reunião importante"
    n "Ela disca um número, mas aparentemente não obtem resposta"
    c "Certo..."
    n "A recepcionista se levanta de sua cadeira e anda em direção a um grande botão vermelho escrito 'ATAQUE NUCLEAR'"
    show bg recepcao at siren_tint()
    
    play sound "alarm.wav" loop
    n "As luzes começam a piscar em vermelho e um som de alarme começa a tocar."
    c "Ela deve aparecer a qualquer instante!"
    with hpunch
    play sound "doorOpen.ogg"
    n "A porta do escritório abre escancaradamente"
   
    show katarina brava at right
    show katarina brava at siren_tint()
    with moveinright
    k "PORRA ME DIZ QUE É O MEU X-MORTADELA-MALIGNO CLAUDIA, NÃO AGUENTO MAIS ESPERAR"
    show claudia default at siren_tint()
    c  "Senhorita katarina! Essa pessoa veio procurar por ti, ela é de poucas palavras, parece ser algo importante."
    show katarina feliz at siren_tint()
    k "Ah! você faz parte do movimento, o gatovaldo me disse que apareceria."
    k "Claúdia, sempre que algum esquisito assim aparecer por aqui pode liberar direto para a minha sala"
    k "faz parte de uma nova terapia que estou experimentando"
    jump k1m1
    label k1b1:
    c @default "Ela está sim! se não se importa em esperar um pouco, ela está em sua sessão diária de Post-Generic-Slovenian-Punk-Rock."
    c "Enquanto isso, aceita um chá de camomila fervido em sangue de carneiro? é uma bebida típica sueca."
    n "Ela não aguarda por uma resposta e te serve uma xicará de um líquido viscoso esquisito..."
    n "Você definitivamente não quer tomar isso"
    c "Ah! já ia me esquecendo, com licença, preciso acender o incenso do dia, você sabe, para atrair boas energias"
    n "Ela se dirige a um armário rústico e começa a procurar em uma gaveta"
    c "Lavanda, orvalho do amanhecer, lírios holandeses, não... hoje é terça, cade o de terça? aqui! te achei, moshpit do slipknot!"
    n "Ela acende o incenso, e um cheiro de rebeldia toma conta do ambiente, você nem imaginava que seria possível perceber isso olfativamente"
    with hpunch
    play sound "doorOpen.ogg"
    n "A porta do escritório abre escancaradamente"
    show katarina irritada at right
    with moveinright
    k "Claudia, mosh pit do slipknot agora é o incenso de quinta, você não viu as alterações que eu te mandei por email?"
    c "Senhorita katarita! Peço perdão, não acontecerá novamente, já irei providenciar o incenso diário correto." 
    
    c"Ah, aliás, essa pessoa veio te procurar, ela recusou o chá sueco, eu te avisei que capim-limão ornava melhor."
    show katarina feliz
    k "Ah! Você faz parte do movimento, o Gatovaldo me disse que apareceria."
    k "Claúdia, sempre que algum esquisito assim aparecer por aqui pode liberar direto para a minha sala"
    k "Faz parte de uma nova terapia que estou experimentando"
    jump k1m1
label k1m1:
    k "Me acompanhe, meu querido, temos trabalho a fazer."
    
    scene bg escritorio
    hide claudia
    hide katarina
    with gatodissolve
    show katarina default at center
    with moveinleft
    n "Você acompanha katarina até o seu escritório, ele é recheado de esculturas bizarras e pinturas que remetem ao caos e à destruição, tudo em tons de branco e rosa"
    show katarina smirk
    k "Você parece espantado, gostou do meu cantinho? Descobri quem era o bansky e tranquei ele aqui com baldes de tinta durante 3 dias."
    k "Na verdade, 3 dias para cada vez que eu abrisse a porta e não gostasse do que estava vendo, ele acabou ficando uns 2 meses trancado aqui,{w} mas no fim o resultado foi espetacular!"
    show katarina default
    k "Ele até deu uma sumida da ruas, acho que deve ter ido procurar terapia, mas sinceramente, não entendo o porquê...{w} Minha sala tem ar condicionado e eu sempre o alimentava com minhas refeições preferidas."
    n "Você se lembra de uma aberração gastronômica sendo mencionada anteriormente..."
    n "...coitado dele"
    show katarina feliz
    k "Bem, vamos falar de negócios, sugeri ao seu chefe que a gente fosse explodir alguma coisa..."
    
    show katarina meh
    k "...mas ele achou melhor não, fiquei muito frustrada, vou ser franca contigo, entrei na revolução para explodir coisas!"
    show katarina brava
    k "Aquela ratazana imunda acha que pode simplesmente acabar com uma das minhas fontes de renda e ainda deixar milhares de gatinhos por ai com fome? Fala sério! Eu quero mais é explodir tudo mesmo"
    show katarina smirk
    k "Antes de sair, a gente precisa se conhecer um pouco. Para começar, qual é seu nome?"
    if jogador1:
        azul "Me chamo [nome1]" 
    else:
        laranja "Me chamo [nome2]"
    n "*Após dizer seu nome, ela começa a digitar e ler algumas coisas no computador dela*"
    show katarina default
    k "Huuum... Certo, já te conheço.{w} Sua vez, me faz uma pergunta"
    menu:
        "Você pesquisou informações minhas na internet?":
            jump k1a2
        "O que são aquelas cabeças empalhadas com joias no lugar dos olhos?":
            jump k1b2       
label k1a2:
    show katarina default
    k "Na realidade não, só pesquisei o significado do seu nome, isso já basta pra mim."
    k "Acho que já podemos ir, eu vou dirigindo!"
    menu:
        "Ir para a missão":
            $ JogadorAtivo += 0
            jump missaokat1
label k1b2:
    show katarina feliz
    k "Não se preocupe, elas são falsas, menos a do jacaré, a do leão, a do urso..."
    n "Ela diz mais alguns nomes"
    n "Aparentemente no máximo umas 3 delas são falsas"
    show katarina triste
    k "Eram do meu pai. Eu as herdei quando ele morreu, assim como as joias. Apenas uni as duas coisas..."
    show katarina feliz
    k "Acho que já podemos ir, eu vou dirigindo!"
    menu:
        "Ir para a missão":
            $ JogadorAtivo += 1
            jump missaokat1
label missaokat1:
    scene bg deserto
    with gatodissolve
    play music "deserto.mp3" volume 0.5
    n "Vocês dirigem até uma estrada deserta, não há nada além de um posto de gasolina abandonado e uma grande torre de telefone nas redondezas"
    show katarina irritada
    k "Que calor da porra, ainda bem que eu vim preparada"
    n "Ela tira uma garrafa de vodka da mochila"
    menu:
        "Você não deveria fazer isso em uma missão":
            $ JogadorAtivo += 0
            jump k1a3
        "Me dá um pouco?":
            $ JogadorAtivo += 1
            jump k1b3
label k1a3:
    show katarina confusa
    k "Isso o que? beber água?"
    n "Você percebe que aquilo na realidade era água, e não entende o porquê de ela usar garrafas de vodka ao invés de garrafas térmicas, parece estar bem quente"
    menu:
        "Qual é a vantagem de carregar garrafas de vidro contigo?":
            jump k1a4
        "Se jogar numa panela da pra fazer um miojo":
            jump k1b4
            
label k1b3:
    
    show katarina feliz
    k "Claro, eu tenho mais duas!"
    n "Você percebe que aquilo na realidade era água, e não entende o porquê de ela usar garrafas de vodka ao invés de garrafas térmicas, parece estar bem quente"
    menu:
        "Qual é a vantagem de carregar garrafas de vidro contigo?":
            jump k1a4
        "Se jogar numa panela da pra fazer um miojo":
            jump k1b4
label k1a4:
    
    show katarina feliz
    k "Nunca se sabe quando você irá precisar de uma arma improvisada, e além disso, você já quebrou uma garrafa para uma briga de bar? É super divertido"
    
    jump k1m2
label k1b4:
    show katarina feliz
    k "Sim! Se to no inferno vou logo abraçar o capeta.{p} Minha bebida favorita do inverno é milkshake."
    jump k1m2
label k1m2: 
    show katarina default
    k "Bem, acho que a gente ainda tem um tempo"
    k "Aliás, acho que você não deve ter a menor ideia do que a gente está fazendo aqui"
    k "Basicamente teu chefe, o gato falante, está desconfiando de uma empresa de sorvetes.{p}Ele acha que ela está realizando tráfico ilegal de queijos para a sede do governo"
    k "Você sabe, estamos sendo governados por um rato, deve ser mais barato traficar do que lidar com todos os trâmites legais e impostos para a importação desses queijos chiques para cá"
    k "Ou talvez o gatovaldo só queria tomar um sorvetinho e não estava sabendo pedir, então, caso ele esteja errado, pelo menos sairemos daqui com picolés!"
    k "Mas antes, bora naquele posto de gasolina abandonado e depois a gente sobe naquela torre telefonica pra ter uma visão melhor dos arredores e começar a se preparar"
    show bg posto
    with gatodissolve
    n "Vocês andam até o posto de gasolina abandonado..."
    n "É definitivamente um posto de gasolina..."
    n "Está definitivamente abandonado..."
    show katarina surpresa
    k "Que maneiro, parece que algumas coisas das prateleiras ainda estão aqui, bora dar uma olhada"
    n "Katarina vira de costas para você, tem uma tarântula enorme nela"
    menu:
        "AHHH (matar a aranha)":
            $ JogadorAtivo += -2
            jump k1a5
        "er... tem uma tarântula enorme nas suas costas":
            jump k1b5
label k1a5:
    with vpunch
    show katarina confusa
    k "Que porra foi essa? Por que você bateu em m... {w} Espera, isso estava nas minhas costas?"
    show katarina surpresa
    k "PUTA QUE PARIU"
    show katarina triste
    k "Não acredito que você fez isso, nunca tinha visto uma dessa espécie, que droga, argh, tudo bem, vamos entrar."
    n "Ela tira uma foto da aranha estraçalhada no chão"
    
    k "Puta que pariu... Era uma demonius Dosinfernus..."
    n "Vocês entram na loja, parece ter algumas coisas para explorar"
    
    menu:
        "Procurar nas prateleiras":
            jump k1a7
        "Procurar no caixa":
            jump k1b7
        "Procurar no banheiro":
            jump k1c7
        "Procurar no escritório":
            jump k1d7
label k1b5:
    show katarina surpresa
    k "SÉRIO? RÁPIDO, abre o segundo bolso da minha mochila, você vai entender o que fazer"
    n "Você abre o segundo bolso, tem um pote de vidro, um desodorante aerosol e um isqueiro"
    menu:
        "Tacar fogo na aranha":
            $ JogadorAtivo += -1
            jump k1a6
        "Colocar ela no pote":
            $ JogadorAtivo += +2
            jump k1b6
label k1a6:
    n "FUUUUSH"
    n "Você torra a aranha"
    show katarina brava
    k "O QUE CARALHOS VOCÊ ACABOU DE FAZER? EU FALEI O SEGUNDO BOLSO."
    show katarina triste
    k "Ah, espera, droga, acho que guardei meu lança chamas no lugar errado, que porra..."
    k "Enfim, bora entrar nessa loja conveniente"
    n "Vocês entram na loja, parece ter algumas coisas para explorar"
    menu:
        "Procurar nas prateleiras":
            jump k1a7
        "Procurar no caixa":
            jump k1b7
        "Procurar no banheiro":
            jump k1c7
        "Procurar no escritório":
            jump k1d7
label k1b6:
    n "Você coloca ela no pote, ela entra sem resistir"
    show katarina muitofeliz
    k "CARALHO, QUE FODA, É UMA DEMONIUS DOSINFERNUS, nunca tinha visto uma dessa espécie, muito obrigada! Vou levar ela para o meu zoológico particular."
    show katarina default
    k "Enfim, bora entrar nessa loja conveniente"
    n "Vocês entram na loja, parece ter algumas coisas para explorar"
    menu:
        "Procurar nas prateleiras":
            jump k1a7
        "Procurar no caixa":
            jump k1b7
        "Procurar no banheiro":
            jump k1c7
        "Procurar no escritório":
            jump k1d7
label k1a7:
    $ JogadorAtivo += 1
    n "Você procura por coisas nas prateleiras, e acha um salgadinho super ardido.{p}Ele venceu há 2 anos"
    k "Eai, algo que preste?"
    show katarina muitofeliz
    k "Caralho! esse era edição limitada, valeu!"
    jump k1m3
label k1b7:
    $ JogadorAtivo += 1
    n "Você procura por coisas no caixa, e acha uma escopeta escondida debaixo da maquina registradora"
    k "Eai, algo que preste?"
    show katarina feliz
    "Que massa, mais uma pro meu arsenal."
    jump k1m3
label k1c7:
    $ JogadorAtivo += 0
    n "Você procura por coisas no banheiro..."
    n "Parece que alguém recentemente deu um uso a ele"
    n "Você se arrepende de sua escolha"
    k "Eai, algo que preste?"
    show katarina smirk
    "Pelo seu silêncio, julgo que coisa boa não foi"
    jump k1m3
label k1d7:
    $ JogadorAtivo += 1
    n "Você procura por coisas no escritório, e acha um dvd antigo de um filme de terror trash norueguês"
    k "Eai, algo que preste?"
    show katarina feliz
    "Porra, to querendo ver esse tem meses, obrigada!"
    jump k1m3
label k1m3:
    show katarina triste
    k "Bom, eu achei isso aqui"
    n "Ela te mostra uma revista, na capa, você vê uma garota usando rosa com o seu pai, o título é: \"Sucesso entre os felinos! Pai e filha revelam alguns dos segredos  dos petiscos mais cobiçados pelos gatunos\""
    k "Eu até que gostava dele."
    k "Na realidade, eu gostava dele, mas era jovem demais para entender isso."
    k "Eu perdi mais do que um braço naquele atentado"
    menu:
        "Atentado?":
            jump k1a8
        "Meus sentimentos...":
            $ JogadorAtivo += 1
            jump k1b8
label k1a8:
    show katarina irritada
    k "Não quero falar sobre isso no momento,{p}acho que já ta na hora da gente se preparar"
    jump k1m4
label k1b8:
    show katarina triste
    k "É... obrigado.{p}Bora ir se preparar agora"
    jump k1m4
label k1m4:
    show katarina feliz
    n "Vocês vão até a torre e começam a subir nela.{w} Ela parece instável, mas a confiança e animação de katarina te passa uma segurança inexplicável" 
    
    show bg caixadagua
    with gatodissolve
    n "Após chegarem a uma certa altura, vocês se sentam na beirada, e percebem que definitivamente não há mais nada por perto além dessa torre e daquele posto de gasolina"
    k "É... Parece que a gente ta bem isolado aqui mesmo, mas vai ser bom para ver quando o caminhão estiver chegando." 
    k "Bora fazer alguma coisa enquanto isso.{p}Abre o terceiro bolso da minha mochila ai e pega alguma coisa"
    menu:
        "Pegar tabuleiro de xadrez":
            jump k1a9
        "Pegar garrafa de vodka":
            $ JogadorAtivo += 1
            jump k1b9
        "Pegar rifle de precisão":
            jump k1c9

label k1a9:
    
    show katarina feliz
    k "Ótima escolha!"
    n "Ela abre o tabuleiro, dentro dele há uma coleção de mini pingas"
    menu:
        "Pegar uma":
            $ JogadorAtivo += 1
            jump k1a10
        "Recusar":
            $ JogadorAtivo += -1
            jump k1b10
label k1b9:
    show katarina feliz
    k "Boa!! tava querendo fazer isso mesmo"
    n "Ela pega a garrafa da sua mão, a arremessa para frente e aguarda ansiosamente ela espatifar no chão "
    show katarina default
    k "Aqui é alto mesmo né"
    n "Vocês permanecem em silêncio por um tempo"
    n "Plaft"
    k "Maneiro..."
    jump k1m5
label k1c9:
    show katarina default
    k "Não sei se vai ter muito o que fazer com isso aqui, mas bora tentar, toma, ve se você acha alguma coisa"
    n "Você observa pela mira, e avista algumas coisas"
    menu:
        "Atirar em um urubu voando":
            $ JogadorAtivo += 1
            jump k1a11
        "Atirar no posto de gasolina":
            $ JogadorAtivo += 1
            jump k1b11
        "Atirar em um animal morto":
            $ JogadorAtivo += 2
            jump k1c11
        "Não atirar":
            $ JogadorAtivo += 0
            jump k1d11
label k1a10:
    show katarina feliz
    k "Toma essa aqui, é massa"
    n "Ela te da uma pinga sabor planta carnívora"
    n "Você já deveria ter aprendido a não confiar nas preferências gastronômicas dela"
    k "Feita em casa!"
    jump k1m5
label k1b10:
    show katarina meh
    k "Poxa, mas elas estao tao gostosinhas..."
    n "Ela pega uma sabor rabo de rato"
    show katarina smirk
    k "Você deve ter paladar infantil"
    jump k1m5
label k1a11:
    show katarina default
    n "Você tenta atirar em um urubu voando, mas erra"
    show katarina smirk
    k "Boa tentativa, passa isso ai pra mim"
    n "Ela pega a arma da sua mão, e atira para cima sem mirar"
    n "3 urubus caem do seu lado"
    k "Viu só?"
    jump k1m5
label k1b11:
    show katarina default
    n "Você atira em uma bomba de combustível no posto"
    n "Nada acontece"
    show katarina feliz
    k "Você é dos meus, infelizmente esse posto ai já tá desativado há um bom tempo."
    n "Mas seria daora se ele explodisse"
    jump k1m5
label k1c11:
    show katarina default
    n "Você atira em uma carcaça de coiote na distância"
    show katarina feliz
    a "Woow, não estava prestando atenção, você matou aquele bicho? Muito foda!"
    jump k1m5
label k1d11:
    show katarina default
    n "Você simplesmente não atira"
    show katarina smirk
    k "Ahh, então você é um pacifistinha? Tudo bem, nada contra,{w} tenho até amigos que são..."
    jump k1m5
label k1m5:
    n "Um som de veículo começa a ser ouvido na distância"
    show katarina surpresa
    k "Espera!{w} Acho que é o nosso caminhão se aproximando"
    n "Você observa um caminhão de sorvete se aproximando"
    show katarina feliz
    k "É isso mesmo! Bora descer"
    n "Vocês descem a torre. A escada é bem precária e você tem a sensação de quase morte ao pisar em um degrau e ele quebrar"
    show bg deserto
    with gatodissolve
    show katarina default
    k  "Olha, é o seguinte, eu sei que eu sou uma das financiadoras disso daqui, e que você provavelmente questiona muito as minhas decisões e não confia em mim, mas eu peço, deixa que eu lido com isso daqui, siga o meu plano."
    n "Ela abre a mochila, e te dá uma garrafa de ketchup"
    k "Você sabe o que fazer."
    n "Você não sabe o que fazer."
    show katarina feliz
    k "Ok, vejo na sua cara que você não sabe o que fazer. {w}Vai lá na estrada, deita e joga bastante ketchup na sua perna e perto dela, você vai chorar e gritar de dor, pedindo por ajuda"
    show katarina smirk
    k "Se ele acelerar e passar por cima de você, teremos certeza que eles trabalham para o governo e estão preparados para lidar com emboscadas"
    k "Se ele parar para te ajudar, a gente vai saber que ele provavelmente é só um motorista inocente, você irá dizer que é uma pegadinha e tudo ficará certo, pode ser?"
    menu:
        "Me sinto feliz de morrer pela causa!":
            $ JogadorAtivo += 1
            jump k1a12
        "Você quer me usar como um sacrifício humano?":
            $ JogadorAtivo += -1
            jump k1b12
label k1a12:
    
    show katarina smirk
    k "Sempre desconfiei que você fosse meio biruta, mas não, não irei deixar você morrer. Se ele acelerar eu acerto um tiro no meio da testa dele e você sai correndo, tenho uma boa mira"
    jump k1m6
label k1b12:
    show katarina surpresa
    k "Claro que não! Só estava zoando com a sua cara, eu dou um jeito pra ele não fazer isso, mas fique preparada para correr caso precise"
    jump k1m6
label k1m6:
    n "Você sente que não tem outra alternativa a não ser a confiar nela. Flashs da sua vida inteira passam pela sua cabeça, e o caminhão ainda nem está vindo na sua direção"
    hide katarina
    n "Então você vai, deita na rodovia, e espalha o ketchup porcamente na sua perna.{w} só uma pessoa muito ingênua mesmo cairia nisso"
    n "O caminhão se aproxima cada vez mais, você sente um frio na espinha mas começa a gritar por ajuda, sua atuação é terrível, nem a alma mais inocente da terra seria capaz de acreditar nisso"
    n "Ele chega a uma distância consideravelmente perto de ti... {w} ele se aproxima...{w} e de repente..."
    n "Ele para"
    n "Um senhorzinho muito fofo sai da cabine"
    show vovo default at left
    vo "Meu Deus! você está bem? o que houve?"
    
    menu:
        "É pegadinha!!!! kkkkkk caiu igual um patinho!!!":
            jump k1a13
        "*Continuar atuando*":
            jump k1b13
label k1a13:
    
    vo "O que? mas o que você está fazendo aqui nesse meio do nada?"
    jump k1m7
label k1b13:
    vo "Minha nossa! esse machucado parece estar feio!"
    jump k1m7
label k1m7:
    n "Você percebe que ele genuinamente acredita em ti e está evitando olhar para a sua perna"
    n "Você vê Katarina chegando de mansinho com um rifle e usando uma bandana na cara"
    show katarina brava at right
    k "Mãos ao alto velhote!"
    vo "Mas o que"
    k "Isso mesmo! mãos ao alto! isso é um assalto!"
    n "Ele paralisa, parece estar muito assustado"
    show katarina feliz
    k "To te zoando!"
    n "Ela abaixa a arma"
    k "É só uma pegadinha para o meu canal do youtube!"
    vo "Ah.. Haha.. Entendi... Por favor me deixem ir eu tenho familia..."
    n "Ele ainda está bem assustado"
    k "Calma! Toma aqui"
    n "Ela tira um maço de dinheiro da mochila"
    k "Me vê três picolés!"
    vo "C-claro, s-s-só preciso pegar eles ali na p-parte de trás"
    n "Vocês vão até a parte de trás do caminhão, ele entra, e sai com três picolés de baunilha"
    vo "A-aqui o troco"
    show katarina confusa
    k "Troco? Desde quando picolés são tão baratos assim? Ah quer saber, pode ficar...{p}Pelo susto, vai"

    hide vovo
    with moveoutleft

    n "O senhor entra de volta no caminhão, e sai acelerado"

    show katarina brava at center
    with move

    k "Logo o de baunilha... Que sabor mais sem graça... É, bem, ele está limpo, precisamos analisar a nossa próxima hipótese"
    menu:
        "Você mandou bem!":
            $ JogadorAtivo += 1
            jump k1a14
        "É... Acho que você precisa tomar um pouco mais de cuidado ao lidar com civis...":
            $ JogadorAtivo += -1
            jump k1b14
label k1a14:
    show katarina smirk
    k "Ah, eu sei né! Falei poxa, confia em mim!"
    jump k1m8
label k1b14:
    show katarina smirk
    k "Aquele velhote vai valorizar muito mais a vida dele depois desse susto, tava precisando parar de ser besta também, você é péssimo atuando, não sei como ele caiu naquilo!"
    
    jump k1m8

label k1m8:
    n "Vocês voltam até o carro, o picolé já está quase derretido, o calor está insuportável"
    show katarina feliz
    k "Hey, acho que a gente precisa se conhecer mais, você deve ter percebido que isso é importante para mim.{w} Tenho um problema em conviver com estranhos."
    
    show katarina smirk

    extend " Quem sabe eu não te conto mais sobre o meu pai, {w}eu sei que está curioso"
    n "Você tenta dar uma resposta, mas ela imediatamente liga o som do carro em um volume estrondoso, e começa a acelerar o carro.{p} Vocês partem"

    jump finalkat1

label finalkat1:
    if jogador1:
        $ k.azul += JogadorAtivo
    else:
        $ k.laranja += JogadorAtivo
    jump whereToGo
