###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 

label d2kat1:
    play music "audio/escritorio.wav" volume 0.5
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
    play music "audio/banco.wav" volume 0.5

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
    k "Me desculpe mas ela está pedindo para ser assaltada"
    menu:
        "Vamos agir com cautela.":
            jump k2m15
        "Você está certa.":
            jump k2m3
label k2m15:
    k "Droga, está bem, o que você quer fazer então?"
    menu:
        "Vamos esperar.":
            k "Sério? Desde quando a gente joga pelas regras? E aliás, olha só a cara dela."
            n "Você olha para a atendente, seu rosto transparece claramente que ela não pretende atender vocês tão cedo."
            k "Nossa única chance é colocando uma arma na cabeça dela!"
            menu:
                "Está bem, foda-se.":
                    jump k2m3
                "Vamos colocar uma arma na cabeça dela, porém furtivamente.":
                    k "Tudo bem..."
                    jump k1m16
        "Vamos atacar furtivamente.":
            k "Ótima ideia!"
            jump k1m16
            
label k1m16:
    n "Katarina se levanta e esgueira-se até a porta da recepção."
    k "Vem!"
    n "Você vai até ela, que abre sua mochila e começa a procurar por algo."
    k "Estava bem aqui..."
    k "Cadê?"
    k "Achei!"
    n "Katarina tira uma presilha de cabelo e um revólver comicamente grande da mochila."
    k "O que acha melhor?"
    menu:
        "Lockpick com a presilha.":
            k "Posso tentar..."
            n "Katarina fica concentrada por alguns minutos tentando destrancar a porta."
            k "Isso é difícil..."
            n "Ela derruba o grampo dentro da fechadura."
            k "AH! Eu não acredito!"
            n "Ela se apoia na maçaneta para se lamentar, abrindo a porta instantâneamente."
            menu:
                "Ela estava... Destrancada?":
                    k "Eu..."
                    k "Acho que esqueci de verificar..."
                "Mandou bem!":
                    k "Obrigado! Ter derrubado o grampo lá dentro deve ter acionado um mecanismo secreto que destrancou a porta."
                    k "É a única explicação plausível."
                    n "Ela parece acreditar no que diz."
            n "Vocês entram na sala da atendente, que está de costas."
            k "Olha! Ela está jogando joguinho de tiro!"
            n "Ela está jogando Counter Strike."
            jump k2m16
        "Arrombar a tranca com o revólver.":
            k "É isso aí porra! Sabia que essa furtividade não iria durar."
            n "Katarina faz uma pose, mira e atira."
            n "BANG!"
            n "Ela chuta a porta."
            k "E nem pense em fazer nada estúpido!"
            n "Ela mira o revólver comicamente grande para a atendente, que está de costas, e continua no computador sem expressar reação."
            k "..."
            k "Olha! Ela está jogando joguinho de tiro!"
            n "Ela está jogando Counter Strike, por isso deve ter ignorado os barulhos."
            jump k2m16
label k2m16:
    k "Observe, e aprenda."
    n "Katarina pega o revolver e dá um leve toque com a coronha na cabeça da atendente, que cai desmaiada imediatamente."
    n "Ele é comicamente pesado."
    k "..."
    k "Ela vai ficar bem!"
    menu:
        "Por que não disse sobre esse revolver antes?":
            k "Eu tinha esquecido!"
            k "Estava procurando pelo grampo e acabei encontrando ele."
            k "Achei que seria comicamente engraçado usá-lo como alternativa."
            n "'Comicamente engraçado' é um pleonasmo que não deveria existir."
            jump k2a16
        "Como você consegue manuseá-lo com tanta facilidade?":
            k "..."
            k "Nunca pensei nisso..."
            n "O revólver cai da mão de Katarina, criando uma leve cratera no chão."
            n "Vocês tentam levantá-lo, mas falham."
            k "Talvez fosse o poder da amizade, sei lá, mas infelizmente você acabou com o que quer que seja!"
            jump k2b16
        

