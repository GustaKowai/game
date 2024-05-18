###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 1--------------- ##############################################
########################################################################################################################### 

label d1kat1:
    default escopeta = False

    play music "escritorio.mp3" volume 0.5
    $ katDay1 = False
    scene bg recepcao
    if jogador1:
        with fadeA
    else:
        with fadeL
    n "Você entra em uma sala de recepção com uma decoração atípica."

    n "Há uma parede cheia de cabeças de animais empalhados, com os olhos trocados por pedras preciosas."

    n "Em um balcão extravagante, próximo a duas espingardas rosas cruzadas entre o símbolo da marca de rações de Katarina."

    n "Uma simpática recepcionista te atende."
    show claudia default
    with dissolve
    c "Boa tarde! Como posso te ajudar?"
    menu:
        "Katarina.":
            jump k1a1
        "Boa tarde, a senhorita Katarina encontra-se no recinto?":
            jump k1b1
label k1a1:
    c "Espere um momento."
    show claudia brava at easeinzoom
    c "KATARINA!" with vpunch
    n "A recepcionista grita, mas não obtém nenhuma resposta."
    show claudia default at easeoutzoom
    c "Peço perdão, só um instante, ela provavelmente deve estar em uma reunião importante."
    n "Ela disca um número, mas aparentemente não obtém resposta."
    c "Certo..."
    hide claudia
    with moveoutleft
    n "A recepcionista se levanta de sua cadeira e anda em direção a um grande botão vermelho escrito 'AMEAÇA NUCLEAR'."
    show claudia default 
    with moveinleft
    show bg recepcao at siren_tint()
    show claudia default at siren_tint()
    
    play sound "alarm.wav" loop
    n "As luzes começam a piscar em vermelho e um som de alarme começa a tocar."
    show claudia feliz with dissolve
    c "Ela deve aparecer a qualquer instante!"
    with hpunch
    play sound "doorOpen.ogg"
    n "A porta do escritório abre escancaradamente."


    show claudia default at left
    with move
    show katarina brava at right
    show katarina brava at siren_tint()
    with moveinright
    k "PORRA ME DIZ QUE É O MEU X-MORTADELA-MALIGNO, CLÁUDIA, 2 HORAS JÁ QUE EU PEDI!"
    show claudia feliz with dissolve
    c  "Senhorita Katarina! Essa pessoa veio procurar por ti, ela é de poucas palavras, parece ser algo importante."
    show katarina feliz with dissolve
    k "Ah! Você faz parte do movimento, o Gatovaldo me disse que apareceria."
    show katarina default with dissolve
    k "Claudia, sempre que alguma pessoa esquisita assim aparecer por aqui pode liberar direto para a minha sala."
    show katarina smirk with dissolve
    k "Faz parte de uma nova terapia que estou experimentando."
    jump k1m1



    label k1b1:
    c @default "Ela está sim! Se não se importa em esperar um pouco, ela está em sua sessão diária de Post-Generic-Slovenian-Punk-Rock."
    show claudia feliz with dissolve
    c "Enquanto isso, aceita um chá de camomila fervido em sangue de carneiro? É uma bebida típica sueca."
    show claudia default with dissolve
    n "Ela não aguarda por uma resposta e te serve uma xícara de um líquido viscoso esquisito..."
    n "Você definitivamente não quer tomar isso."
    c "Ah! Já ia me esquecendo. Com licença, preciso acender o incenso do dia. Você sabe, para atrair boas energias."
    n "Ela se dirige a um armário rústico e começa a procurar por algo em uma gaveta."
    show claudia thinking with dissolve
    c "Lavanda, orvalho do amanhecer, lírios holandeses, não... Hoje é terça, cadê o de terça?"
    show claudia feliz with dissolve
    c "Aqui! Te achei, Mosh Pit do Slipknot!"
    n "Ela acende o incenso, e um cheiro de rebeldia toma conta do ambiente. Você nem imaginava que seria possível perceber isso olfativamente."
    with hpunch
    play sound "doorOpen.ogg"
    n "A porta do escritório abre escancaradamente."
    show claudia default at left
    with move
    show katarina irritada at right
    with moveinright
    k "Claudia, Mosh Pit do Slipknot agora é o incenso de quinta, você não viu as alterações que eu te mandei por email?"
    c "Senhorita Katarita! Peço perdão, não acontecerá novamente! Já irei providenciar o incenso diário correto." 
    
    c "Ah, aliás, essa pessoa veio te procurar. Ela recusou o chá sueco, eu te avisei que capim-limão ornava melhor."
    show katarina feliz with dissolve
    k "Ah! Você faz parte do movimento, o Gatovaldo me disse que apareceria."
    show katarina default with dissolve
    k "Claudia, sempre que alguma pessoa esquisita assim aparecer por aqui pode liberar direto para a minha sala."
    show katarina smirk with dissolve
    k "Faz parte de uma nova terapia que estou experimentando."
    jump k1m1
