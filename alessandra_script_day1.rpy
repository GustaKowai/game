###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 1--------------- ##############################################
########################################################################################################################### 


label d1ale1:

    $ aleDay1 = False
    scene bg atelie
    play music "atelie_intro.ogg" volume 1.0
    queue music "atelie_loop.ogg"

    if jogador1:
        with fadeA
    else:
        with fadeL
    
    n "Você chega em um prédio antigo, em um bairro estranho da cidade. Ao mesmo tempo, ele parece confortante e assustador."
    n "Gatovaldo te passou esse endereço e disse que você e Alessandra se encontrariam com algum tipo de informante."
    n "Ao passar pela entrada, um sininho toca em cima de você."

    menu:
        "Tem alguém aí?":
            $ alguem = True
            jump a1a
        "Alessandra?":
            jump a1a1

label a1a:

    n "{cps=*0.2}...{/cps}"

    menu:
        "Alessandra?":
            jump a1a1
        "Senhorita Mallet?":
            jump a1a1

label a1a1:

    n "Você sente algo estranho, como se estivesse sendo observado."
    n "Quando decide olhar para trás..."

    if alguem:
        "Nunca diga \"Tem alguém aí?\".{w} Já assisti filmes de terror o suficiente." 
        "{cps=*0.2}Traz má sorte. {/cps}"
    
    show alessandra sorriso with moveinbottom

    if alguem:
        a "Tô zoando!"
    a "E aí, tudo no jeito para a missão?"

    show alessandra default with dissolve
    a "Só aguardar aqui fora, o transporte já já chega."

    show alessandra smirk with dissolve
    a "Engraçado que você nem percebeu que eu estava escondida atrás da porta quando entrou.{w} Gosto de assustar as pessoas às vezes, é engraçado."

    show alessandra default with dissolve
    a "Sabe, de vez em quando tudo o que a gente precisa é de um pouco de emoção. Vivemos nossas vidas monótonas repetindo o mesmo ciclo dia após dia..."
    a "É bom ter um motivo maior para se preocupar com a sua própria vida."

    show alessandra smirk with dissolve
    a "Aposto que você se assustou de verdade, olha a minha cara de louca! Tô branca igual um vampiro.{w} Não saía desse lugar há muito tempo e quando saía era para comprar miojo ou energético de madrugada no mercadinho 24 horas."  

    show alessandra default with dissolve
    a "Minha sorte é que a minha fama não chegou aqui nas periferias. Ser reconhecida nunca foi um problema aqui, esse é o lugar perfeito."

    n "Uma limousine estaciona em frente ao ateliê, por um momento você se questiona se está vestido adequadamente." 
    n "Alessandra mexe no vestido dela em algo que você não consegue decifrar." 
    

    n "De repente, partes do look que estavam escondidas se revelam e ela fica com uma aparência mais ousada, amedrontadora e claro, estilosa. {w}Agora você tem certeza que não está vestido adequadamente para a ocasião."

    show alessandra smirk with dissolve

    a "Vamos! Parece que o Giuseppe já chegou."

    menu:
        "Você tem algo mais adequado para eu vestir?":
            $ JogadorAtivo += 1
            jump a1a2
        "A gente não ia só se encontrar com um informante em um local público?":
            jump a1b2

label a1a2:

    a "Ah sim, claro!"

    show alessandra default at offscreenright 
    with moveoutright

    n "Ela entra no ateliê... {nw}"
    
    show alessandra default at center
    with moveinright
    
    extend "E volta com um vestido tie-dye."
    $ vestidotiedye = False

    show alessandra sorriso with dissolve 
    a "Está na moda."
    
    n "Você veste o vestido e não se sente na moda."
    n "Mas já que ela diz..."

    jump a1m1

label a1b2:

    a "Sim! No restaurante de luxo com a reserva mais disputada da cidade."
    
    show alessandra eyeroll with dissolve 
    a "E, na realidade, nosso amigo está mais para traficante do que informante, só para te avisar."

    jump a1m1

label a1m1:

    show alessandra default with dissolve 
    a "Bom! Agora vamos!"

    n "Vocês entram na limousine, ela leva vocês até um bairro de alta classe." 
    
    scene bg restaurante
    with gatodissolve
    stop music fadeout 1.0
    play music "restaurante.wav" 

    n "E para em frente a um estabelecimento que se parece com um palácio."

    show alessandra default with dissolve
    
    a "Chegamos! Bem vindo ao Ardórsia."

    n "Você se sente um pouco confuso com esse nome, deveria ser Ardósia? Como a rocha?"
    
    n "Ao entrar no restaurante, vocês são direcionados a uma mesa um pouco afastada, há uma mulher loira com uma banda de jazz se apresentando em um pequeno palco."
    show alessandra eyeroll with dissolve
    
    a "Droga, pensava que a Taylor Swift seria amanhã, nosso amigo traficante escolheu um péssimo dia para o encontro."

    show alessandra default with dissolve
    a "O gatinho te passou o briefing da missão? A gente está aqui para trocar esse diamante do Jared Leto por uma tecnologia importada extremamente letal."
    a "Basicamente ela é capaz de transformar qualquer coisa em tofu, e não sei se você sabe, mas ratos odeiam tofu."

    show alessandra smirk with dissolve
    a "Não é queijo de verdade."

    n "Você se sente extremamente confuso com tudo que acabou de ser proferido por Alessandra."

    menu:
        "Jared Leto?":
            jump a1a3
        "Taylor Swift?":
            jump a1b3

