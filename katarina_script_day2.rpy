###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 

label d2kat1:
    play music "escritorio.mp3" volume 0.5
    $ katDay2 = False
    scene bg recepcao
    if jogador1:
        with fadeA
    else:
        with fadeL

    n "Você chega no escritório de Katarina, ele está decorado para o Halloween"
    n "Cláudia está falando com alguém no telefone"

    show claudia default

    c "Pela última vez, eu te pedi aranhas {size=+10}VENENOSAS{/size}, com veneno de verdade, paralisante, agonizante, que seja! {w}Não quero essas Tarântulas que vocês insistem em trazer para cá pela {size=+20}QUARTA VEZ!{/size}"

    n "*Ela olha para você*"

    c "Só um instantinho!"
    c "{size=+10}EU NÃO ME IMPORTO SE ISSO É LEGAL OU NÃO, QUERO AS MINHAS VIÚVAS NEGRAS PARA {/size}{size=+20}ONTEM.{/size}"
    n "Ela desliga o telefone."
    c "Ai, como é difícil lidar com esses vendedores, eu só queria deixar este lugar em uma ambientação de Halloween digna!"
    menu:
        "Mas estamos em fevereiro":
            jump k2a1
        "Aqui já é assustador o suficiente":
            jump k2b1

label k2a1:
    c "O que? Sério?"
    n "Ela pega o telefone e disca um número"
    c "Esquece as aranhas, quero corações, corações de verdade."
    n "Ela desliga"
    c "Valentines day!!"
    jump k2m1
    
label k2b1:
    c "Eu sei... {w}Mas nunca é o suficiente, sempre pode ser melhor!{p}Eu gosto de deixar as coisas o mais real possível"
    c "Teias falsas? Pra quê? Se eu posso ter minhas próprias aranhas mortais fazendo as suas teias aqui!"
    n "Você começa a se preocupar sobre os 3 esqueletos espalhados pela recepção"
    jump k2m1

label k2m1:
    c "Mas bem, você está aqui pela Katarina, correto?{w} Pode entrar no escritório, ela pediu para te dizer isso."
    n "*Você dá um sorrisinho preocupado, acena com a cabeça e entra no escritório*"
    scene bg escritorio
    with gatodissolve

    show katarina mascarada
    k "Eaeeee!"
    n "Katarina está usando uma máscara de filme de terror"
    k "Bora pedir doces ou travessuras?"
    n "Ela levanta e coloca uma máscara igualmente assustadora em você"
    k "{cps=*0.5}Nem pensa em tirar essa porra.{/cps}"

    menu:
        "Vocês realmente acreditam que estamos perto do Halloween?":
            jump k2a2
        "Partiu.":
            jump k2b2

label k2a2:
    k "Ué, mas estamos!"
    jump k2m2

label k2b2:
    k "Bora"
    jump k2m2

label k2m2:
    k "Hoje é serviço chato, vamos investigar umas transações financeiras em um banco"
    k "Espero que ao menos tenham doces para mim."
    k "Simbora, você vai dirigindo."
    n "Vocês entram no carro, ela te guia até o banco"

    scene bg banco
    with gatodissolve
    show katarina mascarada
    #play music "banco.mp3" volume 0.5

    k "Acho que é aqui, o gatovaldo mandou essa caixa para o escritório hoje de manhã, eu estava fumando lá fora e acabei recebendo isso, a pobre da Cláudia não teve nem a chance de fazer o trabalho de recepcionista dela."
    k "Acho que se eu começar a fumar mais talvez possa demití-la..."
    k "Mas enfim, não entendi muito bem, preferi abrir junto contigo"
    n "Ela pega uma caixa no banco de trás e abre"
    n "Tem um bolo enfeitado com corações, nele está escrito \"Fubanga\" em uma letra romântica"

    k "Que? {w}Que porra é essa? {w}Quem ele pensa que é para me chamar de fuba- fugan- fubanda sei lá que porra é essa! Mas deve ser ruim!"
    k "Aaaargh!"
    n "Ela dá um soco no bolo"
    k "Espera..."
    k "Tem alguma coisa aqui dentro..."  
    n "Ela tira um saco plástico de dentro dele"
    k "Espera, isso é... UMA ARMA??"
    n "Definitivamente é uma arma"
    k "Por que caralhos ele foi mandar uma arma para mim?"
    k "Ele sabe que eu já tenho dezenas dessa"
    k "Bem, isso fica comigo, nunca é demais."
    k "Agora bora pra essa chatisse."
    show bg bancodentro
    n "Vocês dois entram no banco, ele está vazio"
    k "Ótimo, isso não deve demorar."
    n "Ela se dirige até o caixa"
    k "Boa tarde, gostaria de-"
    show katarina mascarada at right
    show atendente default at left
    ate "Tira uma senha."
    k "O que?"
    ate "Tira uma senha. Já te atendo."
    k "Tá bom?"
    n "Katarina tira uma senha, é o número 348"
    n "O Último numero chamado aparentemente foi o 165"
    k "Espera, isso não pode ser verdade, não tem ninguém aqui, como pode ter tanta gente na nossa frente?"
    ate "Ninguém mais vem pessoalmente para o banco, to atentendo todo mundo pelo Discord, vocês deveriam tentar"
    n "Diz a atendente sem tirar o olho do computador"
    ate "Perdão Dona Neide, como eu estava dizendo, seu neto não está trancado no nosso cofre, você recebeu um trote."
    n "Katarina vira desapontada para você"
    k "Acho que prefiro morrer a ter que esperar aqui."
    k "Espera, acho que entendi a mensagem do gatovaldo, e se a gente assaltar essa porra aqui? {w}Já estamos de máscara mesmo."
    menu:
        "VOCÊ ESTÁ MALUCA? bora":
            jump k2a3
        "Precisamos nos atentar ao plano, vamos apenas extrair os documentos que precisamos.":
            jump k2b3
