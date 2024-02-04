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
    
    show alessandra smirk

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

    show alessandra default
    
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

    show alessandra smirk

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

label a1a8:
    a "Era 'famous' do Kanye West, não tenho a menor ideia do que rolou entre eles so sei que essa musica aí não significa coisa boa para ela não"

    jump a1c8

label a1b8:

    a "Muitas das minhas inimigas eram fãs dela, isso é algo para se prestar atenção em uma pessoa, tome cuidado."

    jump a1c8


label a1c8:

    n "Ela parece inflexível, ela nem era tão ruim assim"

    show alessandra default

    a "Aliás, será que eu deixei muito claro meu gosto músical? Odeio fazer isso. Detesto ser previsível, me fala algo que você acha que eu gosto"

    menu:
        "My Chemical Romance":
            jump a1a9
        "Ivete sangalo":
            jump a1b9
        "Barões da pisadinha":
            jump a1c9
        "One direction":
            jump a1d9

label a1a9:

    show alessandra surpresa

    a "Emo? sério? olha para a minha cara!"

    n "Ela tem mechas brancas no cabelo e está usando uma roupa extremamente gótica"

    jump a1m4

label a1b9:

    show alessandra brava

    a "Odeio, fez um feat com a taylor."

    n "Você não sabe do que ela está falando, mas tem certeza que ela a Ivete Sangalo nunca fez um feat com essa outra cantora que você acabou de conhecer"

    jump a1m4

label a1c9:

    show alessandra surpresa

    a "Droga! {w}Você é bom, acertou na mosca. {p}Vou tentar ser mais discreta, não posso ficar me entregando tanto assim."

    jump a1m4

label a1d9:

    show alessandra smirk

    a "Ok, você é bem inocente mesmo, fico feliz por não ter deixado na cara."

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
    
    traf "Vocês são que são alessandra e-"

    show alessandra smirk

    a "SIM! É a gente, você não sabe como é bom fazer négocios com você!"

    n "Ela parece aliviada"

    traf "Okay, bem, eu implementei algumas funções novas nessa belezinha..."

    n "Ele tira a arma tofu do bolso"

    traf "...então o preço também subiu."

    show alessandra brava

    a "O que? isso não é justo, a gente está com o seu diamante aqui, esse foi o combinado"

    n "Ele parece empolgado com o diamante"

    traf "Ela agora apaga memórias em um raio de 20 metros, você transforma um prato em tofu, boom! Ele nunca existiu."
    traf "Um ente querido, um pet, qualquer coisa!"
    traf "'Por que tem um tofu nessa coleira? Não sei, mas parece delicioso!'"
    traf "É o que uma madame irá pensar quando você transformar o lulu da pomerânia dela em queijo de soja.{w} Então sim, o preço subiu."
    
    with hpunch
    
    a "Droga! tudo bem, preciso conversar com o meu associado primeiro, um instante"

    n "Ela vira para você e começa a cochichar"

    a "O que a gente vai fazer, porra?"

    menu:
        "De mais algo valioso para ele":
            jump a1a10
        "Invente uma mentira":
            jump a1b10
        "Vamos transformar ele em tofu":
            jump a1c10
        "Contate o gatovaldo":
            jump a1d10