label a1a3:

    show alessandra default with dissolve
    a "É, poxa, esse diamante já fez parte de um visual que eu desenhei para ele. É aquele cara da banda 30 minutos para o fim do mundo, ou sei lá o que. Ele já fez alguns filmes também, se não me engano. É o que daremos em troca pela arma."

    jump a1m2

label a1b3:

    show alessandra triste with dissolve
    a "Hoje é sexta, pensei que colocariam alguém de mais prestígio."
    a "Tipo, sei lá, o Calcinha Preta."

    jump a1m2

label a1m2:

    n "Você prefere não questionar, isso já tem sido uma noite bem estranha."

    n "Alguns minutos se passam, e nada do traficante."

    n "Você consegue perceber Alessandra ficando um pouco impaciente."

    show alessandra triste with dissolve

    a "O quão desrespeitoso seria pedir a comida antes do nosso querido colega chegar? Estou faminta."

    menu:
        "Ele provavelmente não está nem aí para a comida.":
            $ JogadorAtivo += 1
            a "Que bom que concorda!"
            jump a1a4
        "Seria extremamente desrespeitoso e você com certeza acabaria com o nosso plano inteirinho por conta dessa sua atitude egoísta.":
            $ JogadorAtivo += -1
            jump a1b4
        "Eu não me importo. Garçooom!":
            $ JogadorAtivo += 0
            jump a1c4

label a1a4: 

    show alessandra default with dissolve

    n "Ela chama o garçom."

    show alessandra default at right
    with move

    show garcom default at left
    with moveinleft
    

    gar "Pois não?"

    a "Gostaria de um Frango Picatta com salada, pode fazer dois, para a gente."


    hide garcom
    with moveoutleft

    show alessandra default at center
    with move

    jump a1m3
    
label a1b4:
    show alessandra surpresa with dissolve

    a "..."
    
    show alessandra eyeroll with dissolve

    a "Ahh, acho que não é para tanto, ninguém mandou ele se atrasar."
    
    show alessandra default with dissolve
    a "Vou pedir algo legal para a gente, quem sabe você não se acalma um pouco."

    jump a1a4

label a1c4:

    n "O garçom se aproxima da mesa."

    show alessandra default at right
    with move

    show garcom default at left
    with moveinleft

    gar "Pois não?"

    n "Você olha para o menu, mas não entende absolutamente nada que está escrito."

    menu:
        "Pedir comida com nome alemão.":
            $ JogadorAtivo += 1
            n "Você pede uma comida com um nome esquisito em alemão."
            hide garcom
            with moveoutleft
            show alessandra surpresa at center
            with move
            a "Uau, você sabe que acabou de pedir dois pães com salsisha e uma Itaipava, né?"
            a "Tem coisa melhor aqui, mas aprecio sua ousadia."

        "Pedir comida com nome francês.":
            $ JogadorAtivo += 2
            n "Você pede uma comida com um nome esquisito em francês."
            hide garcom
            with moveoutleft
            show alessandra surpresa at center
            with move
            a "Adoro fígado de pato! Ótima escolha."
            n "Você acha que fez uma péssima escolha, mas ela parece ter gostado"

        "Pedir comida com nome coreano.":
            $ JogadorAtivo += 0
            n "Você pede uma comida com um nome esquisito em coreano."
            hide garcom
            with moveoutleft
            show alessandra surpresa at center
            with move
            a "Polvo vivo!"
            a "Diferente, mas interessante."
            n "Você deveria ter usado o tradutor."


    hide garcom

    with moveoutleft


    show alessandra surpresa at center
    with move

    jump a1m3
    
label a1m3:

    n "O garçom sai com o pedido, mas vocês inevitavelmente voltam à espera."

    show alessandra triste with dissolve

    a "Que tédio..."

    show alessandra seria with dissolve
    a "Lugares como esse fazem eu me sentir estranha, principalmente depois de ter passado tanto tempo longe de tudo. Cheio de pessoas mesquinhas, que se acham superiores por simplesmente terem conseguido uma reserva."

    show alessandra seria2 with dissolve
    a "Eu vou ser bem sincera, a comida daqui nem é a melhor da cidade." 

    show alessandra seria with dissolve
    a "Não estou dizendo que prefiro fast food ou um prato feito, existem lugares chiques que preparam pratos muito melhores e que têm um atendimento incomparável ao daqui..." 

    show alessandra eyeroll with dissolve
    a "...mas por algum motivo essa bodega aqui recebe todo o holofote."   

    show alessandra triste with dissolve  
    a "Se não tivesse sido a escolha pessoal do nosso colega eu teria outras 20 melhores opções de restaurantes para escolher."


    show alessandra default with dissolve

    a "Mas, já que estamos aqui, aguardemos..."



    menu:
        "Vamos jogar algo.":
            $ JogadorAtivo += 0
            jump a1a5
        "Vamos pedir uma música.":
            $ JogadorAtivo += 1
            jump a1b5

label a1a5:

    a "Hum... Que tal verdade ou desafio? Gostei, eu começo. Verdade ou desafio?"
    
    menu:
        "Verdade":
            $ JogadorAtivo += 0
            jump a1b6
        "Desafio":
            $ JogadorAtivo += 2
            jump a1a6
    
label a1b5:

    show alessandra smirk with dissolve
    a "Ótima ideia!"
    
    show alessandra default with dissolve
    n "Ela pega um papel e uma caneta e começa a escrever alguma coisa."
    
    a "Toma! Leva isso para ela."

    n "Você leva o papel para a mulher no palco. {w} Ela lê, fecha a cara, amassa o papel e joga em você."

    show alessandra smirk with dissolve

    a "KKKKKK"

    menu:
        "O que estava escrito?":
            $ JogadorAtivo += 1
            jump a1a8
        
        "Por que você não gosta dela?":
            $ JogadorAtivo += 0
            jump a1b8

