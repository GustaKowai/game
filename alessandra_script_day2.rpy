###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 

label d2ale1:
    default telefonema = False
    default katana = False
    default catnip = False
    default mensagem = False

    play music "atelier.mp3" volume 0.5
    $ aleDay2 = False
    scene bg atelie

    if jogador1:
        with fadeA
    else:
        with fadeL

    show alessandra default
    
    n "Você chega no Ateliê de Alessandra, ela já está aguardando por você na frente"

    a "Eai, preparado? Hoje vamos rezar um pouco."

    menu:
        "Amém":
            jump a2a1
        "O que?":
            jump a2b1
label a2a1:
    a "É isso aí, já tá no espírito"
    jump a2m1
label a2b1:
    a "Isso mesmo que você está pensando!"
    jump a2m1

label a2m1:
    a "Vamos para uma igreja, o Gatovaldo suspeita que ela está servindo de fachada para algo maior."
    a "Eu sei que as suspeitas dele nunca levam a lugar nenhum, mas, se ele mandou, sabe como é, né?"
    n "Seu celular começa a tocar{p}É o Gatovaldo"
    a "Melhor atender, pode ser importante."
    menu:
        "recusar a ligação":
            jump a2a2
        "atender":
            $ telefonema =  True
            jump a2b2
label a2a2:
    n "Você desliga o telefone"
    n "E se sente muito rebelde por isso"
    n "Você imagina que gatovaldo provavelmente admira sua atitude"
    show alessandra confusa
    a "Você acabou de recusar uma ligação do nosso chefe enquanto estamos prestes a ir para uma missão?"
    show alessandra feliz
    a "Ousado, mas você deve estar muito confiante para fazer isso"
    n "Você não tem a menor ideia de porque fez isso"
    show alessandra default
    a "Bom, espero que não tenha sido nada importante"
    n "Provavelmente era"
    a "Acho que já sabemos de tudo que precis-"
    show alessandra confusa
    a "Espera, aquilo ali é uma katana?"
    n "Tem uma katana jogada no chão perto de um bueiro"
    menu:
        "Pegar a katana":
            $ katana = True
            jump a2a7
        "Jogar ela dentro do bueiro":
            jump a2b7

label a2a7:
    n "Você pega a Katana"
    show alessandra surpresa
    a "Uau, quem caralhos perde uma katana?"
    menu:
        "Pode acontecer com qualquer um *Jogar a katana dentro do bueiro*":
            $ katana = False
            jump a2a8
        "Não sei, mas agora ela está nas mãos certas *Fazer uma pose foda*":
            jump a2b8

label a2a8:
    n "Alessandra fica um tempo olhando para o bueiro"
    show alessandra confusa
    a "Por que você fez isso?"
    n "Ela respira profundamente"
    show alessandra smirk
    a "Você realmente está bastante confiante hoje"
    jump a2m2

label a2b8:
    show alessandra confusa
    n "Ela olha com uma cara confusa pra ti"
    n "Você está fazendo uma pose muito foda empunhando a katana"
    show alessandra default
    a "De qualquer forma, espero que seja útil."
    jump a2m2

label a2b2:
    n "Você atende o telefone"
    g "Miau?"
    g "Digo, alô??"
    n "A voz do Gatovaldo está estranha"
    if jogador1:
        g "[nome1] você está aí?" 
    if jogador1==False:
        g "[nome2] você está ai?" 
    n "É catnip, certeza"
    g "Escuta, você precisa entender..."
    n "Ele fica em silêncio por alguns segundos"
    show alessandra confusa
    a "O que ele está dizendo?"
    menu:
        "Tá chapadasso de catnip":
            $ catnip = True
            jump a2a3
        "Aparentemente eu preciso saber de algo":
            jump a2b3
label a2a3:
    show alessandra brava
    a "Ah, era melhor você nem ter atendido, eu deveria ter desconfiado pelo horário"
    n "São 9 da manhã"
    jump a2m3
label a2b3:
    show alessandra surpresa
    a "Que bom que você atendeu, deve ser uma informação importante"
    jump a2m3
label a2m3:
    g "Alô?"
    n "Gatovaldo retorna à chamada"
    g "Burro não é um cavalo dirigindo, burro é um cavalo no meio da pista"
    n "Ele desliga o telefone"
    show alessandra confusa
    a "Ele falou mais alguma coisa?"
    menu:
        "Algo sobre burros e cavalos dirigindo ou no meio de uma pista?":
            $ mensagem = True
            jump a2m4
        "Ele definitivamente está chapado.":
            jump a2m4