label a1a10:
    a "O que de mais valioso eu poderia dar pra ele? Esse vestido que foi usado pela beyonce no concerto em Munique na Alemanha em 2008? Ele nunca iria aceit-"

    show alessandra smirk

    a "Espera, ótima ideia!"

    n "Ela vira de volta ao traficante"

    show alessandra default

    a "Então, coleguinha, você gosta de divas pop, presumo eu"

    n "Os olhos dele brilham"

    traf "O-oque você quer dizer com isso?"

    a "Muito, bem, está vendo esse vestido que eu estou usando?"

    traf "S-sim, o que tem ele?"

    a "Munique, 2008, isso te lembra alguma coisa?"

    n "Ele começa a pensar"

    traf "ESPERA, esse não é o vestido que a b-b-be-beyon-"

    a "Sim, querido, ele é, pode pesquisar se sua memória estiver fraca."

    traf "E-eu, eu preciso conversar com o meu assistente"

    hide traficante
    with moveoutleft

    show alessandra smirk at center
    with move

    n "Ele se retira da mesa e vai até um lugar um pouco afastado para realizar uma ligação"

    a "Acho que a gente mandou bem!"

    n "{size=+10}\"AAH!\"{/size}"
    with vpunch
    n "Vocês ouvem do telefone dele"

    show alessandra default at right
    with move

    show traficante default at left
    with moveinleft

    traf "Ta na mão!"

    traf "T-tudo bem, a arma é sua!{w} Mas eu preciso do diamante e do vestido agora!"

    show alessandra brava

    a "O que? E eu saio daqui como?"

    traf "Eu te empresto minhas roupas, mas quero de volta depois"

    a "Argh, tá bom..."

    n "Eles vão até o banheiro e trocam de roupa"

    traf "Magnifico! Bom, tchauzinho!"

    n "Ele sai do restaurante feliz"

    hide traficante
    with moveoutleft

    show alessandra brava at center
    with move

    a "Mas que droga, o preço foi bem maior do que eu imaginava..."

    menu:
        "Sinto muito pelo seu vestido":
            jump a1a11
        "Sinto muito pelas roupas que você está vestindo":
            jump a1b11

label a1b10:

    show alessandra default

    a "Agora você falou a minha língua, e se a gente disser que..."

    show alessandra smirk

    a "Já sei!"

    n "Ela vira de volta ao traficante"

    a "Então, meu querido, o nosso preço também aumentou."

    traf "O que?!"

    a "Isso mesmo, ta vendo esse diamante aqui?"

    traf "Sim, o do Jared Leto, o que tem nele?"

    a "Então, ele não fez parte de um look só do Jared Leto."

    traf "Não? Espera, o que você quer dizer com isso?"

    a "Quero dizer que eu já reaproveitei ele em dois grandes visuais{w} e se você adivinhar qual foi esse outro visual eu trocarei ele pela arma e não requisitarei mais nada de você."

    traf "E-eu posso analisá-lo?"

    a "Claro, aqui está.{w} Só não tente nada estúpido."

    n "Ele começa a observar minuciosamente o diamante, cheirando-o, ouvindo-o, sentindo-o até que paralisa em choque"

    traf "{size=+10} {cps=*0.2}ESSE-{/cps}{w}{cps=*2} NÃO ME DIGA QUE ESSE DIAMANTE FOI UTILIZADO NO FIGURINO DA KATY PERRY EM DARK HORSE, FOI?{/cps}{/size}"

    show alessandra surpresa

    n "Alessandra finge surpresa"

    n "Ela olha para você e diz sussurando alto"

    a "Eu pensei que ele não fosse descobrir... Como?"

    show alessandra confusa

    n "Ela te dá uma piscadinha sutil"

    a "Certo, trato é trato, você acertou, eu aceito trocá-lo pela arma nessas condições"

    n "Ele parece impressionado"

    traf "M-muito obrigado"

    n "Eles realizam a troca entre a arma e o diamante"

    show alessandra feliz

    a "Esplêndido!{p} Foi um prazer realizar negócios com vocês, bye bye!"

    hide traficante
    with moveoutleft

    n "Ele sai do restaurante dando pulinhos"

    show alessandra default at center
    with move

    a "Mas que figura ein,"

    show alessandra feliz

    extend "todo dia sai de casa um malandro e um otario, bate aqui!"

    n "você retribui o cumprimento dela"

    menu:
        "Você mandou bem!":
            jump a1a12
        "Mandamos bem!":
            jump a1b12