label a1a6:
    a "Te desafio a ir até aquele garçom e falar que ele está servindo horrores."

    hide alessandra with dissolve

    show garcom default with dissolve

    n "Você vai até o garçom..."
    n "Vocês dois se olham em silêncio por alguns segundos."

    if jogador1:
        azul "Você está servindo horrores."
    else:
        laranja "Você está servindo horrores."

    n "Ele não parece entender."

    gar "Críticas favor encaminhar à gerência."

    hide garcom
    with moveoutright

    n "Ele sai andando em passos rápidos enxugando lágrimas nos olhos disfarçadamente."

    show alessandra surpresa with dissolve

    a "Ué? O que aconteceu? Você não falou que ele estava bem vestido?"
    a "Amei o uniforme do pessoal daqui, não entendi como alguém poderia se magoar com um elogio."

    show alessandra default with dissolve

    a "Mas tudo bem, você fez o desafio, isso que importa."

    jump a1m7

label a1b6:

    a "Beleza, fala aí."

    menu:
        "Eu tenho medo de tubarões.":
            $ JogadorAtivo += 0
            jump a1a7
        "Eu já quebrei os meus dois braços e minhas duas pernas.":
            $ JogadorAtivo += 2
            jump a1b7
        "Já dei PT de pinga azul em um forró.":
            $ JogadorAtivo += 3
            jump a1c7
        "Secretamente eu gosto dos filmes do Adam Sandler.":
            $ JogadorAtivo += -2
            jump a1d7

label a1a7:

    show alessandra sorriso with dissolve

    a "E quem não tem? Bobinho... Esses bichos foram criados para fazer as pessoas borrarem as calças."

    a "Tudo culpa do Spielberg!"

    show alessandra default with dissolve

    n "Ela não sabe que você perdeu os seus pais em um ataque de tubarão há dois anos atrás."

    jump a1m7

label a1b7:

    show alessandra surpresa with dissolve

    a "Nossa, você está mais remendado do que muitas roupas com que trabalhei, espero que isso não venha a nos atrapalhar."


    show alessandra smirk with dissolve

    a "Brincadeira! Precisando de mais remendos estou aqui para ajudar."

    jump a1m7

label a1c7:

    show alessandra surpresa with dissolve

    a "Realmente, nenhuma experiência é individual."

    show alessandra triste with dissolve

    a "Eu sei bem como é..."     

    show alessandra smirk with dissolve

    a "Quando tudo isso acabar daremos PT de pinga azul para comemorar!"

    jump a1m7

label a1d7:

    show alessandra brava with dissolve

    a "Acho que essa foi a pior coisa que você poderia ter me contado."

    show alessandra seria with dissolve
    a "Por muito tempo..."

    a "Meio que só passavam filmes do Adam Sandler na minha televisão."

    show alessandra triste with dissolve
    a "É difícil de explicar..."

    n "Ainda bem que ela não sabe que o seu filme favorito de todos os tempos é 'Cada Um Tem a Gêmea Que Merece'."

    jump a1m7

label a1a8:

    show alessandra sorriso with dissolve

    a "Falei para ela ajeitar a postura!"
    n "Você percebe que ela realmenete é meio torta."

    jump a1c8

label a1b8:

    show alessandra smirk with dissolve

    a "Sei lá! Só acho engraçado tirar uma com a cara dela"

    jump a1c8


label a1c8:
 
    show alessandra default with dissolve

    a "Aliás, será que eu deixei muito claro meu gosto musical? Odeio fazer isso. Detesto ser previsível, me fala algo que você acha que eu gosto."

    menu:
        "My Chemical Romance":
            $ JogadorAtivo += 0
            jump a1a9
        "Ivete Sangalo":
            $ JogadorAtivo += -1
            jump a1b9
        "Barões da Pisadinha":
            $ JogadorAtivo += 2
            jump a1c9
        "One Direction":
            $ JogadorAtivo += 1
            jump a1d9

label a1a9:

    show alessandra surpresa with dissolve

    a "Emo? Sério? Olha para a minha cara!"

    n "Ela tem mechas brancas no cabelo e está usando uma roupa extremamente gótica."

    jump a1m4

label a1b9:

    show alessandra eyeroll with dissolve

    a "Odeio, fez um feat com a Taylor."

    n "Você não sabe do que ela está falando, mas tem certeza que a Ivete Sangalo nunca fez um feat com essa outra cantora que você acabou de conhecer."

    jump a1m4

label a1c9:

    show alessandra surpresa with dissolve

    a "Droga! {w}Você é bom, acertou na mosca."
    
    show alessandra triste with dissolve
    a "Vou tentar ser mais discreta, não posso ficar me entregando tanto assim."

    jump a1m4

label a1d9:

    show alessandra smirk with dissolve

    a "Ok, você é bem inocente mesmo, fico feliz por não ter deixado na cara."

    jump a1m4


label a1m7:
    show alessandra default with dissolve
    a "Sua vez agora, vou deixar você escolher por mim."

    menu:
        "Verdade":
            a "Hummm... Deixa eu pensar..."
            show alessandra seria with dissolve
            a "Ok, a verdade é que eu não confio em absolutamente ninguém daqui."
            show alessandra sorriso with dissolve
            a "Menos você, eu confio em ti."
            show alessandra smirk with dissolve
            a "Mas fica esperto."

        "Desafio":
            $ lenco = True
            n "Você desafia Alessandra a pedir um autógrafo para a Taylor."
            
            show alessandra eyeroll with dissolve
            a "Que humilhação... Tantos adolescentes perto daquele palco e você quer que eu vá até lá pedir um autógrafo?"

            a "Argh, tudo bem, um desafio é um desafio"

            hide alessandra with dissolve
            n "Ela levanta da mesa e volta depois de alguns minutos."

            show alessandra default with dissolve
            a "Aqui está."

            n "Ela te mostra um lenço com a assinatura da cantora."

            a "A-a-ATCHIM!"

            n "Ela espirra e assoa o nariz no lenço."

            show alessandra smirk with dissolve
            a "Desculpa, não resisti!"

    jump a1m4