label k1m1:
    k "Me acompanhe, meu querido, temos trabalho a fazer."
    
    scene bg escritorio
    hide claudia
    hide katarina
    with gatodissolve
    show katarina default at center
    with moveinleft
    n "Você acompanha Katarina até o seu escritório. Ele é repleto de esculturas bizarras e pinturas que remetem ao caos e à destruição, tudo em tons de branco e rosa."
    show katarina smirk with dissolve
    k "Você parece espantado, gostou do meu cantinho? Descobri a identidade do Bansky e tranquei ele aqui com baldes de tinta durante 3 dias."
    show katarina default with dissolve
    k "Na verdade, 3 dias para cada vez que eu abrisse a porta e não gostasse do que estivesse vendo. Ele acabou ficando uns 2 meses trancado aqui."
    show katarina smirk with dissolve
    k "Mas no fim o resultado foi espetacular!"
    show katarina default with dissolve
    k "Ele até deu uma sumida da ruas, acho que deve ter ido procurar terapia, mas sinceramente, não entendo o porquê...{w} Minha sala tem ar condicionado e eu sempre o alimentava com minhas refeições preferidas."
    n "Você se lembra de uma aberração gastronômica sendo mencionada anteriormente..."
    n "...pobrezinho."
    show katarina feliz with dissolve
    k "Bem, vamos falar de negócios, sugeri ao seu chefe que a gente fosse explodir alguma coisa..."
    
    show katarina meh with dissolve
    k "...mas ele achou melhor não, fiquei muito frustrada. Vou ser franca contigo, entrei na revolução para explodir coisas!"
    show katarina brava with dissolve
    k "Aquela ratazana imunda acha que pode simplesmente acabar com uma das minhas fontes de renda e ainda deixar milhares de gatinhos por aí com fome? Fala sério! Eu quero mais é explodir tudo mesmo!"
    show katarina smirk with dissolve
    k "Mas antes de sair, a gente precisa se conhecer um pouco. Para começar, qual é seu nome?"
    if jogador1:
        azul "Me chamo [nome1]" 
    else:
        laranja "Me chamo [nome2]"
    
    show katarina default with dissolve
    n "Após dizer seu nome, ela começa a digitar e ler algumas coisas no computador."
    k "Huuum... Certo, já te conheço.{w} Sua vez, me faz uma pergunta"
    menu:
        "Você pesquisou informações minhas na internet?":
            $ JogadorAtivo += 0
            jump k1a2
        "O que são aquelas cabeças empalhadas com joias no lugar dos olhos?":
            $ JogadorAtivo += 1
            jump k1b2       
label k1a2:
    k "Na realidade não, só pesquisei o significado do seu nome, isso já basta pra mim."
    k "Só responde esse formulário aqui depois e manda para mim, é extremamente necessário."
    n "Ela te manda um teste do Buzzfeed para descobrir qual membro do One Direction você seria."
    show katarina feliz with dissolve
    k "Acho que já podemos ir, eu vou dirigindo!"
    menu:
        "Ir para a missão":
            jump missaokat1
label k1b2:
    show katarina feliz with dissolve
    k "Não se preocupe, elas são falsas, menos a do jacaré, a do leão, a do urso..."
    n "Ela diz mais alguns nomes..."
    n "Aparentemente no máximo umas 3 delas são falsas."
    show katarina triste with dissolve
    k "Eram do meu pai. Eu as herdei quando ele morreu, assim como as joias. Apenas uni as duas coisas..."
    show katarina feliz with dissolve
    k "Acho que já podemos ir, eu vou dirigindo!"
    menu:
        "Ir para a missão":
            jump missaokat1