label k2a16:
    n "POW!"
    n "Uma porta perto de vocês abre abruptamente."
    n "Vocês veem um homem de terno e óculos escuros, com algum tipo de dispositivo tecnológico na mão, como se fosse uma luv..."
    n "Espera, é o Robert Downey Jr.?"
    k "Espera, Robert Downey Jr.?"
    rdj "I am Iron Man"
    n "Vocês percebem que ele está prestes a atirar em vocês com a luva dele"
    k "CALMA LÁ!"
    n "Katarina mira o revólver comicamente grande para ele."
    rdj "HEY, HEY, HEY, SLOW DOWN!"
    n "Ele abaixa a luva, parece ter se sentido intimidado."
    k "Vamos manter a calma!"
    rdj "Sim! Sim!"
    k "Espera, você entende português?"
    rdj "Sim! Preciso casa de banho!"
    n "Ele aponta para o banheiro."
    k "Ah, lógico."
    k "Pode ir."
    rdj "Obrigado."
    rdj "Você rapariga fixe!"
    k "..."
    k "Tá, agora que estamos sozinhos, podemos investigar melhor isso aqui."
    menu:
        "Você acha que é uma boa ideia deixarmos ele sozinho?":
            k "..."
            k "Puta merda, verdade."
            jump k2a17


        "Vambora!":
            jump k2b17


label k2b17:
    n "Vocês descem até o cofre do banco."
    n "Ele é gigante."
    k "Uau..."
    k "..."
    k "É... A gente meio que não tem a senha..."
    menu:
        "Vamos investigar a recepção.":
            jump k2a18
        "Vamos encontrar o Robert.":
            jump k2b18

label k2a18:
    k "Boa! Aquela recepcionista deve estar escondendo alguma coisa."
    n "Vocês vão até a recepção, a recepcionista continua desacordada."
    k "Por onde começaremos?"
    menu:
        "Gavetas.":
            n "Vocês começam a investigar as gavetas."
            n "Você encontra documentos que indicam a falência do banco, eles estão em uma gaveta que tem um adesivo escrito 'Para a reciclagem'"
            k "Ei, olha isso aqui!"
            n "Katarina te mostra uma gaveta repleta de revistas de fofoca com o Robert Downey Jr. na capa."
            n "Uma delas, que está guardada em uma caixa de vidro, tem um autógrafo."
            k "Caramba... Essa guria..."
            menu:
                "É fissurada nele!":
                    k "Demais!"
                    k "Precisamos encontrá-lo!"
                "Está roubando revistas da recepção!":
                    k "..."
                    k "Não era isso que eu queria dizer, mas realmente, talvez ela esteja!"
                    k "Precisamos encontrá-lo!"
                    
        "Computador.":
            n  "Vocês começam a fuçar pelo computador, o wallpaper é uma foto do Robert Downey Jr."
            n "Vocês abrem o navegador, há uma página aberta no Twitter, logada na conta 'Mundinho RDJ'"
            k "Caramba... Essa guria..."
            menu:
                "É fissurada nele!":
                    k "Demais!"
                    k "Precisamos encontrá-lo!"
                "É adm da página Mundinho RDJ!":
                    n "Katarina parece confusa com o fato de você conhecer essa página."
                    k "..."
                    k "Realmente, parece que ela é..."
                    k "Enfim, precisamos encontrá-lo!"
        "Os bolsos dela.":
            k "..."
            k "Ótima ideia!"
            n "Vocês começam a vasculhar os bolsos dela."
            n "Vocês encontram um celular e uma carteira."
            k "Isso fica comigo."
            n "Katarina embolsa o celular e a carteira."
            k "É para a gente investigar melhor na base!"
            k "Ei, espera!"
            k "Aquele cagão está demorando demais, acho que a gente deveria ir atrás dele."
    jump km18