label a1m4:


    show alessandra default with dissolve

    a "Eita, acho que ele chegou."

    n "Você olha para trás, e vê um homem parrudo e amedrontador, usando roupas formais, de óculos escuros. Ele está se aproximando da mesa de vocês."

    show alessandra assustada with dissolve

    a "A gente tá fudido, olha o tamanho desse cara."

    n "Ele se aproxima em passos pesados."

    show alessandra medo1 with dissolve

    a "Eu vou para o banheiro e você lida com isso, tudo bem?"

    n "Alessandra está suando frio, ela parece muito nervosa. Ele está cada vez mais perto."

    show alessandra medo2 with dissolve

    a "Cara, por que eu fui me meter nisso? {w} Aquilo é uma arma?{w} Eu vou desmaiar..."

    n "Ele chega até a mesa de vocês e..."
    n "Ele passa reto."

    show alessandra surpresa2 with dissolve

    a "..."

    show alessandra sorriso with dissolve

    a "Ah, acho que era o segurança..."

    traf "Oiêêê."

    show alessandra confusa with dissolve

    a "O que foi isso?"

    traf "Oiêêê."

    a "De onde está vindo isso?!"

    n "Você percebe que, enquanto se distraíam e cagavam nas calças, uma pessoa de estatura baixa usando roupas rosas sentou-se à mesa com vocês."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft
    
    traf "Vocês são que são Alessandra e-"

    show alessandra smirk with dissolve

    a "SIM! É a gente, você não sabe como é bom fazer négocios com você!"

    n "Ela parece aliviada."

    show alessandra default with dissolve

    traf "Esse lugar que o Gatovaldo escolheu é camp!"

    show traficante default at bounce
    traf "Tipo, a Taylor está tocando aqui! Eu nem sabia que ela tocava em restaurantes!"

    show alessandra confusa with dissolve
    a "Espera, Gatovaldo? Ele que escolheu aqui?"

    traf "Sim! O chefe de vocês, não é?"

    show alessandra default with dissolve

    traf "Okay. Bem. Vamos direto ao ponto."

    n "O traficante recosta-se na cadeira e começa a falar em um tom sério."
    
    traf "Eu implementei algumas funções novas nessa belezinha..."

    n "Ele tira a arma tofu do bolso."

    traf "...então o preço também subiu."

    show alessandra surpresa2 with dissolve
    pause 0.5
    
    show alessandra brava2 with dissolve
    with hpunch

    a "O quê? Isso não é justo, a gente está com o seu diamante aqui! Esse foi o combinado!"

    n "Ele parece empolgado com o diamante."

    traf "Ela agora apaga memórias em um raio de 20 metros!"
    traf "Você transforma algo em tofu e boom! {w}Ele nunca existiu."
    traf "Um ente querido, um pet, qualquer coisa!"
    traf "'Por que tem um tofu nessa coleira? Não sei, mas parece delicioso!'"
    traf "É o que uma madame irá pensar quando você transformar o Lulu da Pomerânia dela em queijo de soja.{w} Então sim, o preço subiu."
    
    
    show alessandra eyeroll with dissolve
    a "Droga! {w} Tudo bem, preciso conversar com o meu associado primeiro. Um instante."

    n "Ela vira para você e começa a cochichar."

    hide traficante with dissolve
    show alessandra brava2 at center 
    with move
    show alessandra brava2 at easeinzoom
    a "O que a gente vai fazer, porra?"

    menu:
        "Dê algo mais valioso para ele." if lenco:
            $ JogadorAtivo += 3
            jump a1a10
        "Invente uma mentira.":
            $ JogadorAtivo += 0
            jump a1b10
        "Devemos tomar medidas drásticas.":
            $ JogadorAtivo += 2
            jump a1c10
        "Contate o gatovaldo.":
            $ JogadorAtivo += 1
            jump a1d10

label a1a10:
    a "O que de mais valioso eu poderia dar pra ele?"

    show alessandra triste with dissolve
    
    a "Tudo o que eu tenho é esse diamante aqui e..."

    show alessandra smirk with dissolve

    a "Espera, ele gosta da Taylor, não gosta?"

    show alessandra default at easeoutzoom

    n "Ela vira de volta ao traficante."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft

    a "Então, coleguinha, você gosta de divas pop, presumo eu."

    n "Os olhos dele brilham."

    traf "O.. O que você quer dizer com isso?"

    a "Muito bem, está vendo esse lencinho aqui na minha mão?"

    traf "S-sim, o que tem ele?"

    a "Essa caligrafia aqui, te lembra alguma coisa?"

    n "Ele começa a pensar."

    show traficante default at shake

    traf "ESPERA, essa não é a assinatura da Taylor, é?"

    show alessandra default with dissolve

    a "Sim, querido, é. Ela está logo ali, se quiser perguntar, mas infelizmente a sessão de autógrafos foi extremamente exclusiva e já acabou."

    a "Mas o que você não deve ter reparado é que..."

    show alessandra smirk with dissolve

    a "Esse lenço foi usado."
    a "Por ela."

    show alessandra default with dissolve

    n "Ele fica paralisado por um tempo, como se tivesse o Santo Graal a sua frente."
    traf "Eu... Eu preciso conversar com o meu assistente."

    hide traficante
    with moveoutleft

    show alessandra default at center
    with move

    n "Ele se retira da mesa e vai até um lugar um pouco afastado para realizar uma ligação."

    show alessandra smirk with dissolve

    a "Acho que a gente mandou bem!"

    with vpunch
    n "{size=+10}\"AAH!\"{/size}"
    
    n "Vocês ouvem um grito do telefone dele."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft

    traf "T-tudo bem, a arma é sua!{w} Mas eu preciso do diamante e do lenço agora!"

    show alessandra smirk with dissolve

    a "São todos seus!"

    n "Eles realizam a troca"
    achieve Arma_tofu

    traf "Magnífico! Bom, tchauzinho!"

    n "Ele sai do restaurante feliz."

    hide traficante
    with moveoutleft

    show alessandra sorriso at center
    with move
    a "Aquele otário vai levar meu catarro pra casa."

    menu:
        "Me sinto mal por termos enganado ele.":
            $ JogadorAtivo += 0
            jump a1a11
        "Tomou na jabiraca.":
            $ JogadorAtivo += 1
            jump a1b11

