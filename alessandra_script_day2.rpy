###########################################################################################################################        
######################################### # ----------Alessandra------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 

label d2ale1:
    play music "atelie_intro.ogg" volume 1.0
    queue music "atelie_loop.ogg"
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
    show alessandra confusa with dissolve
    a "Você acabou de recusar uma ligação do nosso chefe enquanto estamos prestes a ir para uma missão?"
    show alessandra feliz with dissolve
    a "Ousado, mas você deve estar muito confiante para fazer isso"
    n "Você não tem a menor ideia de porque fez isso"
    show alessandra default with dissolve
    a "Bom, espero que não tenha sido nada importante"
    n "Provavelmente era"
    a "Acho que já sabemos de tudo que precis-"
    show alessandra confusa with dissolve
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
    show alessandra surpresa with dissolve
    a "Uau, quem caralhos perde uma katana?"
    menu:
        "Pode acontecer com qualquer um *Jogar a katana dentro do bueiro*":
            $ katana = False
            jump a2a8
        "Não sei, mas agora ela está nas mãos certas *Fazer uma pose foda*":
            jump a2b8

label a2a8:
    n "Alessandra fica um tempo olhando para o bueiro"
    show alessandra confusa with dissolve
    a "Por que você fez isso?"
    n "Ela respira profundamente"
    show alessandra smirk with dissolve
    a "Você realmente está bastante confiante hoje"
    jump a2m2

label a2b8:
    show alessandra confusa with dissolve
    n "Ela olha com uma cara confusa pra ti"
    n "Você está fazendo uma pose muito foda empunhando a katana"
    show alessandra default with dissolve
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
    show alessandra confusa with dissolve
    a "O que ele está dizendo?"
    menu:
        "Tá chapadasso de catnip":
            $ catnip = True
            jump a2a3
        "Aparentemente eu preciso saber de algo":
            jump a2b3
label a2a3:
    show alessandra brava with dissolve
    a "Ah, era melhor você nem ter atendido, eu deveria ter desconfiado pelo horário"
    n "São 9 da manhã"
    jump a2m3
label a2b3:
    show alessandra surpresa with dissolve
    a "Que bom que você atendeu, deve ser uma informação importante"
    jump a2m3
label a2m3:
    g "Alô?"
    n "Gatovaldo retorna à chamada"
    g "Burro não é um cavalo dirigindo, burro é um cavalo no meio da pista"
    n "Ele desliga o telefone"
    show alessandra confusa with dissolve
    a "Ele falou mais alguma coisa?"
    menu:
        "Algo sobre burros e cavalos dirigindo ou no meio de uma pista?":
            $ mensagem = True
            jump a2m4
        "Ele definitivamente está chapado.":
            jump a2m4
label a2m4:
    if mensagem and (catnip):
        show alessandra confusa with dissolve
        a "Caramba, que catnip é esse que a Katarina anda trazendo para ele?"
    if mensagem and (catnip==False):
        show alessandra smirk with dissolve
        a "Deve ser um enigma, vamos ficar atentos a tudo que possa remeter a isso."
    if (mensagem==False) and (catnip):
        show alessandra triste with dissolve
        a "Coitado... "
    if (mensagem==False) and (catnip==False):
        show alessandra default with dissolve
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
    show alessandra default with dissolve
    a "Não se preocupe, sou uma boa condutora"
    show alessandra smirk with dissolve
    a "E afinal, se precisarmos dar fuga será muito mais fácil"
    show alessandra capacete with dissolve
    jump a2m5
label a2b5:
    show alessandra default with dissolve
    a "Sim"
    n "Ela pega um capacete e coloca na cabeça"
    show alessandra capacete with dissolve
    n "Aparentemente só ela tem um capacete"
    jump a2m5
label a2m5:
    n "Vocês montam na moto"
    a "Ah, se alguem brecar a gente você faz o favor de pedir para redirecionaram a palavra ao Danran?"
    menu:
        "O que?":
            jump a2m11
        "Danran?":
            jump a2m11