label km18:
    n "Vocês vão até o banheiro a procura de Robert Downey Jr."
    n "Quando estão prestes a entrar, ele abre a porta abruptamente e tenta correr, porém se depara com vocês."
    n "Ele está suando bastante."
    k "Eita! A coisa foi feia pelo jeito."
    menu:
        "Por que está nervoso?":
            rdj "Muita apertado!"
            k "O que?"
            rdj "Ventana!"
            k "Não estamos te entendendo, amigão."
            n "Ele começa a fazer gestos duvidosos com a mão, tentando explicar com mímica que ele ficou preso na janela do banheiro tentando escapar"
            n "Ninguém além do narrador entende os gestos dele."
            k "Tá, deixa quieto isso aí, por que está correndo?"
        "Por que está agitado?":
            rdj "Eu preciso embora!"
            rdj "Vocês são... maluco!"
            k "O que? Não! A gente não é!"
    rdj "Eu não confio vocês."
    k "Mas... Somos tão legais!"
    menu:
    
        "Dar um sorriso.":
            n "Você dá um sorriso extremamente macabro."
            n "Todos ficam em silêncio por alguns instantes."
            rdj "Yeah... Meu uber chegou!"
            n "Ele sai correndo."
            n "Vocês veem ele se jogando na frente de um carro na rua, que breca instantaneamente, ele entra pela porta do passageiro."
            n "Após alguns segundos parado, o carro parte cantando pneu."
            k "Na próxima vez deixa que eu tento usar o meu charme."
            n "O seu telefone começa a tocar, é o gatovaldo."
            k "É o Gatovaldo? Precisa atender não, a gente vai pessoalmente avisar ele que deu tudo errado."
            k "Depois a gente pode ir tomar uma cachaça lá no meu escritório para afogar as mágoas."
            n "Katarina pega o seu celular tocando e aremessa ele na parede."
            k "..."
            k "Eu te compro um novo."
            k "Vamos embora daqui..."
            jump finalkat1
        "Concordar com Katarina.":
            n "Você diz: 'Sim, Katarina, de fato somos pessoas extremamente divertidas!' de uma maneira que beira o robótico."
            n "Os dois te olham com uma cara esquisita."
            k "Isso normalmente não acontece! Dá um voto de confianca para a gente, vai!"
            rdj "Hm..."
            menu:
                "Fazer cara de coitado.":
                "":
                
        "Apresentar provas concretas.":
            n "Você abre seu celular no briefing da missão e mostra para ele."
            n "Você diz que estão agindo dentro da legalidade das leis que entrarão em vigência quando Gatovaldo assumir o poder."
            n "Ele parece impressionado."
            rdj "Vocês tem um causa nobre."
            rdj "Contem em mim."
            k "Irado!"
            n "O seu telefone começa a tocar."
            n "É o Gatovaldo."
            k "É o Gatovaldo? Deixa esse merdinha no vácuo, a gente tem o apoio de Robert fucking Downey Jr!"
            k "Que tal irmos para meu escritório tomarmos uma birita?"
            rdj "I want to meet the cat first."
            k "Tá bom então sr. Duolingo, primeiro gatovaldo, depois meu escritório!"
            n "Vocês três partem para a base."
            jump finalkat1

    


label k2b18:
    k "Verdade, ele está demorando demais!"
    jump k2a17




label k2a17:
    n "Vocês correm até o banheiro, e encontram ele entalado em uma pequena janela tentando escapar."
    rdj "HELP! HELP!"
    k "Que ótima ideia."
    menu:
        "Empurrar ele para fora":
            n "Você imagina que o objetivo dele era sair, então você começa a empurrá-lo para fora."
            k "NÃO!"
            n "Katarina começa a puxar ele para dentro."
            rdj "aaaaaaaaaaaaaaaaaaaaaaaaa"
            n "Robert começa a gritar"
            rdj "ME LARGUEEEE!"
            k "PUXAAAAAAAAAAA!"
            menu:
                "Fazer mais força.":
                    n "Você desobedece a ordem dos dois e começa a empurrar ainda mais forte."
                    n "É como se você estivesse disputando em um cabo de guerra com Katarina."
                    n "Só que ao invés de uma corda vocês estão quase partindo o Robert Downey Jr. em dois."
                    k "AAAAAAAAAAAAARGH"
                    n "Katarina encarna uma força ancestral e consegue puxar RDJ de volta para o banheiro."
                    n "Ela está ofegante e com os olhos arregalados te encarando."
                    k "Foi bom disputar com você!"
                    n "Ela te estende a mão, vocês se cumprimentam."
                    n "Robert observa vocês dois do chão como dois malucos."
                "Começar a puxar.":
                    n "Você enfim começa a puxar, e logo vocês conseguem trazer ele de volta para o banheiro."
        "Puxar ele para dentro":
            n "Vocês pega em uma perna, Katarina pega na outra, e juntos vocês o puxam para dentro do banheiro novamente."
    k "Escuta aqui, listen."
    k "O que você está fazendo aqui?"
    rdj "..."
    n "Ele parece não ter uma resposta."
    k "Tudo bem, nem tudo precisa de uma explicação, o que importa é que você está aqui, understand?"
    n "Ele acena com a cabeça."
    k "a gente está aqui porque..."
    menu:
        "Fazemos parte de uma revolução que quer tirar do poder o rato autoritário líder de nosso país no momento.":
            n "Ele parece se interessar."
            k "E por isso qualquer ajuda é bem vinda!"
            k "Hoje mesmo, viemos roubar documentos importantes de..."
            n "Seu telefone começa a tocar."
            n "É o Gatovaldo."
            k "É o Gatovaldo? Atende ele aí poxa!"
            jump k2m17

        "Não precisa de explicação.":
            k "..."
            rdj "..."
            k "Acho que nesse caso a gente tem uma boa explicação, então não tem motivo para não dizer para ele."
            k "Estamos roubando informações confidenciais para vantagem competitiva!"
            n "Robert Downey Jr. parece surpreso."
            rdj "But... Isso é errado!"
            n "Ele parece desconfiado."
            k "É... Mas... Na realidade..."
            n "Katarina parece um pouco nervosa."
            n "O seu telefone começa a tocar."
            n "É o Gatovaldo."
            k "É o Gatovaldo? Deixa eu conversar com ele."
            menu:
                "Atender":
                    jump k2m17
                "Dar o celular para a Katarina":
                    n "Katarina atende o celular."
                    k "Alô?"
                    k "Ué, já estamos aqui!"
                    k "O que?"
                    k "A gente veio aqui a toa então?"
                    k "Espera..."
                    k "Encomenda?"
                    n "Katarina tira da mochila a arma que vocês acharam dentro do bolo."
                    n "Ela aperta o gatilho "
                    n " 'Como é grande o meu amor por você' do Roberto Carlos começa a tocar"
                    k "VOCÊ E A CLÁUDIA O QUE?"
                    n "Ela desliga o telefone."
                    k "AQUELE GATO SAFADO!"
                    k "EU VOU PEGAR O FÍGADO DELE E CRIAR UM NOVO SABOR DE RAÇÃO!"
                    rdj "..."
                    rdj "Oh! Preciso ir, my limousine is here."
                    n "Ele sai correndo para fora do banco, pela janela, vocês o veem entrando em um Fiat Palio prata."
                    k "O desgraçado pediu um uber..."
                    k "Droga, não lidei bem com a informação de que o meu chefe e a minha secretária estão..."
                    k "Acabei me descontrolando, acho que ele se assustou."
                    k "De qualquer forma, o Gatovaldo disse que já resolveu tudo."
                    jump k2m14