label k2a3:
    k "Gosto muito mais de você do que dos outros, essa revolução tem muita gente idiota, você tem coragem!"
    n "Ela vai à balconista"
    jump k2m3

label k2b3:
    k "Ah, droga, por que que você tem que ser a voz consciente da minha cabeça? Espero que eu possa te agradecer por isso depois."
    n "Vocês vão até a balconista"
    ate "Por favor volte ao seu assento e aguarde."
    n "Katarina olha furiosa para você"
    k "Me desculpe mas ela está pedindo para ser assaltad"
    jump k2m3

label k2m3:
    k "Desliga essa call"
    ate "O que?"
    n "Ela tira o fone da cabeça e olha para a Katarina"
    ate "Por que caralhos a senhora está usando uma máscara?"
    n "Há barulhos de tiro saindo do fone"
    k "Espera aí"
    n "Katarina vira o monitor da atendente"
    n "Ela está jogando Counter Strike"
    n "Há uma pessoa com o nome xXDona_NeideXx no time dela"
    ate "EU POSSO EXPLICAR! FAZ PARTE DO NOSSO NOVO ATENDIMENTO!"
    k "Eu não me importo!"
    n "Ela saca a arma"
    k "Isso é um assalto! Passa a senha do cofre!"
    ate "Calma! Calma! Eu levo vocês até ele!"
    n "Vocês descem até o cofre com a atendente"
    n "Ela parece desesperada"
    ate "Eu não acredito!"
    n "Ela começa a chorar"
    ate "Eu vou cair para o ouro 4 de novo!"
    n "Katarina vira para você"
    k "Do que caralhos ela ta falando? Tem ouro aqui em baixo?"
    menu:
        "Sim. Ela disse que tem muito, acho que umas 4 toneladas.":
            jump k2a4
        "Provavelmente está falando em códigos, deve ter algo super secreto aqui que a gente não pode saber.":
            jump k2b4
label k2a4:
    k "Haha! Aí sim, tomamos a decisão correta!"
    jump k2m4
label k2b4:
    k "Mal posso esperar para ver..."
    jump k2m4

label k2m4:

    show bg cofre

    n "Vocês chegam até o cofre, Ele é gigante"
    n "A Atendente vai até ele e começa a digitar uma senha"
    ate "Não me culpem por isso, nem sei o que vocês estão fazendo aqui."
    n "Ela abre o cofre"
    show bg cofreaberto
    n "Ele está vazio"
    ate "Nós estamos falidos! Como vocês não perceberam isso?"
    k "Mas..."
    n "O seu celular começa a tocar"
    n "É o Gatovaldo"
    k "Quem é?"
    menu:
        "É o Gatovaldo":
            jump k2a5
        "É a Cláudia":
            jump k2b5

label k2a5:
    k "Eita, deve ser importante"
    jump k2m5
label k2b5:
    k "Manda ela pra merda!"
    jump k2m5

