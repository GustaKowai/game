###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 1--------------- ##############################################
########################################################################################################################### 


label d1ale1:
    default lenco = False

    $ aleDay1 = False
    scene bg atelie
    play music "atelie_intro.ogg" volume 1.0
    queue music "atelie.wav"

    if jogador1:
        with fadeA
    else:
        with fadeL
    
    n "Você chega em um prédio antigo, em um bairro estranho da cidade. Ao mesmo tempo, ele parece confortante e assustador."
    n "Gatovaldo te passou esse endereço e disse que você e Alessandra se encontrariam com algum tipo de informante"
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
    
    show alessandra sorriso
    with moveinbottom

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
    a "E, na realidade, nosso amigo está mais para traficante do que informante, só para te avisar"

    jump a1m1

label a1m1:

    show alessandra default with dissolve 
    a "Bom! Agora vamos!"

    n "Vocês entram na limousine, ela leva vocês até um bairro de alta classe." 
    
    scene bg restaurante
    with gatodissolve
    play music "restaurante.mp3" volume 0.5

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
    a "É, poxa, esse diamante já fez parte de um visual que eu desenhei para ele. É aquele cara da banda 30 minutos para o fim do mundo, ou sei lá o que, ele já fez alguns filmes também, se não me engano, é o que daremos em troca pela arma."

    jump a1m2

label a1b3:

    show alessandra triste with dissolve
    a "Hoje é sexta, pensei que colocariam alguém de mais prestígio."
    a "Tipo, sei lá, o Calcinha Preta"

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
            $ JogadorAtivo += 2
            jump a1c4

label a1a4: 

    show alessandra default with dissolve

    n "Ela chama o garçom."

    show alessandra default at right
    with move

    show garcom default at left
    with moveinleft
    

    gar "Pois não?"

    a "Gostaria de um Frango Picatta com salada, pode fazer dois, para a gente"


    hide garcom
    with moveoutleft

    jump a1m3
    
label a1b4:
    
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

    n "Você faz o pedido para a mesa, mas não tem a menor ideia do que está pedindo, é um menu complexo."

    hide garcom

    with moveoutleft


    show alessandra surpresa with dissolve
    k "Uau, você sabe que acabou de pedir dois queijos coalhos e uma sprite, né?"

    k "Tem coisa melhor aqui, mas aprecio sua ousadia."

    jump a1m3
    
label a1m3:

    n "O garçom sai com o pedido, mas vocês inevitavelmente voltam à espera."

    show alessandra triste at center
    with move

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
        "Vamos jogar verdade ou desafio enquanto isso.":
            $ JogadorAtivo += 0
            jump a1a5
        "Vamos pedir uma música.":
            $ JogadorAtivo += 0
            jump a1b5

label a1a5:

    a "Verdade ou desafio? Gostei, eu começo, verdade ou desafio?"
    
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

    n "Você leva o papel para a mulher no palco. {w} Ela lê, fecha a cara, amassa o papel e joga em você"

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

    hide alessandra

    show garcom default

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

    show alessandra surpresa

    a "Ué? O que aconteceu? Você não falou que ele estava bem vestido?"
    a "Amei o uniforme do pessoal daqui, não entendi como alguém poderia se magoar com um elogio."


    a "Mas tudo bem, você fez o desafio, isso que importa."

    jump a1m4

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

    show alessandra feliz

    a "E quem não tem? Bobinho... Esses bichos foram criados para fazer as pessoas borrarem as calças."

    a "Tudo culpa do Spielberg!"

    n "Ela não sabe que você perdeu os seus pais em um ataque de tubarão há dois anos atrás."

    jump a1m4

label a1b7:

    show alessandra surpresa

    a "Nossa, você está mais remendado do que muitas roupas com que trabalhei, espero que isso não venha a nos atrapalhar."

    a "Brincadeira! precisando de mais remendos estou aqui para ajudar."

    jump a1m4

label a1c7:

    show alessandra surpresa

    a "Realmente, nenhuma experiência é individual"

    a "Eu sei bem como é..."     

    show alessandra smirk

    a "Quando tudo isso acabar daremos PT de pinga azul para comemorar!"

    jump a1m4

label a1d7:

    show alessandra brava

    a "Acho que essa foi a pior coisa que você poderia ter me contado."

    a "Por muito tempo..."

    a "Meio que só passavam filmes do Adam Sandler na minha televisão"

    a "É difícil de explicar..."

    n "Ainda bem que ela não sabe que o seu filme favorito de todos os tempos é 'Cada Um Tem a Gêmea Que Merece'."

    jump a1m4

label a1a8:

    show alessandra default

    a "Falei para ela ajeitar a postura kkkkk"

    jump a1c8