label k2m17:
    n "Você atende o telefone"
    g "Miau! Quer dizer, Alô? {w}Então vocês já chegaram no banco? {w}É que eu já consegui as informações que eu precisava"
    g "Aparentemente eu me enganei e estava tudo em um banco online, foi fácil hackear e obter tudo."

    menu:
        "Haha ainda não chegamos":
            g "Que alívio!"
        "Poxa que bom haha...":
            g "Poisé né!"

    g "Pode perguntar para a Katarina se a Claudia recebeu a minha encomenda?{w} Fica entre nós, mas é algo bem romantico, quero que somente ela abra"

    menu:
        "Vou perguntar sim haha, tchau!!":
            n "Você desliga o telefone"
            k "Perguntar o que?"
        "Dia dos namorados chegando né, tudo bem, tchau!!":
            n "Você desliga o telefone"
            k "Dia dos namorados? Mas estamos em outubro"
            n "Vocês definitivamente estão em fevereiro."
            rdj "Valentines day!"
            n "Ele tira uma rosa do bolso e a oferece para Katarina."
            k "..."
            n "Katarina pega a rosa, envergonhada."
            k "Niguém nunca..."
            k "Eu nunca ganhei..."
            k "Eu nunca ganhei flores..."
            n "Ela cheira a rosa."
            k "Isso vai dar uma pinga das boas!"
            rdj "Pinga? Caipirinha?"
            k "Sim! Podemos fazer caipirinha!"
            n "Katarina parece ter conquistado Rdj com sua habilidade de fazer pinga com coisas improváveis."
            k "Ei, já que a gente já fez tudo que tinhamos para fazer aqui, vamos embora!"
            k "Pede um uber para a base aí, eu te faço o pix depois, eu e o Robert vamos para casa fabricar pingas!"
            rdj "And caipirinhas."
            k "Com certeza!
            n "Os dois caminham para fora do banco, entram no carro e vão embora."
            n "Resta a você pedir um uber e voltar para a base."
            jump finalkat1