label k2m5:
    n "Você atende o telefone"
    g "Miau! Quer dizer, Alô? {w}Então vocês já chegaram no banco? {w}É que eu já consegui as informações que eu precisava"
    g "Aparentemente eu me enganei e estava tudo em um banco online, foi fácil hackear e obter tudo."

    menu:
        "Haha ainda não chegamos":
            jump k2a6
        "Poxa que bom haha...":
            jump k2b6

label k2a6:
    g "Que alívio!"
    jump k2m6

label k2b6:
    g "Poisé né!"
    jump k2m6

label k2m6:
    g "Pode perguntar para a Katarina se a Claudia recebeu a minha encomenda?{w} Fica entre nós, mas é algo bem romantico, quero que somente ela abra"

    menu:
        "Vou perguntar sim haha, tchau!!":
            jump k2a7
        "Dia dos namorados chegando né, tudo bem, tchau!!":
            jump k2b7

label k2a7:
    n "Você desliga o telefone"
    k "Perguntar o que?"
    jump k2m7
label k2b7:
    n "Você desliga o telefone"
    k "Dia dos namorados? Mas estamos em outubro"
    jump k2m7

label k2m7:
    n "Você pega a arma da mão dela"
    k "O que você está fazendo?"
    n "Você percebe que no cabo dela está escrito 'Você me mata de paixão'"
    n "Você mira para cima e aperta o gatilho"
    n "Uma música cafona do Roberto Carlos começa a tocar"
    k "O que caralhos isso significa?"
    ate "Vocês fizeram eu perder a minha partida e nem uma arma de verdade tem? {w}Que patético"
    n "A atendente sai andando para a recepção novamente"
    hide atendente
    menu:
        "A Cláudia e o Gatovaldo estão...":
            jump k2a8
        "Acho que acabamos tudo o que tinhamos para fazer aqui.":
            jump k2b8

label k2a8:
    k "Estão o que? Deus! Por que que eu estou sempre cercada de gente esquisita?"
    jump k2m8
label k2b8:
    k "Não brinca? Não tem nada aqui, o Gatovaldo fez a gente de trouxa."
    jump k2m8

label k2m8:
    k "Vamos dar o fora."
    n "Vocês saem da sala do cofre e vão até a recepção"
    scene bg bancodentro
    show katarina mascarada
    k "Eu não acredito que a gente passou por essa vergonha pra não ter NADA aqui"
    menu:
        "Vergonha?":
            jump k2a9
        "A gente pode ser preso!":
            jump k2b9
label k2a9:
    k "Claro! é desonrante assaltar um banco e sair de mãos abanando, quando isso virar um esporte tudo bem."
    jump k2m9
label k2b9:
    k "Fica tranquilo, estamos de máscara."
    n "Ela é famosa suficiente para ser reconhecida mesmo de máscara"
    n "E usa sempre a mesma roupa"
    jump k2m9
label k2m9:
    ate "Ei!"
    show katarina mascarada at right
    show atendente at left
    n "Chuk-Chuk"
    n "A recepcionista do banco está com uma espingarda apontada para vocês"
    ate "Vocês acham mesmo que eu não sei o motivo de vocês estarem aqui?"
    n "Katarina olha confusa pra você"
    k "É... "
    ate "Eu sei do que vieram atrás, mas vocês não irão levá-lo."
    k "Sei.. haha..."
    n "Katarina sussura para você"
    k "Do que caralhos ela ta falando?"
    menu:
        "Sei lá, blefa!":
            jump k2a10
        "Fala que a gente já está de saída, aquela arma está me assustando.":
            jump k2b10
label k2a10:
    k "Você sabe muito bem que isso não vai acabar bem, então é melhor você entregar logo para a gente antes que...{p}Antes que os nossos reforços cheguem, eles já foram acionados!"
    n "A recepcionista parece suar frio"
    ate "Mas... Mas... Vocês estavam usando uma arma de brinquedo!"
    k "Aquilo foi apenas um mal entendido, agora o batalhão de verdade está chegando."
    k "E aliás, vocês não tem dinheiro nem para um segurança, acha que essa escopeta vai ser capaz de parar os nossos... Quantos homems?"
    menu:
        "1500":
            jump k2a11
        "1278":
            jump k2b11
label k2a11:
    k "1500 homens! Acha que vai ser capaz de parar os nossos 1500 homens? E eu nem te falei o número de mulheres ainda."
    jump k2m10
label k2b11:
    k "1278 homens! Acha que vai ser capaz de parar os nossos 1278 homens? E eu nem te falei o número de mulheres ainda."
    jump k2m10