label a2m4:
    if mensagem and (catnip):
        show alessandra confusa
        a "Caramba, que catnip é esse que a Katarina anda trazendo para ele?"
    if mensagem and (catnip==False):
        show alessandra smirk
        a "Deve ser um enigma, vamos ficar atentos a tudo que possa remeter a isso."
    if (mensagem==False) and (catnip):
        show alessandra triste
        a "Coitado... "
    if (mensagem==False) and (catnip==False):
        show alessandra default
        a "Ah, ele também já me fez pensar que algo que estava dizendo era importante mas na realidade era só coisa da cabeça dele"
        a "Passei a aprender a reconhecer quando está com a voz mole"
        jump a2m2

label a2m2:
    a "Bom, bora que estamos sem tempo"
    a "Ela aponta para uma moto do outro lado da rua"
    menu:
        "Tenho medo de motos":
            jump a2a5
        "Tem capacete?":
            jump a2b5
label a2a5:
    show alessandra default
    a "Não se preocupe, sou uma boa condutora"
    show alessandra smirk
    a "E afinal, se precisarmos dar fuga será muito mais fácil"
    show alessandra capacete
    jump a2m5
label a2b5:
    show alessandra default
    a "Sim"
    n "Ela pega um capacete e coloca na cabeça"
    show alessandra capacete
    n "Aparentemente só ela tem um capacete"
    jump a2m5
label a2m5:
    n "Vocês montam na moto"
    a "Ah, se alguem brecar a gente você faz o favor de pedir para redirecionaram a palavra ao Danran?"
    menu:
        "O que?"
        "Danran?"
    a "Danrandan danrandan danran"
    n "Ela começa a imitar o som da moto e saí cantando pneu e dando grau"
    scene bg igreja
    n "Após uma viagem assustadora e de algumas experiências de quase morte em sinais vermelhos, vocês chegam ao destino"
    show alessandra capacete
    n "Alessandra tira o capacete e dá uma jogada de cabelo, ele está intacto"
    show alessandra default
    a "Ok, agora a gente precisa ser discreto"
    n "Ela está com uma roupa extremamente estilosa e chamativa"
    a "Me acompanhe, acho que a missa já começou"
    n "Vocês estão diante de uma grande igreja imponente, sua arquitetura remete ao goticismo"
    n "Todas as casas ao redor de vocês são extremamente antigas e muitas delas estão abandonadas"
    a "Isso aqui é bem sinistro"
    n "Vocês abrem a porta da igreja"
    show bg igrejadentro
    n "Ela é imensa por dentro"
    n "O padre estava no meio de um sermão, as cadeiras estão praticamente lotadas"
    n "Ele para imediatamente de falar e todas as pessoas que estão lá olham em conjunto para vocês"
    n "Eles ficam encarando vocês por alguns segundos, e depois olham de volta para o padre, que continua a falar"
    show alessandra assustada
    a "Cara, isso foi bizarro"
    show alessandra default
    a "Acho que tem dois lugares para a gente ali no meio"
    n "Vocês vão até os assentos livres, as pessoas parecem não olhar mais para vocês"
    a "Vamos prestar atenção no que ele diz"
    hide alessandra
    show padre default
    padre "Os cordeiros, OS CORDEIROS! Eles são guiados, eles têm um pastor."
    padre "O pastor guia os cordeiros!"
    padre "Da mesma forma que 2 + 2 são 4."
    padre "Você não vai atrás de bolo em um açougue."
    padre "Entendem o que eu estou falando?"
    n "Todos dizem amém"
    padre "Metáforas nos dizem tantas coisas."
    n "O padre desce do presbitério"
    padre "É uma dádiva da nossa língua "
    n "Ele começa a se aproximar dos fiéis"
    padre "Podemos dizer diretamente que alguém sujo é um porco"
    n "Ele começa a se aproximar de vocês"
    padre "E todos entendem isso"
    n "As pessoas dizem amém"
    padre "Mas agora, meus queridos cordeiros"
    n "Ele chega ao seu lado, e olha para você"
    padre "Mas me diga, cordeirinho, você acha que nós somos burros?"
    n "Ele coloca o microfone perto da sua boca, todos na igreja olham para vocês"
    menu:
        "*Amputar o braço dele com a katana*" if katana:
            jump a2a9
        "S-somos cordeiros":
            jump a2b9
        "Sim":
            jump a2a10
        "Definitivamente":
            jump a2a10
        "Burro não é um cavalo dirigindo, burro é um cavalo no meio da pista." if mensagem:
            jump a2a11
        "Os burros somos nozes.":
            jump a2b11