label k2b16:
    n "POW!"
    n "Uma porta perto de vocês abre abruptamente."
    n "Vocês veem um homem de terno e óculos escuros, com algum tipo de dispositivo tecnológico na mão, como se fosse uma luv..."
    n "Espera, é o Robert Downey Jr.?"
    k "Espera, Robert Downey Jr.?"
    rdj "I am Iron Man"
    n "Vocês percebem que ele está carregando alguma espécie de ataque e mira a luva em vocês."
    k "CALMA LÁ!"
    n "Katarina realiza um movimento 'get down mr. president' em ti e vocês dois desviam do raio laser disparado pela luva."
    k "QUE PORRA É ESSA??"
    rdj "Stay on the ground."
    n "Ele pega um telefone, disca um número e começa a falar com alguém."
    n "Katarina sussurra para você:"
    k "O que a gente vai fazer?"
    menu:
        "Usa a arma do bolo.":
            k "Ótima ideia!"
            n "Katarina pega a arma."
            k "Ei, amigão, eu sou inevitável."
            n "Ela aponta para ele."
            rdj "Hey! Calm down, calma!"
            k "Tira essa luva! Gloves! On the ground!"
            n "Ele tira a luva e joga ela no chão."
            n "Katarina mira na luva e aperta o gatilho."
            n "'Como é grande o meu amor por você' do Roberto Carlos começa a tocar"
            k "..."
            k "Droga, o que é isso?"
            k "Está escrito 'Você me mata de paixão no cabo'."
            n "Vocês olham para Robert Downey Jr., ele parece não entender o que está acontecendo e está completamente aterrorizado."
            menu:
                "Tentar pegar as luvas.":
                    n "Você cogita pegar as luvas, e é nesse momento que você dá na cara que o Roberto Carlos não fazia parte dos planos."
                    n "Robert também pula para alcançar as luvas, e vocês começam uma disputa."
                    k "Aaah droga!"
                    menu:
                        "Pedir ajuda para Katarina.":
                            n "Vocês começam a rolar no chão, com medo de levar a pior, você chama por Katarina."
                            jump k2m18

                        "Tentar se virar.":
                            n "Você tenta se garantir no soco, mas Robert parece ter um melhor treinamento do que ti (Que faz parte da linha de frente de uma revolução)."
                            n "Ele claramente está na melhor."
                            n "Katarina tirou um Toddynho da mochila e está observando vocês enquanto lutam."
                            menu:
                                "Pedir ajuda.":
                                    n "Com medo de continuar apanhando, você grita por Katarina"
                                    jump k2m18
                                "Persistir.":
                                    n "Você persiste."
                                    n "Sua força de vontade parece dominá-lo, uma força interior desperta dentro de ti."
                                    n "Você é capaz, você chegou até aqui, não vai perder para um ator com um Oscar roubado."
                                    n "'Ele pertencia ao Ryan Gosling, seu desgraçado!' Você começa a pensar."
                                    n "Você começa a elaborar o seu discurso de vitória."
                                    n "Enquanto isso, Robert alcança a luva."
                                    k "Uhuuuuuuuuul! Isso foi foda!"
                                    jump k2m19
                    
                "Manter pose ameaçadora.":
                    n "Você mantém uma pose ameaçadora, e começa a cantar a música junto com a arma."
                    n "Ele parece confuso e assustado."
                    n "Katarina lentamente se aproxima das luvas e pega elas"
                    k "Tá bom, escuta aqui, a gente não é bandido, então não te sequestraremos, a não ser que você queira."
                    k "Deixamos em suas mãos."
                    rdj "..."
                    n "Ele parece estar mais confuso ainda."
                    menu:
                        "A gente tem redbull à vontade na base!":
                            n "Robert parece ter se interessado."
                        "Somos tipo os vingadores!":
                            n "Robert parece ter se interessado."
                    rdj "Okay! Let's do it."
                    k "Fechou, sr. Duolingo, vamos ir conhecer o gato."
                    n "Vocês vão embora juntos."
                    jump finalkat1
            

        "Vamos aguardar.":
            jump k2m19