label a2m11:
    a "Danrandan danrandan danran"
    n "Ela começa a imitar o som da moto e saí cantando pneu e dando grau"
    play music "audio/igreja.wav" volume 1.0
    scene bg igreja
    n "Após uma viagem assustadora e de algumas experiências de quase morte em sinais vermelhos, vocês chegam ao destino"
    show alessandra capacete with dissolve
    n "Alessandra tira o capacete e dá uma jogada de cabelo, ele está intacto"
    show alessandra default with dissolve
    a "Ok, agora a gente precisa ser discreto"
    n "Ela está com uma roupa extremamente estilosa e chamativa"
    a "Me acompanhe, acho que a missa já começou"
    n "Vocês estão diante de uma grande igreja imponente, sua arquitetura remete ao goticismo"
    n "Todas as casas ao redor de vocês são extremamente antigas e muitas delas estão abandonadas"
    show alessandra assustada with dissolve
    a "Isso aqui é bem sinistro"
    n "Vocês abrem a porta da igreja"
    show bg igrejadentro with dissolve
    show alessandra default with dissolve
    n "Ela é imensa por dentro"
    n "O padre estava no meio de um sermão, as cadeiras estão praticamente lotadas"
    n "Ele para imediatamente de falar e todas as pessoas que estão lá olham em conjunto para vocês"
    n "Eles ficam encarando vocês por alguns segundos, e depois olham de volta para o padre, que continua a falar"
    show alessandra assustada with dissolve
    a "Cara, isso foi bizarro"
    show alessandra default with dissolve
    a "Acho que tem dois lugares para a gente ali no meio"
    n "Vocês vão até os assentos livres, as pessoas parecem não olhar mais para vocês"
    a "Vamos prestar atenção no que ele diz"
    hide alessandra
    show padre default with dissolve
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
    show alessandra assustada with dissolve
    a "CORRE!!"
    hide padre
    show alessandra medo1 at center
    n "Vocês começam a correr, a igreja inteira começa a perseguir vocês"
    a "EU FALEI, AINDA BEM QUE A GENTE VEIO DE MOTO"
    show alessandra capacete with dissolve
    n "Vocês montam na moto"
    play sound "moto.mp3"
    play music "dejavunointro.mp3" volume 1.0
    show bg igrejamoto
    a "LIGA PRO DANRAN, O CELULAR TA NO MEU BOLSO"
    menu:
        "De novo essa piada?":
            jump a2a12
        "*Segurar firme*":
            jump a2b12
label a2a12:
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
    show alessandra medo2 with dissolve
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
    show alessandra brava with dissolve
    a "NÃO TEM NADA AQUI"
    n "As pessoas da igreja ainda estão atrás de vocês"
    n "O bairro está tão vazio que parece que ninguém está presenciando isso"
    a "DROGA!"
    n "Alessandra vira para um beco estreito"
    show bg beco
    play music "audio/beco.wav" volume 1.0
    show alessandra smirk with dissolve
    a "QUERO VER ELES PASSAREM AQUI"
    n "Ela acelera ainda mais, até que vocês chegam em uma área populada da cidade"
    show bg cidade
    play music "audio/cidade.wav" volume 1.0
    a "Agora eles não chegam mais na gente"
    show alessandra brava with dissolve
    a "Bom, da próxima vez presta mais atenção no que falam para você, quase nos ferramos bonito."
    show alessandra default with dissolve
    a "Mas tudo bem, temos algo a contar para o Gatovaldo."
    n "Vocês voltam para a base."
    jump finalale1