label a1b8:

    show alessandra smirk

    a "Sei lá! Só acho engraçado, e eu genuinamente prefiro o Calcinha Preta"

    jump a1c8


label a1c8:

    n "Você percebe que ela realmenete é meio torta"

    show alessandra default

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

    show alessandra surpresa

    a "Emo? Sério? Olha para a minha cara!"

    n "Ela tem mechas brancas no cabelo e está usando uma roupa extremamente gótica."

    jump a1m4

label a1b9:

    show alessandra brava

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

    show alessandra smirk

    a "Ok, você é bem inocente mesmo, fico feliz por não ter deixado na cara."

    a "Sua vez agora, vou te deixar escolher."

    menu:
        "Verdade":
            a "Hummm... Deixa eu pensar..."
            show alessandra assustada
            a "Ok, a verdade é que eu não confio em absolutamente ninguém daqui"
            show alessandra feliz
            a "Menos você, eu confio em ti."
            show alessandra default
            a "Mas fica esperto"

        "Desafio":
            $ lenco = True
            n "Você desafia Alessandra a pedir um autógrafo para a Taylor"
            
            show alessandra brava
            a "Que humilhação... Tantos adolescentes perto daquele palco e você quer que eu vá até lá pedir um autógrafo?"

            a "Argh, tudo bem, um desafio é um desafio"

            n "Ela levanta da mesa e volta depois de alguns minutos"

            a "Aqui está."

            n "Ela te mostra um lenço com a assinatura da cantora."

            a "A-a-ATCHIM!"

            n "Ela espirra e assoa o nariz no lenço"

            show alessandra smirk
            a "Desculpa, não resisti!"


    jump a1m4

label a1m4:


    show alessandra assustada with dissolve

    a "Eita, acho que ele chegou."

    n "Você olha para trás, e vê um homem parrudo e amedrontador, usando roupas formais, de óculos escuros. Ele está se aproximando da mesa de vocês."

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

    show alessandra feliz with dissolve

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
    
    traf "Vocês são que são Alessandra e-"

    show alessandra smirk with dissolve

    a "SIM! É a gente, você não sabe como é bom fazer négocios com você!"

    n "Ela parece aliviada."

    show alessandra default with dissolve

    traf "Esse lugar que o Gatovaldo escolheu é camp!"
    traf "Tipo, a Taylor está tocando aqui! Eu nem sabia que ela tocava em restaurantes!"

    show alessandra confusa with dissolve
    a "Espera, Gatovaldo? Ele que escolheu aqui?"

    traf "Sim! O chefe de vocês, não é?"

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

    a "Muito, bem, está vendo esse lencinho aqui na minha mão?"

    traf "S-sim, o que tem ele?"

    a "Essa caligrafia aqui, te lembra alguma coisa?"

    n "Ele começa a pensar."

    traf "ESPERA, essa não é a assinatura da Taylor, é?"

    show alessandra default with dissolve

    a "Sim, querido, é. Ela está logo ali, se quiser perguntar, mas infelizmente a sessão de autógrafos foi extremamente exclusiva e já acabou."

    a "Mas o que você não deve ter reparado é que..."

    show alessandra smirk with dissolve

    a "Esse lenço foi usado."
    a "Por ela."

    show alessandra default with dissolve

    n "Ele fica paralisado por um tempo, como se tivesse o Santo Graal a sua frente"
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
    
    n "Vocês ouvem do telefone dele."

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft

    traf "Tá na mão!"

    traf "T-tudo bem, a arma é sua!{w} Mas eu preciso do diamante e do lenço agora!"

    show alessandra smirk with dissolve

    a "São todos seus!"

    traf "Magnífico! Bom, tchauzinho!"

    n "Ele sai do restaurante feliz."

    hide traficante
    with moveoutleft

    show alessandra brava at center
    with move

    show alessandra risada
    a "KKKKKKKK"
    a "Aquele otário vai levar meu catarro pra casa"

    menu:
        "Me sinto mal por termos enganado ele.":
            $ JogadorAtivo += 0
            jump a1a11
        "Tomou na jabiraca.":
            $ JogadorAtivo += 1
            jump a1b11