label k2m19:
    rdj "On the ground! Now!"
    k "Caaalma Duolingo. Que tal a gente ir tomar um café e resolver isso com calma?"
    rdj "NOW!"
    n "Ele parece nervoso."
    k "Droga, ele não está para brincadeira."
    n "Katarina se deita no chão."
    n "Ela começa a sussurrar para ti."
    k "Escuta aqui, a gente ta meio fodido, vamos precisar escapar daqui."
    menu:
        "Mas e os documentos?":
            k "Foda-se os documentos! É a nossa vida em jogo, você quer ir acabar virando figurante da Marvel?"
            k "A gente precisa distraí-lo e correr. "
        "Mas ele tem uma luva que atira raios laser!":
            k "Eu sei! Isso também me assusta. Por isso criaremos uma distração."
    menu:
        "Usa alguma coisa da sua mochila!":
            k "Boa ideia!"
            n "Katarina discretamente abre a sua mochila e pega um explosivo c4."
            k "Isso vai bastar!"
            menu:
                "puta que pariu.":
                    k "Relaxa!"
                "puta merda.":
                    k "Preocupa não!"
            k "HEY!"
            n "Katarina chama a atenção de Robert."
            n "Ao virar para vocês, Katarina arremessa a bomba na testa dele."
            k "CORRE!!"
            n "Vocês começam a correr em direção à saída."
            menu:
                "POR QUE VOCÊ TEM UMA BOMBA NA MOCHILA?":
                    k "Era uma réplica!"
                    n "Você se acalma um pouco."
                    k "Funcional, mas ela não estava ativa, então é seguro!"
                    n "Você se desacalma."
                "POR QUE VOCÊ TACOU A BOMBA NA TESTA DELE?":
                    k "Era a coisa mais pesada que eu tinha na bolsa!"
                    k "Pelo menos ela não explodiu!"
                    n "Talvez deixar decisões nas mãos de Katarina não seja tão sábio assim..."
            n "Vocês finalmente alcançam o carro."
            k "Bem, em relação a bomba, relaxa, ele vai saber lidar com is..."
            n "BOOOOOOOOOOM"
            n "O banco explode logo atrás de vocês."
            k "..."
            k "Eles vão ficar bem!"
            n "Katarina acelera, e vocês voltam para a base."
            jump finalkat1


        "Vamos esperar para ver o que acontece!":
            k "NÃO! Cansei disso, não podemos continuar entregando nosso destino ao acaso, já é a seg..."
            n "Seu telefone começa a tocar."
            n "É o gatovaldo."
            k "AGORA!"
            n "Katarina pega o celular da sua mão e arremessa-o na cabeça de Robert."
            k "Eu te compro outro!"
            n "Vocês correm, sem olhar para trás."
            n "Até que você fica um pouco curioso, e olha para trás."
            n "Ele parece estar desmaiado."
            k "Ele vai ficar bem!"
            n "Vocês alcançam a saída, entram no carro e começam a ir embora."
            k "..."
            k "Pelo menos temos história para contar!"
            jump finalkat1

label k2m18:
    n "Katarina tira um taser da mochila e eletrocuta Robert."
    rdj "Ouch!"
    n "Ele te larga e se afasta um pouco."
    k "Escuta aqui, seu bostinha, me explica tudo. O que caralhos você está fazendo aqui?"
    rdj "..."
    rdj "Eu não sei..."
    k "Lavagem cerebral. Caso resolvido."
    k "Você vem com a gente."
    rdj "What?"
    k "Isso mesmo. vamos te apresentar para um gatinho."
    n "Vocês prendem as mãos dele com um enforca gato e o guiam até o carro."
    n "Seu telefone começa a tocar, é o Gatovaldo."
    k "Desliga essa merda, foda-se os documentos, conseguimos algo mais importante."
    n "Katarina dá dois tapinhas na cabeça de Robert Downey Jr."
    jump k2m14


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
    ate "Eu vou cair para o ouro de novo!"
    n "Katarina vira para você"
    k "Do que caralhos ela ta falando? Tem ouro aqui em baixo?"
    menu:
        "Sim.":
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
    n "Vocês definitivamente estão em fevereiro."
    jump k2m7

label k2m7:
    n "Você pega a arma da mão dela"
    k "O que você está fazendo?"
    n "Você percebe que no cabo dela está escrito 'Você me mata de paixão'"
    n "Você mira para cima e aperta o gatilho"
    n " 'Como é grande o meu amor por você' do Roberto Carlos começa a tocar"
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
        "2":
            jump k2b11
label k2a11:
    k "1500 homens! Acha que vai ser capaz de parar os nossos 1500 homens? E eu nem te falei o número de mulheres ainda."
    k "Acredite, são muitas também."
    jump k2m10
label k2b11:
    k "2 homens!"
    k "..."
    k "Pode parecer pouco, mas eles são os caras."
    k "Vai por mim, você não seria párea."
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
    k "Você entregou... {w}Exatamente o que a gente precisava, agora fica pianinha ai!"
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
    k "Bem, acho que podemos ir."
    n "Vocês retornam para a base"
    jump finalkat1