label a2b13:
    n "Alessandra acelera em direção à rampa"
    show alessandra feliz with dissolve
    a "IHUUU!"
    n "Você sente que talvez tenha sido uma má ideia subir nessa moto"
    n "Vocês pousam em segurança"
    show bg cidade
    play music "audio/cidade.wav" volume 1.0
    show alessandra confusa with dissolve
    a "Espera, não tem nada aqui!"
    show alessandra smirk with dissolve
    a "Acho que você entendeu errado, mas não tem problema, isso foi maneiro"
    show bg igreja
    n "Você olha para trás, a igreja está parada olhando para vocês de boca aberta, foi de fato impressionante"
    a "Ok, acho que eles pararam, bora voltar para a base, o Gatovaldo vai amar ouvir isso."
    n "Vocês voltam para a base"
    jump finalale1
label a2c13:
    n "Alessandra vira para a esquerda"
    show alessandra smirk with dissolve
    a "HAHA, boa!"
    n "Ela acelera"
    a "Se prepara, vai exp-"
    play sound "explosion.ogg"
    show bg fumaca
    with explosion
    n "Você olha para trás, há apenas fumaça"
    n "Aparentemente a igreja inteira foi dizimada"
    menu:
        "O que foi isso?":
            jump a2m12
        "Quem fez isso?":
            jump a2m12

label a2m12:
    show alessandra brava with dissolve
    a "Tenho meus contatos, caso o Gatovaldo pergunte, diga que foi necessário"
    show alessandra feliz with dissolve
    a "Mas acho que na real ele vai ficar feliz com isso, bora contar para ele"
    n "*Vocês voltam para a base*"
    achieve O_culto
    $ sucessoMissao2Ale = True
    $ sucesso += 1
    jump finalale1

label a2b9:
    padre "CORRETO!"
    n "O padre grita"
    n "Todos os fiéis gritam amém"
    jump a2m7

label a2a10:
    n "O padre começa a te encarar"
    n "Você sente que algo terrível está prestes a acontecer"
    padre "Errado!"
    padre "Nós somos cordeiros, se lembra?"
    n "Todos os fiéis gritam amém"
    jump a2m7

label a2b11:
    n "O padre olha confuso para ti"
    n "Os fiéis olham confusos para ti"
    padre "Somos nós, você quer dizer?"
    padre "Errado!"
    padre "Nós somos cordeiros, se lembra?"
    n "Todos os fiéis gritam amém"
    jump a2m7

label a2m7:
    n "Alessandra olha assustada para você"
    a "O QUE FOI ISSO?"
    a "Eles estão agindo de uma forma muito estranha, a gente precisa sair daqui agora, a gente não pode virar oferenda de ritual!"
    padre "Cordeirinhos, agora chegou a hora mais importante, a que todos estavamos aguardando, hora da nossa comunhão!"
    n "Os fiéis começam a gritar amém muito animados"
    padre "Se organizem, em filas, sem tumulto, como da última vez."
    padre "Não queremos perder outros fiéis pisoteados, queremos?"
    n "A igreja repete um 'não' em um tom triste"
    padre "Descanse em paz, Kenny."
    padre "Bem, se organizem em filas"
    n "Todos levantam e começam a formar filas"
    hide padre
    show alessandra default at center
    a "E agora? o que a gente faz?"
    menu:
        "Vamos entrar na fila":
            jump a2a14
        "Vamos dar o fora daqui agora":
            jump a2b14
label a2a14:
    show alessandra surpresa with dissolve
    a "VOCÊ ESTÁ MALUCO?"
    a "Eles vão drogar a gente!"
    show alessandra medo1 with dissolve
    a "Eu não posso morrer aqui."
    n "Você entra na fila"
    a "Droga!"
    jump a2m8
label a2b14:
    show alessandra smirk with dissolve
    a "Ótima ideia!"
    n "Vocês começam a andar na direção oposta das pessoas"
    n "Elas olham com uma cara estranha para vocês"
    show alessandra surpresa at right
    show padre default at center
    padre "Não tão cedo, cordeirinhos"
    n "O padre toca no seu ombro"
    padre "Vocês não vão querer perder a comunhão, vão?"
    n "Vocês parecem não ter escolha"
    jump a2m8