label missaokat1:
    scene bg deserto
    with gatodissolve
    play music "deserto.mp3" volume 0.5
    n "Vocês dirigem até uma estrada deserta. Não há nada além de um posto de gasolina abandonado e uma grande torre de telefone nas redondezas."
    show katarina irritada with dissolve
    k "Que calor da porra, ainda bem que eu vim preparada..."
    n "Ela tira uma garrafa de vodka da mochila."
    menu:
        "Você não deveria fazer isso em uma missão.":
            $ JogadorAtivo += 0
            jump k1a3
        "Me dá um pouco?":
            $ JogadorAtivo += 1
            jump k1b3
label k1a3:
    show katarina confusa with dissolve
    k "Isso o que? Beber água?"
    n "Você percebe que aquilo na realidade era água. Parece estar bem quente."
    menu:
        "Qual é a vantagem de carregar garrafas de vidro contigo?":
            jump k1a4
        "Se jogar numa panela da pra cozinhar um miojo.":
            jump k1b4
            
label k1b3:
    
    show katarina feliz with dissolve
    k "Claro, eu tenho mais duas!"
    n "Você dá uma golada preparado para algo bastante forte, mas percebe que aquilo na realidade era água. E está quente pra porra."
    menu:
        "Qual é a vantagem de carregar garrafas de vidro contigo?":
            jump k1a4
        "Se jogar numa panela da pra fazer um miojo.":
            jump k1b4
label k1a4:
    
    show katarina smirk with dissolve
    k "Nunca se sabe quando você irá precisar de uma arma improvisada. E além disso, você já quebrou uma garrafa para uma briga de bar? É super divertido."
    
    jump k1m2

label k1b4:
    show katarina feliz with dissolve
    k "Sim! Se tô no inferno vou logo abraçar o capeta.{p} Minha bebida favorita do inverno é milkshake."
    jump k1m2

label k1m2: 
    show katarina default with dissolve
    k "Bem, acho que a gente ainda tem um tempo."
    k "Aliás, acho que você não deve ter a menor ideia do que a gente está fazendo aqui, né?"
    k "Basicamente, teu chefe, o gato falante, está desconfiando de uma empresa de sorvetes.{w} Ele acha que ela está realizando tráfico ilegal de queijos para a sede do governo."
    k "Você sabe, estamos sendo governados por um rato. Deve ser mais barato traficar do que lidar com todos os trâmites legais e impostos para a importação desses queijos chiques para cá."
    show katarina feliz with dissolve
    k "Ou talvez o Gatovaldo só queria tomar um sorvetinho e não estava sabendo pedir, então, caso ele esteja errado, pelo menos sairemos daqui com picolés!"
    show katarina default with dissolve
    k "Mas antes, bora naquele posto de gasolina abandonado dar uma explorada e depois a gente sobe naquela torre telefônica para termos uma visão melhor dos arredores e começarmos a nos preparar."
    show bg posto
    with gatodissolve
    n "Vocês andam até o posto de gasolina abandonado..."
    n "É definitivamente um posto de gasolina..."
    n "Está definitivamente abandonado..."
    show katarina surpresa with dissolve
    k "Que maneiro, parece que algumas coisas das prateleiras ainda estão aqui, bora dar uma olhada."
    show katarina default with dissolve
    n "Katarina vira de costas para você, tem uma tarântula enorme nela."
    menu:
        "AHHH! (matar a aranha)":
            $ JogadorAtivo += -2
            jump k1a5
        "Er... tem uma tarântula enorme nas suas costas.":
            jump k1b5