label a1b10:

    show alessandra default with dissolve

    a "Agora você falou a minha língua, e se a gente disser que..."
    a "Isso pode ser difícil, você precisa me ajudar a enganá-lo"

    show alessandra smirk with dissolve

    a "Já sei!"

    show alessandra default at easeoutzoom

    n "Ela vira de volta ao traficante."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft


    a "Então, meu querido, o nosso preço também aumentou."

    traf "O quê?!"

    a "Isso mesmo, tá vendo esse diamante aqui?"

    traf "Sim, o que tem nele?"

    show alessandra smirk with dissolve
    a "Então, antes de ser parte de um look do Jared Leto, esse diamante já esteve em outras mãos."

    traf "Jared Leto? Espera, esse diamante não é do Jason Momoa?"

    show alessandra surpresa with dissolve
    a "..."

    menu: 
        "Na realidade é do Jason Momoa sim!": #0
            $ pontosSucesso += 0
            traf "Então por que ela falou Jared Leto?"
            traf "Tipo, não tem nada a ver uma coisa com a outra"
            show alessandra confusa with dissolve
            a "É porque... Os dois nomes começam com J."
            a "E... Eu tenho um grande problema com nomes."
            show alessandra default with dissolve
            a "Eu só fui decorar o nome dos meus pais com 12 anos de idade."
            show alessandra triste with dissolve
            a "E eu esqueci de novo com 15."
            n "Alessandra está improvisando muito."
            n "Mas ele não parece muito convencido."
            traf "Tudo bem, mas como você ia dizendo, ele já esteve em outras mãos?"
            
        "É do Jared Leto, mas fez parte de outro look famoso": #1
            $ pontosSucesso += 1
            traf "Mas eu estou aqui por um diamante do Jason Momoa, foi o que combinaram comigo!"
            show alessandra default with dissolve
            a "É... Na realidade não!"
            a "Você está aqui pelo diamante do Jared Leto"
            a "Foi o combinado!"
            a "Você deve ter entendido errado porque... "
            a "Os dois nomes começam com J!"
            n "O gaslight de Alessandra parece ser efetivo"
            traf "Ok... Peço perdão por toda essa confusão!"
            traf "Mas eu estou aqui por um diamante do Jason Momoa, então espero que me convençam!"
            traf "Como você ia dizendo, ele já esteve em outras mãos?"

    show alessandra default with dissolve
    a "Isso mesmo! "

    show alessandra default with dissolve
    a "Quero dizer que ele já foi utilizado em outra grande ocasião{w} e acredito que a notoriedade desta ocasião se destacará muito mais do que o verdadeiro motivo pelo qual você veio até aqui hoje"

    traf "Eu posso analisá-lo?"

    a "Claro, aqui está.{w} Só não tente nada estúpido."

    n "Ele começa a observar minuciosamente o diamante, cheirando-o, ouvindo-o, sentindo-o. Até que paralisa em choque."

    traf "{size=+10}{cps=*0.2}ESSE-{/cps}{w}{cps=*2} ESPERA, ISSO É O QUE ESTOU PENSANDO?{/cps}{/size}"

    menu:
        "Esse diamante foi segurado por Katy Perry em Dark Horse": #1
            $ pontosSucesso += 1
            traf "UAU!"
            traf "Não era o que eu imaginava, mas até que faz sentido"

        "Esse diamante já foi da Joelma, ex-Calypso": #0
            $ pontosSucesso += 0
            traf "APOCALIPSE?"
            traf "O QUE VOCÊ QUER DIZER COM ISSO?"
            traf "Não parece bom..."
            show alessandra brava with dissolve
            a "Calypso foi o maior grupo de Brega-Pop brasileiro a já existir!"
            a "A Joelma é a nossa Taylor Swift Paraense!"
            traf "Ahh... Tem pop no nome, deve ser bom então."
            traf "Mas ainda não supera o motivo de eu estar aqui."
            n "Alessandra parece ter gostado de sua mentira, mas o traficante parece não conhecer a Joelma"
            a "Você não tem a menor ideia do quanto isso é valioso"
            traf "Preciso ter certeza disso ainda..."


        "Esse diamante esteve na banheira de Look What You Made me Do, da Taylor Swift": #3
            $ pontosSucesso += 3
            traf "EU SABIA!"
            traf "Isso realmente é bastante empolgante"

        "Esse diamante apareceu no clipe de Diamonds, da Rihanna": #2
            $ pontosSucesso += 2
            traf "EITA!"
            traf "Faz total sentido!"

    show alessandra smirk with dissolve

    a "Eai, podemos realizar a troca?"

    traf "Só um instante, preciso falar com o meu associado."

    n "Ele pega o telefone, disca um número, e sai da mesa por alguns instantes."

    n "Após alguns minutos, ele finalmente volta."

    traf "Certo! Agora preciso que vocês me digam as suas intenções com essa arma"
    traf "Tenho consciência social, ela pode causar grandes estragos!"
    traf "Ano passado vendi uma arma que transformava pessoas em queijo Brie para um francês"
    traf "Ele queria dominar o mundo, transformou toda sua cidade em queijo Brie"
    traf "O problema é que ele gostava muito de queijo Brie"
    traf "Comeu tanto que morreu"

    menu:
        "Também queremos dominar o mundo!": #-1
            $ pontosSucesso += -1
            n "Ele olha para vocês com uma cara séria."
            traf "Vocês ouviram o que eu acabei de dizer?"

        "Pretendemos transformar o Ratotávio em tofu!": #2
            $ pontosSucesso += 2
            traf "Uauu! Gostei da ideia."
            traf "Seria irônico, e icônico."

        "Queremos promover o veganismo!": #1
            $ pontosSucesso += 1
            traf "Lacraram!"
            n "Ele parece gostar da ideia"
            n "Por mais que a arma transforme coisas vivas em tofu"

    #se fez 3 ou mais pontos
    if pontosSucesso >= 3:
        traf "Tá bom! Vamos fazer esse negócio"

        show alessandra sorriso with dissolve

        a "Sabia que você faria a escolha certa!"

        n "O traficante troca a arma pelo diamante de Alessandra"
        achieve Arma_tofu


        traf "Esplêndido!{p} Foi um prazer realizar negócios com vocês. Agora, bye bye!"

        hide traficante
        with moveoutleft

        n "Ele sai do restaurante dando pulinhos."

        show alessandra default at center
        with move

        a "Mas que figura, ein?"

        show alessandra sorriso with dissolve

        extend "Todo dia sai de casa um malandro e um otário, bate aqui!"

        n "Você retribui o cumprimento dela."

        menu:
            "Você mandou bem!":
                $ JogadorAtivo += 1
                jump a1a12
            "Mandamos bem!":
                $ JogadorAtivo += 0
                jump a1b12

    # se fez menos que 3 pontos

    if pontosSucesso <3:

        traf "É... Acho que mudei de ideia, acredito que vocês não devem ter uma arma tão poderosa em mãos"

        show alessandra brava with dissolve

        a "O QUE?"

        show alessandra brava2 with dissolve
        a "Você só pode estar de brincadeira."

        traf "Foi mal!"
        hide traficante
        with moveoutbottom
        n "O traficante sai de fininho da mesa"

        a "Não acredito que ele fez isso com a gente!"
        $ sucessoMissao1Ale = False

        menu:
            "Mandei mal...":
                show alessandra triste with dissolve
                a "É..."
                show alessandra default with dissolve
                a "Mas eu também não fiz nada para te impedir "
                jump a1m5

            "Mandamos mal...":
                show alessandra triste with dissolve
                a "É..."
                a "Mentir foi uma péssima ideia."
                show alessandra default with dissolve
                a "Nem sempre dá para ganhar todas!"
                show alessandra smirk with dissolve
                a "Mas perder dá sim..."
                jump a1m5