label a1b10:

    show alessandra default

    a "Agora você falou a minha língua, e se a gente disser que..."

    show alessandra smirk

    a "Já sei!"

    n "Ela vira de volta ao traficante."

    a "Então, meu querido, o nosso preço também aumentou."

    traf "O quê?!"

    a "Isso mesmo, ta vendo esse diamante aqui?"

    traf "Sim, o do Jared Leto, o que tem nele?"

    a "Então, ele não fez parte de um look só do Jared Leto."

    traf "Não? Espera, o que você quer dizer com isso?"

    a "Quero dizer que eu já reaproveitei ele em outro grande visual{w} e se você adivinhar qual foi esse outro visual eu trocarei ele pela arma e não requisitarei mais nada de você."

    traf "E-eu posso analisá-lo?"

    a "Claro, aqui está.{w} Só não tente nada estúpido."

    n "Ele começa a observar minuciosamente o diamante, cheirando-o, ouvindo-o, sentindo-o. Até que paralisa em choque."

    traf "{size=+10} {cps=*0.2}ESSE-{/cps}{w}{cps=*2} NÃO ME DIGA QUE ESSE DIAMANTE FOI UTILIZADO NO FIGURINO DA KATY PERRY EM DARK HORSE, FOI?{/cps}{/size}"

    show alessandra surpresa

    n "Alessandra finge surpresa."

    n "Ela olha para você e diz sussurando alto."

    a "Eu pensei que ele não fosse descobrir... Como?"

    show alessandra confusa

    n "Ela te dá uma piscadinha sutil."

    a "Certo, trato é trato, você acertou, eu aceito trocá-lo pela arma nessas condições."

    n "Ele parece impressionado."

    traf "M-muito obrigado."

    n "Eles realizam a troca entre a arma e o diamante."

    show alessandra feliz

    a "Esplêndido!{p} Foi um prazer realizar negócios com vocês. Agora, bye bye!"

    hide traficante
    with moveoutleft

    n "Ele sai do restaurante dando pulinhos."

    show alessandra default at center
    with move

    a "Mas que figura, ein?"

    show alessandra feliz

    extend "Todo dia sai de casa um malandro e um otário, bate aqui!"

    n "Você retribui o cumprimento dela."

    menu:
        "Você mandou bem!":
            $ JogadorAtivo += 1
            jump a1a12
        "Mandamos bem!":
            $ JogadorAtivo += 0
            jump a1b12

label a1c10:

    show alessandra default

    a "Arriscado, mas dá pra gente tentar... "

    n "Ela vira de volta ao traficante."

    a "E como exatamente a gente sabe que você está falando a verdade?"

    traf "É... Vocês acreditam?"

    a "Nada disso, a gente quer ver a arma funcionando."

    traf "Vocês... Querem transformar alguém daqui em tofu?"

    a "Essa é a sua sugestão?"

    traf "Não! Digo, não sei? Só tô tentando te entender."

    show alessandra smirk

    a "Me empresta isso aqui, vou transformar aquele cara sozinho ali em tofu. Se ninguém perceber e a gente não for preso o diamante é todo seu."

    traf "Espera! Mas por que aquele homem?"

    a "Porque ele... Está sozinho?"

    traf "Ele pode apenas estar exercendo a sua liberdade! O que te garante que ele não tenha alguém esperando por ele em casa?"

    a "Cara, ninguém vai comer sozinho em um restaurante desses, esse aí deve ser um milhonário serial killer excêntrico"

    traf "Tá bom... Só toma cuidado para mirar certo e para não levantar nenhum tipo de suspeita."

    n "Ele entrega a arma tofuzadora pra ela."

    a "Só uma dúvida, como exatamente isso vai funcionar mesmo? Ele vai virar tofu e todo mundo aqui em volta não vai entender nada?"

    traf "Basicamente é isso, a gente provavelmente não se lembrará do momento em que ele se transformou em tofu também. Mas nós nos lembraremos dessa conversa, então saberemos o que aconteceu."
    traf "Agora para todo o resto das pessoas, ele simplesmente não existiu."

    a "Entendi... Agora me fala um pouco sobre você, tá solteiro?"

    traf "Gata, estou sim, mas caso não tenha percebido ainda, eu não me interesso por-"
    traf "Espera,{w} {size=+20}NÃO!{/size}"

    show traficante tofu
    with flashbulb

    n "Ela atira nele."
    n "Por um momento, você se questiona por que tem um tofu na cadeira com vocês"

    show alessandra confusa
    
    a "Espera... Isso realmente aconteceu?"

    n "Você se lembra da conversa."
    n "E as pessoas ao redor agem como se nada tivesse acontecido."

    menu:
        "Comer o tofu que está na cadeira do seu lado.":
            $ JogadorAtivo += 0
            jump a1a13
        "Oferecer o tofu a ela.":
            $ JogadorAtivo += 1
            jump a1b13