label k1a5:
    with vpunch
    show katarina brava with dissolve
    k "Que porra foi essa? Por que você bateu em m..."
    show katarina confusa with dissolve
    k "Espera, isso estava nas minhas costas?"
    show katarina surpresa with dissolve
    k "PUTA QUE PARIU."
    show katarina irritada with dissolve
    k "Não acredito que você fez isso, nunca tinha visto uma dessa espécie!"
    show katarina triste with dissolve
    k "Que droga. Argh, tudo bem, vamos entrar."
    n "Ela tira uma foto da aranha estraçalhada no chão."
    
    k "Puta que pariu... Era uma demonius Dosinfernus..."

    show bg loja
    with gatodissolve
    
    n "Vocês entram na loja, parece ter algumas coisas para explorar."

    
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
    show katarina surpresa with dissolve
    k "SÉRIO? RÁPIDO, abre o segundo bolso da minha mochila, você vai entender o que fazer!"
    n "Você abre o segundo bolso, tem um pote de vidro, um desodorante aerosol e um isqueiro."
    menu:
        "Tacar fogo na aranha":
            $ JogadorAtivo += -1
            jump k1a6
        "Colocar ela no pote":
            $ JogadorAtivo += +2
            jump k1b6
label k1a6:
    n "FUUUUSH!"
    n "Você torra a aranha."
    show katarina brava  with dissolve
    k "O QUE CARALHOS VOCÊ ACABOU DE FAZER? EU FALEI O SEGUNDO BOLSO."
    show katarina triste with dissolve
    k "Ah, espera... Droga, acho que guardei meu lança chamas portátil no lugar errado, que porra..."
    show katarina default with dissolve
    k "Enfim, bora entrar nessa loja conveniente."

    show bg loja
    with gatodissolve

    n "Vocês entram na loja, parece ter algumas coisas para explorar."
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
    n "Você coloca ela no pote, ela entra sem resistir."
    show katarina muitofeliz with dissolve
    k "CARALHO, QUE FODA, É UMA DEMONIUS DOSINFERNUS! Nunca tinha visto uma dessa espécie, muito obrigada! Vou levar ela para o meu zoológico particular."
    show katarina feliz with dissolve
    k "Enfim, bora entrar nessa loja conveniente."

    show bg loja
    with gatodissolve

    n "Vocês entram na loja, parece ter algumas coisas para explorar."
    menu:
        "Procurar nas prateleiras":
            $ JogadorAtivo += 1
            jump k1a7
        "Procurar no caixa":
            $ JogadorAtivo += 1
            jump k1b7
            $ escopeta = True
        "Procurar no banheiro":
            $ JogadorAtivo += 0
            jump k1c7
        "Procurar no escritório":
            $ JogadorAtivo += 1
            jump k1d7
label k1a7:
    show katarina default with dissolve
    n "Você procura por coisas nas prateleiras, e acha um salgadinho super ardido.{w} Ele venceu há 2 anos."
    k "Eaí, algo que preste?"
    show katarina muitofeliz with dissolve
    k "Caralho! Esse era edição limitada, valeu!"
    jump k1m3
label k1b7:
    show katarina default with dissolve
    n "Você procura por coisas no caixa, e acha uma escopeta escondida debaixo da máquina registradora."
    $ escopeta = True
    k "Eaí, algo que preste?"
    show katarina smirk with dissolve
    k "Que massa, mais uma pro meu arsenal."
    show katarina default with dissolve
    k "Se não se importar, guarda ela contigo aí por enquanto, tô sem espaço."
    jump k1m3
label k1c7:
    show katarina default with dissolve
    n "Você procura por coisas no banheiro..."
    n "Parece que alguém recentemente passou por aí."
    n "Você se arrepende da sua escolha."
    k "Eai, algo que preste?"
    show katarina smirk with dissolve
    k "Pelo seu silêncio, julgo que coisa boa não foi."
    jump k1m3
label k1d7:
    show katarina default with dissolve
    n "Você procura por coisas no escritório, e acha uma edição física de um filme nomeado 'Sharkula', aparentemente sobre um tubarão vampiro."
    n "Parece ser terrível."
    k "Eaí, algo que preste?"
    show katarina feliz with dissolve
    k "Porra, tava querendo ver esse aí faz tempo, obrigada!"
    jump k1m3