label a1c10:

    show alessandra default with dissolve

    a "Arriscado, mas dá pra gente tentar... "

    show alessandra default at easeoutzoom

    n "Ela vira de volta ao traficante."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft


    a "E como exatamente a gente sabe que você está falando a verdade?"

    traf "É... Vocês acreditam?"

    a "Nada disso, a gente quer ver a arma funcionando."

    traf "Vocês... Querem transformar alguém daqui em tofu?"

    a "Essa é a sua sugestão?"

    traf "Não! Digo, não sei? Só tô tentando te entender."

    show alessandra smirk with dissolve

    a "Me empresta isso aqui, vou transformar aquele cara sozinho ali em tofu. Se ninguém perceber e a gente não for preso o diamante é todo seu."

    traf "Espera! Mas por que aquele homem?"

    show alessandra default with dissolve

    a "Porque ele... Está sozinho?"

    traf "Ele pode apenas estar exercendo a sua liberdade! O que te garante que ele não tenha alguém esperando por ele em casa?"

    show alessandra eyeroll with dissolve
    a "Cara, ninguém vai comer sozinho em um restaurante desses, esse aí deve ser um milhonário serial killer excêntrico."

    traf "Não sei se gosto dessa ideia..."

    menu:
        "Vamos transformar esse cara em tofu mesmo, ele é esquisito.":
            show alessandra smirk with dissolve
            $ JogadorAtivo += 1
            a "Viu!"

        "Vamos transformar um garçom em tofu.":
            show alessandra smirk with dissolve
            a "É uma alternativa! Ele provavelmente peida na comida."

        "Vamos transformar a Taylor Swift em tofu":
            $ JogadorAtivo += 2
            show alessandra smirk with dissolve
            a "Gostei dessa ideia!"
            traf "O QUE?"
            traf "VOCÊ ESTÁ MALUCO??"
            show alessandra surpresa with dissolve
            a "Não gostei dessa ideia..."
            n "Alessandra está mentindo."
            n "Mas o traficante parece realmente odiar essa ideia."
            menu:
                "Estou falando sério.":
                    $ JogadorAtivo += 1
                    traf "Vocês só podem estar de brincadeira!"
                    traf "Sério, desisto de tentar fazer négocio com vocês!"
                    hide traficante
                    with moveoutleft
                    show alessandra surpresa with dissolve
                    a "Eita."
                    show alessandra smirk with dissolve
                    a "Gostei tanto da sua ideia que por um momento esqueci que nosso objetivo era transformar ele em tofu."
                    show alessandra default with dissolve
                    a "Infelizmente, nem sempre dá para ganhar todas!"
                    show alessandra smirk with dissolve
                    a "Mas perder dá sim..."
                    $ sucessoMissao1Ale =  False
                    jump a1m5


                "Brincadeira! Vamos transformar um garçom mesmo...":
                    $ JogadorAtivo +=-1
                    traf "Ufa, melhor."

    traf "Tá bom... Só toma cuidado para mirar certo e para não levantar nenhum tipo de suspeita."

    n "Ele entrega a arma tofuzadora pra ela."
    achieve Arma_tofu

    show alessandra default with dissolve

    a "Só uma dúvida, como exatamente isso vai funcionar mesmo? Ele vai virar tofu e todo mundo aqui em volta não vai entender nada?"

    traf "Basicamente é isso, a gente provavelmente não se lembrará do momento em que ele se transformou em tofu também. Mas nós nos lembraremos dessa conversa, então saberemos o que aconteceu."
    traf "Agora para todo o resto das pessoas, ele simplesmente não existiu."

    a "Entendi... Agora me fala um pouco sobre você, tá solteiro?"

    traf "Gata, estou sim, mas caso não tenha percebido ainda, eu não me interesso por-"
    traf "Espera,{w} {size=+20}NÃO!{/size}"


    show white with dissolve
    hide traficante
    show alessandra confusa2 at center
    pause 2.0
    show cgAle1 with dissolve
    hide white


    n "Ela atira nele."
    n "Por um momento, você se questiona por que tem um tofu na cadeira com vocês."
    
    a "Espera... Isso realmente aconteceu?"

    n "Você se lembra da conversa."
    n "E as pessoas ao redor agem como se nada tivesse acontecido."

    menu:
        "Comer o tofu que está na cadeira do seu lado.":
            $ JogadorAtivo += 0
            hide cgAle1 with dissolve
            jump a1a13
        "Oferecer o tofu a ela.":
            $ JogadorAtivo += 1
            hide cgAle1 with dissolve
            jump a1b13