label k2m10:
    n "Ela parece desesperada"
    ate "T-tudo bem! Só não me machuquem!"
    n "Ela larga a arma"
    ate "É de brinquedo também, a gente não tem dinheiro para uma escopeta de verdade"
    ate "Mas o que procuram vale muito mais do que dinheiro."
    n "Ela leva vocês até uma porta, digita uma senha em um dispositivo eletrônico e ela abre"
    n "Dentro, vocês veem uma sala, nela há um homem virado de costas"
    n "Ele se vira"
    rdj "Hey!"
    k "Robert Downey Jr.? O que ele está fazendo aqui? Que droga, pensei que fosse ouro."
    ate "Ele não entende português, na real, ele nem sabe que está sendo sequestrado, pensa que está em um filme"
    n "Ele se aproxima de você e começa um monólogo, você não tem a mínima ideia do que ele está falando, mas parece importante"
    ate "Levem ele daqui! Por favor isso era tudo o que a gente tinha!"
    k "Você entregou... Exatamente o que a gente precisava, agora fica pianinha ai!"
    n "Vocês saem do banco acompanhados dele, o monólogo continua, e não parece ter fim"
    k "O que caralhos a gente vai fazer com Robert Downey Jr.?"
    menu:
        "Isso agora é problema do gatovaldo.":
            jump k2m11
        "Vamos levar ele para a base, pode ser útil para o nosso movimento.":
            jump k2m11
label k2m11:
    k "Que seja."
    n "Vocês voltam para a base"
    jump finalkat1

label k2b10:
    k "É... Na verdade a gente já está de saída mesmo..."
    ate "Sim, sim, eu sei que estão, melhor darem no pé logo então."
    n "Você e Katarina viram de costas e começam a andar apressadamente até a porta"
    ate "Mas antes..."
    k "Ah, droga"
    ate "Tirem as máscaras"
    n "Katarina dá meia volta"
    k "O que?"
    ate "Isso mesmo, tirem as máscaras, quero ver os rostos de vocês."
    menu:
        "Melhor obedecer ela":
            jump k2m12
        "A gente está fodido.":
            jump k2m12

label k2m12:
    n "Vocês se sentem ameaçados e tiram as máscaras"
    show katarina default
    n "A recepcionista espreme os olhos na direção de Katarina"
    ate "Espera..."
    ate "Ei!"
    ate "Eu compro suas rações!"
    ate "Sim, é você mesmo, a dona da VSF PETS!"
    menu:
        "O que?":
            jump k2m13
        "VSF?":
            jump k2m13
label k2m13:
    show katarina feliz
    k "Significa Vão Ser Felizes! Isso foi ideia do meu pai, ele achou que seria ótimo na época."
    show katarina smirk
    k "Hoje eu tenho que lidar com os processos, mas é um preço que estou disposta a pagar"
    ate "Olha a minha cachorrinha!"
    n "A recepcionista mostra a foto de um Pitbull tenebroso, seus olhos são apáticos e sua boca está suja de um líquido vermelho"
    show katarina feliz
    ate "É a princesa! Ela adora melancia"
    k "Haha, legal, toma isso aqui"
    n "Katarina tira um papel do bolso"
    k "Um cupom para uma ração de 1 kg! É só apresentá-lo em uma de nossas lojas parceiras!"
    ate "Meu Deus! Muito obrigado, peço perdão por este inconveniente"
    n "Ela abaixa a arma"
    ate "Podem sair."
    n "Vocês saem do banco"
    hide atendente
    show katarina irritada at center
    k "O Gatovaldo nos mete em cada uma, que porra foi essa?"
    menu:
        "Você anda com vales rações no seu bolso?":
            jump k2a15
        "Aquele cachorro fez eu cagar nas calças":
            jump k2b15
label k2a15:
    k "Nunca se sabe quando precisaremos subornar alguém, pets são muito amados hoje em dia, mais do que os próprios humanos."
    k "Não é a toa que eu estou a cada dia mais rica e cada vez mais restaurantes românticos estão falindo."
    jump k2m14
label k2b15:
    k "Espero que a gente nunca tenha o desprazer de se encontrar com uma \"fofura\" daquelas"
    k "A sua cabeça até que parece uma melancia mesmo..."
    n "Você não gostou dessa piada e definitivamente irá reportar isso ao RH da revolução"
    jump k2m14

label k2m14:
    k "Bem, let's go para a base agora."
    n "Vocês voltam para a base"
    jump finalkat1