label a2m8:
    hide padre
    show alessandra medo1 at center
    n "A fila começa a andar"
    a "A gente não pode morrer aqui..."
    a "Eles vão colocar um parasita na nossa cabeça..."
    show alessandra medo2 with dissolve
    a "Onde é que eu fui me enfiar..."
    menu:
        "Calma!":
            jump a2a15
        "Pelo menos morreremos pela causa":
            jump a2b15
label a2a15:
    a "Estou tentando, mas a situação não ajuda!"
    jump a2m9
label a2b15:
    a "Ah, sim, claro, isso não exclui o fato de que seremos lobotomizados e que vai doer muito!"
    jump a2m9

label a2m9:
    n "Enfim chega a vez de vocês"
    show alessandra medo1 with dissolve
    n "A pessoa responsável pela comunhão pega uma rodela de algo, molha no vinho e te entrega"
    n "Você fecha os olhos e come a rodela misteriosa"
    n "Tem gosto de queijo"
    n "Você olha para Alessandra"
    n "Ela olha para você"
    a "Meu. Deus."
    show alessandra medo2 with dissolve
    n "Ela puxa você pelo braço"
    a "Mas era claro! Como a gente não descobriu antes!"
    menu:
        "Eles são ratos!":
            jump a2a16
        "É um culto de sommeliers de queijo!":
            jump a2b16
label a2a16:
    a "SIM! A gente precisa sair daqui agora"
    jump a2m10
label a2b16:
    a "Não! Eles são ratos!"
    jump a2m10

label a2m10:
    a "Esssas pessoas estão sendo controladas por ratos, talvez como um parasita, não sei, mas há ratos dentro delas!"
    a "O gatovaldo estava certo, tem algo de muito errado com isso aqui, precisamos contar para ele"
    n "Vocês andam em direção a saída, mas alguém para na frente da porta"
    hide alessandra
    show padre default
    padre "Vejo que vocês já tomaram a comunhão, mas preciso ter certeza disso, abram a boca, por favor!"
    n "Ele pega uma lanterna"
    n "Alessandra olha para você"
    menu:
        "Chutar os ovos do padre":
            jump a2a17
        "Imitar um gato bravo":
            jump a2b17
label a2a17:
    n "Você chuta os ovos do padre"
    n "Ele emite sons de dor que parecidos com o de um rato"
    n "Seu pé também dói, você bateu em um pedaço de lata"
    padre "{size=+10}POR QUE QUE ELES PRECISAVAM FAZER OS NERVOS CAUSAREM DORES TÃO REAIS{/size}"
    show padre default at left
    show alessandra medo2 at right
    a "CORRE!!!"
    hide padre
    show alessandra medo2 at center
    n "Vocês correm até a moto"
    show bg igreja
    n "O padre está agonizando de dor no chão, os fiéis parecem estar preocupados de mais com a comunhão"
    show alessandra feliz with dissolve
    a "Essa notícia será bombástica! Bora voltar!"
    n "Vocês voltam para a base"
    jump finalale1

label a2b17:
    n "Você emite sons de gato bravo"
    n "São incrivelmente realistas,{w} você vê muitos vídeos de gato"
    n "O padre parece assustado, ele abre caminho"
    hide padre
    show alessandra surpresa at center
    a "FUNCIONOU! Eles realmente são ratos"
    n "Vocês saem correndo até a moto"
    show bg igreja
    show alessandra feliz with dissolve
    a "Essa notícia será bombástica! Bora voltar!"
    n "Vocês voltam para a base"
    jump finalale1