label a1d10:

    show alessandra default with dissolve

    a "Aquele gato vagabundo deve estar dormindo, mas vale a pena a tentativa."

    n "Ela pega o celular e começa a discar um número."

    show alessandra triste with dissolve

    a "Ele não vai atender."

    g "Miau?"

    show alessandra default

    a "General?"

    g "Sim?"

    a "Temos um problema..."

    n "Ela explica a situação para ele."

    a "Entendo... Irei fazer isso então."

    n "Ela desliga o telefone."

    show alessandra smirk

    a "Ele é um gênio!"

    show alessandra default at easeoutzoom

    n "Ela vira de volta ao traficante."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft


    show alessandra brava with dissolve

    a "Escuta só, seu merdinha, você não sabe com quem você está lidando, o nosso combinado foi o diamante pela a arma, e vai ser isso que a gente irá trocar,{w} o que você fez ou não fez de extra nessa arma simplesmente não interessa!" 
    a "Então vamos fazer o seguinte,{w} ou você sai desse restaurante com o seu diamante e a gente sai com a nossa arma,{w} ou ninguém sai daqui."
    
    show alessandra smirk with dissolve

    a "O que você me diz?"

    show traficante default at shake
    n "Ele começa a suar frio."

    show alessandra brava2 at shake
    a "{size=+5}Grrrrrrrr{/size}"

    n "Ela começa a rosnar."
    n "O traficante olha confuso para você."

    menu: 
        "*Começar a rosnar também*":
            $ JogadorAtivo += 2
            n "Você começa a rosnar junto de alessandra"
            traf "Tá bom!"
            traf "Só por favor, parem de fazer isso, está me assustando"

        "*Fazer um gesto ameaçador*":
            $ JogadorAtivo += 1
            n "Você faz um gesto de corte com sua mão em sua garganta para intimidá-lo."
            traf "Tá bom!"
            traf "Deus, não sabia que vocês eram barra pesada assim."

        "*Rir descontroladamente*":
            $ JogadorAtivo += -2
            n "Você descaralha de rir."
            n "Ver Alessandra rosnando foi realmente algo que você nunca imaginou."
            n "É intankavel."
            show traficante default
            traf "..."
            traf "Vocês estão tirando uma com a minha cara?"
            traf "Quer saber, eu vou embora!"
            hide traficante
            with moveoutleft
            show alessandra brava with dissolve
            a "Ei! O que tem de tão engraçado em me ver rosnando?"
            show alessandra confusa with dissolve
            a "..."
            a "Realmente, foi meio patético..."
            a "Mas você deveria ter me seguido!"
            a "Droga..."
            a "Qualquer coisa a gente mente para o Gatovaldo, falamos que o plano dele deu errado."
            $ sucessoMissao1Ale = False
            jump a1m5


    n "Ele passa a arma por debaixo da mesa."
    achieve Arma_tofu
    show alessandra brava with dissolve

    a "Acho bom!"

    n "Ela desliza o diamante para ele."

    traf "..."

    show alessandra default with dissolve

    a "..."

    n "Os dois ficam em silêncio por alguns segundos."

    traf "B-b-bom, acho que é melhor eu ir indo haha..."

    show alessandra brava2 at shake

    a "{size=+5}Grrrrrrrrrrrr{/size}"

    n "Ela começa a rosnar de novo."

    traf "O-ok, t-tchauzinho!"

    hide traficante
    with moveoutleft

    n "Ele levanta apressado e sai correndo."

    show alessandra default at center
    with move

    a "Ufa! Isso foi tenso."

    menu:
        "Você realmente começou a rosnar?":
            $ JogadorAtivo += 1
            jump a1a14
        "Que porra foi essa?":
            $ JogadorAtivo += 0
            jump a1a14