label k1m3:
    show katarina default with dissolve
    k "Bom, eu achei isso aqui."
    n "Ela te mostra uma revista, na capa, você vê uma garota usando rosa com o seu pai, o título é: \"Sucesso entre os felinos! Pai e filha revelam alguns dos segredos dos petiscos mais cobiçados pelos gatunos.\""
    show katarina triste with dissolve
    k "Eu até que gostava dele."
    k "Na realidade, eu gostava dele, mas era jovem demais para entender isso."
    k "Eu perdi mais do que um braço naquele atentado."
    n "Você percebe que um dos braços de Katarina na realidade é uma prótese. Muito bem feita, por sinal."
    menu:
        "Atentado?":
            jump k1a8
        "Meus sentimentos...":
            $ JogadorAtivo += 1
            jump k1b8
label k1a8:
    show katarina irritada with dissolve
    k "Não quero falar sobre isso no momento,{w} acho que já ta na hora da gente se preparar."
    jump k1m4
label k1b8:
    show katarina triste with dissolve
    k "É... obrigada.{w} Bora ir se preparar agora."
    jump k1m4
label k1m4:
    show katarina default with dissolve
    n "Vocês vão até a torre e começam a subir nela.{w} Ela parece instável, mas a confiança e animação de katarina te passam uma segurança inexplicável." 
    
    show bg caixadagua
    with gatodissolve
    n "Após chegarem a uma certa altura, vocês chegam a uma plataforma e se sentam na beirada. Definitivamente não há mais nada por perto além desta torre e daquele posto de gasolina."
    k "É... Parece que a gente está bem isolado aqui mesmo, mas vai ser bom para ver quando o caminhão estiver chegando." 
    show katarina smirk with dissolve
    k "Bora fazer alguma coisa enquanto isso.{w} Abre o terceiro bolso da minha mochila ai e pega alguma coisa."
    menu:
        "Pegar tabuleiro de xadrez":
            jump k1a9
        "Pegar garrafa de vodka":
            $ JogadorAtivo += 1
            jump k1b9
        "Pegar rifle de precisão":
            jump k1c9

label k1a9:
    
    show katarina feliz with dissolve
    $ xadrez = False
    k "Ótima escolha!"
    n "Ela abre o tabuleiro, dentro dele há uma coleção de mini pingas."
    menu:
        "Pegar uma":
            $ JogadorAtivo += 1
            jump k1a10
        "Recusar":
            $ JogadorAtivo += -1
            jump k1b10
label k1b9:
    show katarina feliz with dissolve
    k "Boa! Tava querendo fazer isso mesmo."
    n "Ela pega a garrafa da sua mão, a arremessa para frente e aguarda ansiosamente ela espatifar no chão."
    show katarina default with dissolve
    k "Aqui é alto mesmo né."
    n "Vocês permanecem em silêncio por um tempo."
    n "Plaft!"
    k "Maneiro..."
    k "..."
    k "Acho que aquela lá era de verdade."
    k "Ela era bem cara..."
    show katarina triste with dissolve
    k "Por que eu fiz isso?"
    jump k1m5
label k1c9:
    show katarina default with dissolve
    $ rifle =  True
    k "Não sei se vai ter muito o que fazer com isso aqui, mas bora tentar. Toma, vê se você acha alguma coisa."
    n "Você observa pela mira, e avista algumas coisas."
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
            $ rifle = False
            $ JogadorAtivo += 0
            jump k1d11
label k1a10:
    show katarina feliz with dissolve
    k "Toma essa aqui, é massa."
    n "Ela te dá uma pinga sabor planta carnívora."
    n "Você já deveria ter aprendido a não confiar nas preferências gastronômicas dela."
    k "Feita em casa!"
    jump k1m5
label k1b10:
    show katarina meh with dissolve
    k "Poxa, mas elas estão tão gostosinhas..."
    n "Ela pega uma sabor rabo de rato ao chimichurri."
    show katarina smirk with dissolve
    k "São totalmente veganas!"
    k "...Você deve ter um paladar infantil."
    jump k1m5
label k1a11:
    show katarina default with dissolve
    n "Você tenta atirar em um urubu voando, mas erra."
    show katarina smirk with dissolve
    k "Boa tentativa, passa isso aí pra mim."
    show katarina default with dissolve
    n "Ela pega a arma da sua mão, e atira para cima sem mirar."
    n "3 urubus caem do seu lado."
    show katarina smirk with dissolve
    k "Viu só?"
    show katarina feliz with dissolve
    k "Quem sabe um dia eu não te ensino a atirar."
    jump k1m5