label a2a11:
    n "Você profere tais palavras incompreensiveis"
    n "O padre te olha estarrecido"
    n "Uma fumaça começa a sair pelos seus ouvidos"
    n "De repente, ele abre a boca e um rato sai de dentro dela, ele corre sem pestanejar"
    play music "igrejaporrada.mp3" volume 1.0
    hide padre
    n "Até que..."
    n "Todos na igreja começam a lutar contra si mesmos"
    show alessandra assustada at center
    a "CUIDADO!"
    n "Alessandra te empurra"
    n "Um candelabro estava voando na sua direção"
    a "A gente precisa sair daqui!"
    n "Vocês olham para a saída, há uma idosa batendo de uma forma extremamente performativa e violenta com a sua bengala em um homem"
    a "Talvez não seja uma boa ideia ir para lá"
    menu:
        "Vamos pelas janelas":
            jump a2a18
        "Vamos pela porta dos fundos":
            jump a2b18
        "Vamos lutar!":
            jump a2c18
label a2a18:
    n "Vocês correm até as janelas"
    n "No caminho, passam por diversas pessoas lutando como se tivessem perdido o controle delas mesmas"
    show alessandra surpresa with dissolve
    a "Seja lá o que você tenha dito, parece que tiltou bastante essas pessoas"
    a "Na realidade, acredito que nao são pessoas."
    n "Katarina aponta para uma mulher que acabou de arrancar a cabeça de um coroinha com um pedaço de um banco"
    n "Há fios debaixo da cabeça dele, um rato sai correndo de dentro de sua boca"
    show alessandra assustada with dissolve
    a "Estão formando uma legião de pessoas controladas por ratos!"
    a "Precisamos contar sobre isso para o Gatovaldo, corre!"
    n "Vocês chegam até uma janela, é um mosaico muito bonito e provavelmente muito antigo"
    n "Alessandra taca uma pedra nela sem pensar duas vezes"
    a "Me dá um pezinho!"
    n "Você ajuda ela a subir"
    n "Quando você está subindo, uma pessoa/robô/rato agarra a sua perma e começa a tentar roer ela"
    menu:
        "Dar um chutão":
            jump a2a19
        "Pedir ajuda":
            jump a2b19
label a2a19:
    n "Você dá um chutão na cabeça dela, que reclama fazendo um som de rato"
    a "Não temos tempo para espancar essas criaturas, bora!"
    jump a2m13
label a2b19:
    n "Alessandra dá um chutão na cabeça dela"
    show alessandra brava with dissolve
    a "Você poderia ter feito isso"
    jump a2m13
label a2m13:
    show bg igreja
    n "Vocês correm até a moto, vários ratos estão saindo de dentro da igreja"
    a "Provavelmente aquela frase confusa do caralho deu um pane no sistema deles"
    a "Vamos dar o fora daqui!"
    n "Vocês voltam para a base"
    achieve O_culto
    $ sucessoMissao2Ale = True
    $ sucesso += 1
    jump finalale1

label a2b18:
    n "Vocês correm até a porta dos fundos"
    n "Quando chegam, há um homem com um bastão de baseball virado de costas para vocês"
    show alessandra default with dissolve
    a "É... Senhor?"
    n "Ele encara Alessandra e diz:{p}JUDITE?"
    n "Ele parte para cima dela"
    show alessandra brava with dissolve
    a "EU NÃO SOU ESSA AÍ NÃO"
    menu:
        "Tentar fazer ele tropeçar":
            jump a2a20
        "Tentar bater nele":
            jump a2b20
label a2a20:
    n "Você estica a perna para tentar fazer ele tropeçar"
    n "Ele estava correndo igual um cachorro louco, portanto de fato tropeça na sua perna"
    n "Ele cai de cara no chão, um ratinho sai correndo de dentro da sua boca"
    show alessandra confusa with dissolve
    a "Quando eu achei que já não dava para ficar mais estranho..."
    jump a2m14
label a2b20:
    n "Você tenta dar um socão nele, mas erra feio"
    n "Erra rude"
    n "Alessandra desvia da tacada de basebal e dá um golpe de karatê nas costas dele, que cai duro"
    n "Um ratinho sai correndo de dentro da sua boca"
    menu:
        "Onde aprendeu isso?":
            jump a2a21
        "Acabou com ele!":
            jump a2b21