label a1c10:

    show alessandra default

    a "Arriscado, mas dá pra gente tentar... "

    n "Ela vira de volta ao traficante"

    a "E como exatamente a gente sabe que você está falando a verdade?"

    traf "É... Vocês acreditam?"

    a "Nada disso, a gente quer ver a arma funcionando"

    traf "Vocês... Querem transformar alguém daqui em tofu?"

    a "Essa é a sua sugestão?"

    traf "Não! Digo, não sei? Só to tentando te entender"

    show alessandra smirk

    a "Me empresta isso aqui, vou transformar aquele cara sozinho ali em tofu, se ninguém perceber e a gente não for preso o diamante é todo seu."

    traf "Espera! Mas por que aquele homem??"

    a "Porque ele... Está sozinho?"

    traf "Ele pode apenas estar exercendo a sua liberdade! O que te garante que ele não tenha alguém esperando por ele em casa?"

    a "Cara, ninguém vai comer sozinho em um restaurante desses, esse ai deve ser um milhonário serial killer excêntrico"

    traf "Tá bom... Só toma cuidado para mirar certo e para não levantar nenhum tipo de suspeita"

    n "Ele entrega a arma tofuzadora pra ela"

    a "Só uma dúvida, como exatamente isso vai funcionar mesmo? Ele vai virar tofu e todo mundo aqui em volta não vai entender nada?"

    traf "Basicamente é isso, a gente provavelmente não se lembrará do momento em que ele se transformou em tofu também, mas nos lembraremos dessa conversa, então saberemos o que aconteceu."
    traf "Agora para todo o resto das pessoas, ele simplesmente não existiu"

    a "Entendi... Agora me fala um pouco sobre você, ta solteiro?"

    traf "Gata, estou sim, mas caso não tenha percebido ainda eu não me interesso por-"
    traf "Espera,{w} {size=+20}NÃO!{/size}"

    show traficante tofu
    with flashbulb

    n "Ela atira nele."
    n "Por um momento, você se questiona por que tem um tofu na cadeira com vocês"
    
    a "Espera... Isso realmente aconteceu?"

    n "Você se lembra da conversa"
    n "As pessoas ao redor agem como se nada tivesse acontecido."

    menu:
        "*Comer o tofu que está na cadeira do seu lado*":
            jump a1a13
        "*Oferecer o tofu a ela*":
            jump a1b13

label a1d10:

    show alessandra default

    a "Aquele gato vagabundo deve estar dormindo, mas vale a pena a tentativa"

    n "Ela pega o celular e começa a discar um número"

    show alessandra triste

    a "Ele não vai atender"

    g "Miau?"

    show alessandra default

    a "General?"

    g "Sim?"

    a "Temos um problema..."

    n "Ela explica a situação para ele"

    a "Entendo... Irei fazer isso então"

    n "Ela desliga o telefone"

    show alessandra smirk

    a "Ele é um gênio!"

    n "Ela vira de volta ao traficante"

    show alessandra brava

    a "Escuta só, seu merdinha, você não sabe com quem você está lidando, o nosso combinado foi o diamante pela a arma, e vai ser isso que a gente irá trocar,{w} o que você fez ou não fez de extra nessa arma simplesmente não interessa!" 
    a "Então vamos fazer o seguinte,{w} ou você sai desse restaurante com o seu diamante e a gente sai com a nossa arma,{w} ou ninguém sai daqui."
    
    show alessandra smirk

    a "O que você me diz?"

    n "Ele começa a suar frio"

    traf "T-ta bom..."

    n "Ele passa a arma por debaixo da mesa"

    show alessandra brava

    a "Acho bom!"

    n "Ela desliza o diamante para ele"

    traf "..."

    show alessandra default

    a "..."

    n "Os dois ficam em silêncio por alguns segundos"

    traf "B-b-bom, acho que é melhor eu ir indo haha..."

    show alessandra brava

    a "{size=+5}Grrrrrrrr{/size}"

    n "Ela começa a rosnar"

    traf "O-ok, t-tchauzinho!"

    hide traficante
    with moveoutleft

    n "Ele levanta apressado e sai correndo"

    show alessandra default at center
    with move

    a "Ufa! Isso foi tenso"

    menu:
        "Você acabou de rosnar?":
            jump a1a14
        "Que porra foi essa?":
            jump a1a14


label a1a11:

    show alessandra default

    a "Ah, eu sinceramente não ligava nem um pouco pra isso,"

    show alessandra brava

    extend "o que mais me deixa transtornada é ter que usar essa coisa aqui que ele chama de roupa, que visual terrível!"

    jump a1m5