label k1b11:
    show katarina default with dissolve
    n "Você atira em uma bomba de combustível no posto."
    n "Nada acontece."
    show katarina feliz with dissolve
    k "Você é dos meus, infelizmente esse posto ai já tá desativado há um bom tempo."
    show katarina smirk with dissolve
    k "Mas seria daora se ele explodisse."
    show katarina default with dissolve
    n "Vocês aguardam por alguns segundo em silêncio, como se o posto fosse comicamente explodir do nada."
    show katarina triste with dissolve
    n "Mas nada acontece."
    jump k1m5
label k1c11:
    show katarina default with dissolve
    n "Você atira em uma carcaça de coiote na distância."
    show katarina feliz with dissolve
    k "Wow, não estava prestando atenção, você matou aquele bicho? Muito foda!"
    jump k1m5
label k1d11:
    show katarina default with dissolve
    n "Você simplesmente não atira."
    show katarina smirk with dissolve
    k "Ahh, então você é um pacifistinha? Tudo bem, nada contra,{w} tenho até amigos que são..."
    jump k1m5
label k1m5:
    show katarina default with dissolve
    n "Vocês começam a ouvir um veículo se aproximando."
    show katarina surpresa with dissolve
    k "Espera!{w} Acho que é o nosso caminhão."
    n "Você observa um caminhão de sorvete na distância."
    show katarina feliz
    k "É isso mesmo! Bora descer!"
    n "Vocês descem a torre. A escada é bem precária, você tem uma sensação de quase morte ao pisar em um degrau e ele quebrar."
    show bg deserto
    with gatodissolve
    show katarina default with dissolve
    k  "Olha, é o seguinte, eu sei que eu sou uma das financiadoras disso daqui, e que você provavelmente questiona muito as minhas decisões e não confia em mim, mas eu peço, deixa que eu lido com isso daqui, só siga o meu plano."
    n "Ela abre a mochila, e te dá uma garrafa de ketchup."
    show katarina smirk with dissolve
    k "Você sabe o que fazer."
    n "Você não sabe o que fazer."
    show katarina meh with dissolve
    k "Ok, vejo na sua cara que você não sabe o que fazer. {w}Vai lá na estrada, deita e joga bastante ketchup na sua perna e perto dela. Você vai chorar e gritar de dor, pedindo por ajuda."
    show katarina smirk with dissolve
    k "Se ele acelerar e passar por cima de você, teremos certeza que eles trabalham para o governo e estão preparados para lidar com emboscadas."
    k "Se ele parar para te ajudar, a gente vai saber que ele provavelmente é só um motorista inocente, você irá dizer que é uma pegadinha e tudo ficará certo, pode ser?"
    menu:
        "Me sinto feliz de morrer pela causa!":
            $ JogadorAtivo += 1
            jump k1a12
        "Você quer me usar como um sacrifício humano?":
            $ JogadorAtivo += -1
            jump k1b12

label k1a12:
    show katarina smirk with dissolve
    k "Sempre desconfiei que você fosse meio biruta, mas não, não irei deixar você morrer. Se ele acelerar eu acerto um tiro no meio da testa dele e você sai correndo, tenho uma boa mira."
    jump k1m6

label k1b12:
    show katarina surpresa with dissolve
    k "Claro que não! Só estava zoando com a sua cara, eu dou um jeito pra ele não fazer isso."
    show katarina smirk with dissolve
    k "Mas se prepare para correr caso precise."
    jump k1m6

label k1m6:
    n "Você sente que não tem outra alternativa a não ser a confiar nela. Flashs da sua vida inteira passam pela sua cabeça, e o caminhão ainda nem está vindo na sua direção."
    hide katarina with dissolve
    n "Então você vai, deita na rodovia, e espalha o ketchup porcamente na sua perna.{w} Só uma pessoa muito ingênua mesmo cairia nisso."
    n "O caminhão se aproxima cada vez mais. Você sente um frio na espinha mas começa a gritar por ajuda. Sua atuação é terrível, nem a alma mais inocente da terra seria capaz de acreditar nisso."
    n "Ele chega a uma distância consideravelmente perto de ti... {w} ele se aproxima...{w} e de repente..."
    n "Ele para."
    n "Um senhorzinho muito fofo sai da cabine."
    show vovo default at left with moveinleft
    vo "Meu Deus! Você está bem? o que houve?"
    
    menu:
        "É pegadinha!!!! kkkkkk caiu igual um patinho!!!":
            jump k1a13
        "Continuar atuando":
            jump k1b13