label a1d10:

    show alessandra default

    a "Aquele gato vagabundo deve estar dormindo, mas vale a pena a tentativa."

    n "Ela pega o celular e começa a discar um número."

    show alessandra triste

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

    n "Ela vira de volta ao traficante."

    show alessandra brava

    a "Escuta só, seu merdinha, você não sabe com quem você está lidando, o nosso combinado foi o diamante pela a arma, e vai ser isso que a gente irá trocar,{w} o que você fez ou não fez de extra nessa arma simplesmente não interessa!" 
    a "Então vamos fazer o seguinte,{w} ou você sai desse restaurante com o seu diamante e a gente sai com a nossa arma,{w} ou ninguém sai daqui."
    
    show alessandra smirk

    a "O que você me diz?"

    n "Ele começa a suar frio."

    traf "T-tá bom..."

    n "Ele passa a arma por debaixo da mesa."

    show alessandra brava

    a "Acho bom!"

    n "Ela desliza o diamante para ele."

    traf "..."

    show alessandra default

    a "..."

    n "Os dois ficam em silêncio por alguns segundos."

    traf "B-b-bom, acho que é melhor eu ir indo haha..."

    show alessandra brava

    a "{size=+5}Grrrrrrrr{/size}"

    n "Ela começa a rosnar."

    traf "O-ok, t-tchauzinho!"

    hide traficante
    with moveoutleft

    n "Ele levanta apressado e sai correndo."

    show alessandra default at center
    with move

    a "Ufa! Isso foi tenso."

    menu:
        "Você acabou de rosnar?":
            $ JogadorAtivo += 1
            jump a1a14
        "Que porra foi essa?":
            $ JogadorAtivo += 0
            jump a1a14


label a1a11:

    show alessandra default

    a "Ah, eu sinceramente não ligaria nem um pouco pra isso se eu fosse você..."

    show alessandra feliz

    extend "Afinal, temos nossa arma de tofu em mãos agora!"

    jump a1m5


label a1b11:

    show alessandra feliz

    a "Você teve uma ótima ideia!"

    jump a1m5

label a1a12:

    show alessandra feliz

    a "Agradeço pela sua modéstia, mas você também ajudou nisso. Mandamos bem!"

    jump a1m5

label a1b12:

    show alessandra default

    a "Eu nunca duvidei que seriamos uma ótima dupla."

    n "Ela certamente duvidou que vocês seriam uma ótima dupla"

    jump a1m5

label a1a13:

    n "Você pega o tofu da cadeira e devora ele em uma mordida só."

    hide traficante

    n "Tem gosto de tofu."

    show alessandra surpresa

    a "Espera, {size=+5}VOCÊ ACABOU DE COMER O NOSSO TRAFICANTE?{p} MEU PLANO ERA TENTAR DESENVOLVER UMA TECNOLOGIA REVERSA PARA TRAZER ELE DE VOLTA!{/size}"
    a "{size=+5}AGORA SOMOS ASSASSINOS!!!!{w} E VOCÊ É UM{/size}{size=+15} CANIBAL!!!{/size}"
    
    show alessandra feliz

    a "Brincadeirinha, era só um pedaço de tofu."

    jump a1m5

label a1b13:

    n "Você oferece o tofu a ela."

    show alessandra feliz

    a "Obrigado! Vou guardar de recordação."
    $ tofu = True

    n "Ela chama o garçom."

    show garcom default at left
    with moveinleft

    show alessandra default at right
    with move

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

    jump a1m5

label a1m5:

    show garcom default at left
    with moveinleft

    n "O garçom chega com o pedido de vocês."

    gar "Boa noite, aqui está."

    hide garcom
    with moveoutleft

    show alessandra feliz

    a "Caraca! Uau, isso aqui parece estar muito gostoso"

    n "A comida realmente parece estar muito boa."

    menu:
        "Pedir para ela experimentar primeiro":
            $ JogadorAtivo += 1
            jump a1a15
        "Experimentar primeiro":
            $ JogadorAtivo += 0
            jump a1b15


label a1a15:

    a "Com todo o prazer!"

    jump a1m6

label a1b15:

    n "Você experimenta o prato... Ele está muito gostoso!"

    a "Hummm... Parece que está bom mesmo, minha vez!"

    jump a1m6

label a1m6:

    n "Ela dá uma garfada."

    show alessandra assustada

    menu:
        "Está tudo bem?":
            $ JogadorAtivo += 1
            jump a1a16
        "O que foi? Viu um fantasma?":
            $ JogadorAtivo += 0
            jump a1b16
 
label a1a16:

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

    show alessandra medo1

    a "Essa comida tem o mesmo gosto da comida do lugar em que me mantiveram presa por todos esses anos."

    a "Você não sabia disso e não pode contar a ninguém,{w} agora, precisamos sair, depois conversaremos mais sobre isso."

    n "Ela levanta da cadeira, deixa umas notas de dinheiro na mesa, puxa você pelo ombro e vocês saem do restaurante."

    hide alessandra
    with moveoutright

    n "Você está confuso, mas ela parece ter um bom motivo para estar assustada."


    jump finalale1


label finalale1:
    if jogador1:
        $ a.azul += JogadorAtivo
    else:
        $ a.laranja += JogadorAtivo
    jump whereToGo