label a1b11:

    show alessandra triste

    a "Está tudo bem, foi o preço necessário, foi alto, mas fizemos o que foi preciso."

    jump a1m5

label a1a12:

    show alessandra feliz

    a "Agradeço pela sua modéstia, mas você também ajudou nisso, mandamos bem!"

    jump a1m5

label a1b12:

    show alessandra default

    a "Eu nunca duvidei que seriamos uma ótima dupla"

    n "Ela está claramente mentindo."

    jump a1m5

label a1a13:

    n "Você pega o tofu da cadeira e devora ele em uma mordida só"

    hide traficante

    n "Tem gosto de tofu"

    show alessandra surpresa

    a "Espera, {size=+5}VOCÊ ACABOU DE COMER O NOSSO TRAFICANTE?{p} MEU PLANO ERA TENTAR DESENVOLVER UMA TECNOLOGIA REVERSA PARA TRAZER ELE DE VOLTA!{/size}"
    a "{size=+5}AGORA SOMOS ASSASSINOS!!!!{w} E VOCÊ É UM{/size}{size=+15} CANIBAL!!!{/size}"
    
    show alessandra feliz

    a "Brincadeirinha, era só um pedaço de tofu kkkkkkk"

    jump a1m5

label a1b13:

    n "Você oferece o tofu a ela"

    show alessandra feliz

    a "Obrigado! vou guardar de recordação"

    n "Ela chama o garçom"

    show garcom default at left
    with moveinleft

    show alessandra default at right
    with move

    a "Com licença, poderia me trazer uma embalagem para eu levar isso aqui para a viagem?"

    gar "Mas é claro!"

    hide garcom
    with moveoutleft

    show alessandra smirk at center
    with move

    a "É assim que se faz"

    jump a1m5

label a1a14:

    a "Foi o que o gatovaldo me indicou! intimidar e rosnar, ele diz que para ele sempre funciona"

    jump a1m5

label a1m5:

    show garcom default at left
    with moveinleft

    n "O garçom chega com o pedido de vocês"

    gar "Boa noite, aqui está."

    hide garcom
    with moveoutleft

    show alessandra feliz

    a "Caraca, uau, isso aqui parece estar muito gostoso"

    n "A comida realmente parece estar muito boa"

    menu:
        "Pedir para ela experimentar primeiro":
            jump a1a15
        "Experimentar primeiro":
            jump a1b15


label a1a15:

    a "Com todo o prazer!"

    jump a1m6

label a1b15:

    n "Você experimenta o prato... Ele está muito gostoso!"

    a "Hummm... Parece que está bom mesmo, minha vez!"

    jump a1m6

label a1m6:

    n "Ela da uma garfada e fica paralisada"

    show alessandra assustada

    menu:
        "Está tudo bem?":
            jump a1a16
        "O que foi? Viu um fantasma?":
            jump a1b16
 
label a1a16:

    a "Não, não está tudo bem, precisamos sair daqui agora,{w} tem alguma coisa de estranho nessa comida, acho que estamos sendo observados"

    menu:
        "O que?":
            jump a1a17
        "Mas como??":
            jump a1a17

label a1b17:

    a "Você não entenderia, mas sim, parece que estou lidando com um fantasma, a gente precisa sair daqui, rápido."

    menu:
        "O que?":
            jump a1a17
        "Mas como??":
            jump a1a17

label a1a17:

    show alessandra medo1

    a "Essa comida tem o mesmo gosto da comida do lugar em que me mantiveram presa por todos esses anos."

    a "Você não sabia disso, e não pode contar a ninguém, agora, precisamos sair, depois conversaremos mais sobre isso."

    n "Ela levanta da cadeira, deixa umas notas de dinheiro na mesa, puxa você pelo ombro, e vocês saem do restaurante"

    hide alessandra
    with moveoutright

    n "Você está confuso, mas ela parece ter um bom motivo para estar assustada"


    jump finalale1


label finalale1:
    if jogador1:
        $ a.azul += JogadorAtivo
    else:
        $ a.laranja += JogadorAtivo
    jump whereToGo