label k1a13:
    
    vo "O quê? Mas o que você está fazendo aqui nesse meio do nada?"
    jump k1m7
label k1b13:
    vo "Minha nossa! Esse machucado parece estar feio!"
    jump k1m7
label k1m7:
    n "Você percebe que ele genuinamente acredita em ti e está evitando olhar para a sua perna."
    n "Você vê Katarina chegando de mansinho com um rifle e usando uma bandana na cara."
    show katarina brava at right
    with moveinright
    k "Mãos ao alto velhote!"
    show vovo default at shake
    vo "Mas o quê...?"
    show katarina brava at bounce
    k "Isso mesmo! Mãos ao alto! Isso é um assalto!"
    n "Ele paralisa, parece estar muito assustado."

    menu:
        "Você ouviu ela! (Apontar a escopeta para ele)" if escopeta:
            $ JogadorAtivo += 1
            jump k1a15
        "Não fazer nada" if escopeta:
            n "Você apenas deixa Katarina agir."

    show katarina feliz with dissolve
    k "Tô te zoando!"
    n "Ela abaixa a arma."
    show katarina smirk with dissolve
    k "É só uma pegadinha para o meu canal do Youtube!"
    show vovo default at shake
    vo "Ah.. Haha.. Entendi... Por favor me deixem ir, eu tenho família..."
    n "Ele ainda está bastante assustado."
    show katarina default with dissolve
    k "Calma! Toma aqui."
    n "Ela tira um maço de dinheiro da mochila."
    show katarina feliz with dissolve
    k "Me vê três picolés!"
    vo "C-claro, s-s-só preciso pegar eles ali na p-parte de trás."
    show katarina default with dissolve
    n "Vocês vão até a parte de trás do caminhão, ele entra, e sai com três picolés de baunilha."
    vo "A-aqui o troco."
    show katarina confusa with dissolve
    k "Troco? Desde quando picolés são tão baratos assim? Ah quer saber, pode ficar...{p}Pelo susto, vai."

    hide vovo
    with moveoutleft

    n "O senhor entra de volta no caminhão, e sai acelerado."

    show katarina irritada at center
    with move

    k "Logo o de baunilha... Que sabor mais sem graça..."
    show katarina default with dissolve
    k "É, bem, ele está limpo, precisamos analisar a nossa próxima hipótese."

    menu:
        "Você mandou bem!":
            $ JogadorAtivo += 1
            jump k1a14
        "É... Acho que você precisa tomar um pouco mais de cuidado ao lidar com civis...":
            $ JogadorAtivo += -1
            jump k1b14
label k1a14:
    show katarina smirk with dissolve
    k "Ah, eu sei né! Falei poxa, confia em mim!"
    jump k1m8
label k1b14:
    show katarina smirk with dissolve
    k "Aquele velhote vai valorizar muito mais a vida dele depois desse susto." 
    show katarina default with dissolve
    k "Tava precisando parar de ser besta também, você é péssimo atuando, não sei como ele caiu naquilo!"
    
    jump k1m8


label k1a15:
    show katarina confusa with dissolve
    n "Katarina olha assustada para você, aparentemente ela não pretendia assaltar ele de verdade."
    show katarina surpresa with dissolve
    k "Mas..."
    show katarina smirk with dissolve
    k "Pode ir abrindo o caminhão!"
    n "De qualquer forma, ela parece ter gostado da sua atitude."
    show vovo default at shake
    vo "Está bem! Está bem! Só não me machuquem!"
    
    menu:
        "Investigar a cabine":
            jump k1a16
        "Investigar o baú":
            jump k1b16
    
label k1a16:
    n "Você prossegue para investigar a cabine, e Katarina mantém o vovô de refém."
    n "Parece uma cabine comum de caminhão, tem muitas coisas espalhadas pelos bancos e o porta-luvas está entreaberto."
    show katarina default with dissolve
    k "Rápido aí, a estrada é deserta mas pode passar alguém a qualquer momento."
    menu:
        "Investigar o porta luvas":
            jump k1a17
        "Investigar os bancos":
            jump k1b17