label a2a9:
    n "Como um ninja, você rapidamente tira pega a katana e amputa o braço do padre"
    n "Você fecha o olho na expectativa de receber um jato de sangue na cara, mas não sente nada"
    n "Quando abre os olhos, você percebe que acabou de amputar o braço de um robô"
    n "A igreja inteira começa a emitir ruídos assustados que lembram..."
    show padre decepado at left
    show alessandra surpresa at right
    a "O QUE VOCÊ ACABOU DE FAZER?"
    a "espera, eles estão gritando como... RATOS!"
    n "Você olha para a boca do padre que está aberta gritando"
    n "Você vê um pequeno rato na região que deveria ser a garganta, ele está usando um pequeno óculos de realidade virtual e segurando duas alavancas"
    n "Ele parece estar gritando também"
    show alessandra assustada
    a "CORRE!!"
    n "Vocês começam a correr, a igreja inteira começa a perseguir vocês"
    a "EU FALEI, AINDA BEM QUE A GENTE VEIO DE MOTO"
    n "Vocês montam na moto"
    show bg igrejamoto
    a "LIGA PRO DANRAN, O CELULAR TA NO MEU BOLSO"
    menu:
        "De novo essa piada?":
            jump a2a12
        "*Segurar firme*":
            jump a2b12
label a2a12:
    show alessandra brava
    a "É SÉRIO!!"
    jump a2m6
label a2b12:
    a "RÁPIDO!!"
    jump a2m6
label a2m6:
    n "Você pega o celular da alessandra em um bolso não euclidiano do vestido dela"
    n "Nos contatos, há um Danran, você liga para ele"
    n "Alô?"
    a "ELE ATENDEU? CÓDIGO MORSA CÓDIGO MORSA"
    n "Ela começa a gritar, enquanto sai empinando com a moto"
    n "Entendido."
    n "Danran desliga o microfone"
    n "Tem uma multidão correndo atrás de vocês pelas ruas"
    show alessandra medo2
    a "FERROU FERROU FERROU"
    n "Vocês estão chegando perto de um cruzamento, há uma rampa na rua que segue, uma rua na direita e uma na esquerda"
    a "RÁPIDO, O QUE ELE DISSE PARA VOCÊ?"
    menu:
        "De boa.":
            jump a2a13
        "Moleza.":
            jump a2b13
        "Entendido.":
            jump a2c13
label a2a13:
    n "Alessandra vira para a direita"
    show alessandra brava
    a "NÃO TEM NADA AQUI"
    n "As pessoas da igreja ainda estão atrás de vocês"
    n "O bairro está tão vazio que parece que ninguém está presenciando isso"
    a "DROGA!"
    n "Alessandra vira para um beco estreito"
    show bg beco
    show alessandra smirk
    a "QUERO VER ELES PASSAREM AQUI"
    n "Ela acelera ainda mais, até que vocês chegam em uma área populada da cidade"
    show bg cidade
    a "Agora eles não chegam mais na gente"
    show alessandra brava
    a "Bom, da próxima vez presta mais atenção no que falam para você, quase nos ferramos bonito."
    show alessandra default
    a "Mas tudo bem, temos algo a contar para o Gatovaldo."
    n "Vocês voltam para a base."
    jump finalale1

label a2b13:
    n "Alessandra acelera em direção à rampa"
    show alessandra feliz
    a "IHUUU!"
    n "Você sente que talvez tenha sido uma má ideia subir nessa moto"
    n "Vocês pousam em segurança"
    show bg cidade
    show alessandra confusa
    a "Espera, não tem nada aqui!"
    show alessandra smirk
    a "Acho que você entendeu errado, mas não tem problema, isso foi maneiro"
    show bg igreja
    n "Você olha para trás, a igreja está parada olhando para vocês de boca aberta, foi de fato impressionante"
    a "Ok, acho que eles pararam, bora voltar para a base, o Gatovaldo vai amar ouvir isso."
    n "Vocês voltam para a base"
    jump finalale1
label a2c13:
    n "Alessandra vira para a esquerda"
    show alessandra smirk
    a "HAHA, boa!"
    n "Ela acelera"
    a "Se prepara, vai exp-"
    n "BOOOM"
    show bg fumaca
    n "Você olha para trás, há apenas fumaça"
    n "Aparentemente a igreja inteira foi dizimada"
    menu:
        "O que foi isso?"
        "Quem fez isso?"
    show alessandra brava
    a "Tenho meus contatos, caso o Gatovaldo pergunte, diga que foi necessário"
    show alessandra feliz
    a "Mas acho que na real ele vai ficar feliz com isso, bora contar para ele"
    n "*Vocês voltam para a base*"
    jump finalale1


    