label a2a21:
    a "Fiz aulas, ué!"
    jump a2m14
label a2b21:
    show alessandra smirk with dissolve
    a "Eu sempre acabo."
    jump a2m14

label a2m14:
    n "Vocês abrem a porta e dão a volta"
    show bg igreja
    n "Vocês correm até a moto, vários ratos estão saindo de dentro da igreja"
    a "Provavelmente aquela frase confusa do caralho deu um pane no sistema deles"
    a "Vamos dar o fora daqui!"
    n "Vocês voltam para a base"
    achieve O_culto
    $ sucessoMissao2Ale = True
    $ sucesso += 1
    jump finalale1

label a2c18:
    show alessandra brava with dissolve
    a "Aff, eu tava querendo quardar isso aqui para depois!"
    n "Alessandra tira duas submetralhadores de um compartimento secreto de seu vestido"
    show alessandra smirk with dissolve
    a "A gente conseguiria fazer isso do jeito stealth, mas você que escolheu!"
    n "Ela começa a metralhar todo mundo ao redor dela"
    a "Toma, pega isso!"
    n "Ela joga um martelo para você"
    n "Tem alguns robôs vindo na sua direção"
    menu:
        "Fugir":
            jump a2a22
        "Martelar":
            jump a2b22
label a2a22:
    n "Você sai correndo para uma área mais limpa, eles continuam perseguindo você"
    menu:
        "Continuar fugindo":
            jump a2a23
        "Martelar":
            jump a2b22
label a2a23:
    n "Você continua fugindo deles, mas se encontra encurralado"
    menu:
        "Pedir Ajuda":
            jump a2a24
        "Martelar":
            jump a2b22
label a2a24:
    n "Você grita por Alessandra"
    a "Não posso agora"
    n "Ela ainda está metralhando alguns robôs"
    a "Eu te dei um martelo, poxa, martele esses filhos da puta"
    n "Você não vê outra saída"
    jump a2b22

label a2b22:
    menu:
        "Arremessar o martelo":
            jump a2a25
        "Bonk":
            jump a2b25
        "Girar o martelo":
            jump a2c25
        "Martelar o dedinho":
            jump a2d25
label a2a25:
    n "Você aremessa o martelo na cabeça de um deles, que cai no chão"
    n "Um ratinho atordoado sai correndo"
    jump a2m15
label a2b25:
    n "Você levanta os braços e dá uma martelada com toda a sua força na cabeça de um deles"
    n "Você sente o metal amassar"
    n "Quando ele cai, nenhum ratinho sai de sua boca"
    jump a2m15
label a2c25:
    n "Você sai girando o martelo e derruba vários deles"
    n "Vários ratinhos saem correndo"
    jump a2m15
label a2d25:
    n "Você martela o dedinho do pé de um deles"
    n "Um ratinho é ejetado pela boca e cai lentamente de paraquedas no chão, ele sai correndo após isso"
    n "Você repete o processo, vários ratos caem de paraquedas"
    jump a2m15

label a2m15:
    show alessandra smirk with dissolve
    a "Uau, você realmente se virou ein! "
    n "Diz Alessandra, sentada em uma pilha de corpos de lata"
    a "Acho que a gente acabou com todos eles"
    n "Ela acabou com todos eles, você acabou com uns 5, no máximo"
    show alessandra default with dissolve
    a "Bem, precisamos reportar tudo o que aconteceu ao gatovaldo, bora."
    play music "audio/igreja.wav" volume 1.0 
    show bg igreja
    n "Vocês dois saem da igreja, montam na moto, e partem para a base"
    achieve O_culto
    $ sucessoMissao2Ale = True
    $ sucesso += 1
    if jogador1:
        $ jogador1Ale2 = True
    else:       
        $ jogador2Ale2 = True
    jump finalale1