label k1a17:
    n "Você investiga o porta-luvas."
    n "Você encontra..."
    n "Luvas!"
    menu:
        "Achei umas luvas no... porta-luvas.":
            show katarina brava with dissolve
            k "O que? Quem que guarda luvas no porta-luvas? Você por acaso vai no Coco Bambu e pede coco e bambu?"
            jump k1m9


label k1b17:
    n "Você investiga os bancos."
    n "Há muitos papéis e embalagens de snacks."
    n "Há muitas embalagens de Polenguinho."
    menu:
        "Tem umas embalagens de Polenguinho aqui no banco.":
            show katarina confusa with dissolve
            k "Polenguinho? Aquele queijo de bolso? Quem come esse tipo de coisa?"
            jump k1m9

label k1b16:
    n "Você prossegue para investigar o baú, Katarina mantém o vovô de refém."
    n "É um baú refrigerado, há várias caixas de sorvete."
    show katarina default with dissolve
    k "Procure onde ninguém procuraria! E seja rápido, a estrada é deserta, mas pode passar alguém a qualquer momento."
    menu:
        "Procurar no forro":
            jump k1a18
        "Procurar na seção de sorvetes de queijo":
            jump k1b18

label k1a18:
    n "Você procura por algo escondido no forro do baú."
    n "Você encontra uma submetralhadora, uma máscara de gás e duas granadas de fumaça"
    menu:
        "Tem uma submetralhadora, uma máscara de gás, duas granadas de fumaça e um CD do Raça Negra":
            show katarina surpresa with dissolve 
            k "Nenhum queijo?"
            show katarina irritada with dissolve
            k "Que droga."
            show katarina brava with dissolve
            k "Espera, por que caralhos você tem um CD do Raça Negra escondido?"
            jump k1m9

label k1b18:
    n "Você procura por algo na seção de sorvetes de queijo."
    n "Você sabe que ninguém nunca chegaria perto daí."
    n "Você abre um dos potes, parece normal a princípio."
    n "Você enfia a mão dentro dele, e tira um saco plástico de dentro dele."
    n "Nele, há um exemplar de um queijo babilônico extremamente raro."
    menu:
        "Tem um queijo escondido no sorvete de queijo!":
            show katarina smirk with dissolve
            k "Aha! Sabia! Se explica agora, velhote."
            jump k1m9

label k1m9:
    n "Katarina diz ao vovô."
    show vovo default at shake
    vo "É... é... é..."
    n "Fumaça começa a sair dos ouvidos dele."
    show katarina confusa with dissolve
    k "Que porra é essa?"
    n "O vovô cai, fazendo um grande barulho metálico com o impacto."
    hide vovo with moveoutbottom
    n "Um ratinho sai de sua boca e corre para o deserto."
    k "..."
    show katarina confusa at center with move
    k "Isso realmente acabou de acontecer?" 
    show katarina default with dissolve
    k "Tá bom, colete as evidências, Gatovaldo vai gostar de saber disso."
    k "Vou ligar para uma outra equipe vir aqui lidar com esse caminhão."
    k "Agora a gente precisa dar o fora daqui."
    show katarina feliz with dissolve
    k "Mas, já que ninguém está vendo, vamos pegar alguns picolés para o pessoal!"
    jump k1m8


label k1m8:
    n "Vocês voltam até o carro, os picolés já estão quase derretidos e o calor está insuportável."
    show katarina feliz with dissolve
    k "Hey, acho que a gente precisa se conhecer mais, você deve ter percebido que isso é importante para mim.{w} Tenho um problema em conviver com estranhos."
    
    show katarina smirk with dissolve

    extend " Quem sabe eu não te conto mais sobre o meu pai, {w}eu sei que está curioso."
    n "Você tenta dar uma resposta, mas ela imediatamente liga o som do carro em um volume estrondoso, e começa a acelerar.{p} Vocês partem."

    jump finalkat1


label finalkat1:
    if jogador1:
        $ k.azul += JogadorAtivo
    else:
        $ k.laranja += JogadorAtivo
    jump whereToGo