label a1a11:

    show alessandra default with dissolve

    a "Ah, eu sinceramente não ligaria nem um pouco pra isso se eu fosse você..."

    show alessandra sorriso with dissolve

    a "Afinal, temos nossa arma de tofu em mãos agora!"

    jump a1m5


label a1b11:

    show alessandra sorriso with dissolve

    a "Você teve uma ótima ideia!"

    jump a1m5

label a1a12:

    show alessandra sorriso with dissolve

    a "Agradeço pela sua modéstia, mas você também ajudou nisso. Mandamos bem!"

    jump a1m5

label a1b12:

    show alessandra default with dissolve

    a "Eu nunca duvidei que seriamos uma ótima dupla."

    n "Ela certamente duvidou que vocês seriam uma ótima dupla"

    jump a1m5

label a1a13:

    show alessandra confusa2 at center with dissolve 

    n "Você pega o tofu da cadeira e devora ele em uma mordida só."
    achieve Comer_tofu

    n "Tem gosto de tofu."

    show alessandra confusa2 at center 


    a "Espera, {size=+5}VOCÊ ACABOU DE COMER O NOSSO TRAFICANTE?{/size}"

    show alessandra confusa2 at easeinzoom2
    
    a "{size=+5}MEU PLANO ERA TENTAR DESENVOLVER UMA TECNOLOGIA REVERSA PARA TRAZER ELE DE VOLTA!{/size}"

    show alessandra confusa2 at easeinzoom
    a "{size=+5}AGORA SOMOS ASSASSINOS!!!!{w} E VOCÊ É UM{/size}{size=+15} CANIBAL!!!{/size}"
    
    show alessandra sorriso at easeoutzoom

    a "Brincadeirinha, era só um pedaço de tofu."

    jump a1m5

label a1b13:

    n "Você oferece o tofu a ela."

    hide traficante with dissolve

    show alessandra sorriso at center 
    with dissolve

    a "Obrigada! Vou guardar de recordação."
    $ tofu = True

    n "Ela chama o garçom."

    show alessandra default at right
    with move

    show garcom default at left
    with moveinleft

    

    a "Com licença, poderia me trazer uma embalagem para eu levar isso aqui para a viagem?"

    gar "Mas é claro!"

    hide garcom
    with moveoutleft
    hide traficante
    with moveoutleft

    show alessandra smirk at center
    with move

    a "É assim que se faz."

    jump a1m5

label a1a14:

    a "Foi o que o Gatovaldo me indicou! Intimidar e rosnar, ele diz que para ele sempre funciona."

    n "..."

    jump a1m5

label a1m5:

    show alessandra default at right
    with move

    show garcom default at left
    with moveinleft

    n "O garçom chega com o pedido de vocês."

    gar "Boa noite, aqui está."

    hide garcom
    with moveoutleft

    show alessandra default at center
    with move

    show alessandra surpresa with dissolve

    a "Caraca! Uau, isso aqui parece estar muito gostoso."

    n "A comida realmente parece estar muito boa."

    menu:
        "Pedir para ela experimentar primeiro":
            $ JogadorAtivo += 1
            jump a1a15
        "Experimentar primeiro":
            $ JogadorAtivo += 0
            jump a1b15


label a1a15:

    show alessandra smirk with dissolve
    a "Com todo o prazer!"

    jump a1m6

label a1b15:

    n "Você experimenta o prato... Ele está muito gostoso!"

    show alessandra smirk with dissolve
    a "Hummm... Parece que está bom mesmo, minha vez!"

    jump a1m6

label a1m6:


    n "Ela dá uma garfada."
    $ audio_crossFade(8, "tensao.wav")

    show alessandra assustada with dissolve

    menu:
        "Está tudo bem?":
            $ JogadorAtivo += 1
            jump a1a16
        "O que foi? Viu um fantasma?":
            $ JogadorAtivo += 0
            jump a1b16
 
label a1a16:

    show alessandra medo1 with dissolve

    a "Não, não está tudo bem, precisamos sair daqui agora."
    
    a "Tem alguma coisa de estranho nessa comida, acho que estamos sendo observados."

    menu:
        "O quê?":
            jump a1a17
        "Mas como?!":
            jump a1a17

label a1b16:

    a "Você não entenderia, mas sim, parece que estou lidando com um fantasma. A gente precisa sair daqui, rápido."

    menu:
        "O quê?":
            jump a1a17
        "Mas como?!":
            jump a1a17

label a1a17:

    show alessandra medo1 with dissolve

    a "Essa comida tem o mesmo gosto da comida do lugar em que me mantiveram presa por todos esses anos."

    a "Você não sabia disso e não pode contar a ninguém,{w} agora, precisamos sair, depois conversaremos mais sobre isso."

    n "Ela levanta da cadeira, deixa umas notas de dinheiro na mesa, puxa você pelo ombro e vocês saem do restaurante."

    hide alessandra
    with moveoutright

    n "Você está confuso, mas ela parece ter um bom motivo para estar assustada."

    stop music1 fadeout 2.0

    if jogador1:
        $ jogador1Ale1 = True
    else:       
        $ jogador2Ale1 = True
    jump finalale1


label finalale1:
    if jogador1:
        $ a.azul += JogadorAtivo
    else:
        $ a.laranja += JogadorAtivo 
    jump whereToGo
