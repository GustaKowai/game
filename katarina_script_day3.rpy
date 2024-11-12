###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 
label d3kat1:
  play music "audio/escritorio.wav" volume 0.5
  $ katDay3 = False
  scene bg recepcao
  if jogador1:
      with fadeA
  else:
      with fadeL

  n "Você chega até o escritório de katarina"
  n "Algo extremamente inusitado está prestes a acontecer, você sabe disso."
  n "Ao chegar na porta do escritório, você percebe uma fumaça vazando pelos vãos dela"
  menu:
    "Arrombar a porta":
      jump k3a1
    "Bater na porta":
      jump k3b1

label k3a1:
  n "Você parte em disparada e dá uma ombrada violenta na porta do escritório, que abre sem muita dificuldade"
  scene bg escritorio
  show smoke
  show katarina surpresa at right
  show claudia default at left
  n "Katarina e Claudia olham assustadas para você"
  n "Elas estão fazendo churrasco"
  show katarina irritada
  k "Boa! {w}Vamos ter que trocar a fechadura mais uma vez"
  menu:
    "Mais uma vez?":
      jump k3a2
    "Vocês vão se sufocar aqui":
      jump k3b2

label k3a2:
  k "Poisé, semana passada eu esqueci a minha chave em casa e tive que arrombar também"
  c "Ela se esqueceu que eu estava aqui dentro e poderia destrancar a porta para ela"
  k "Não esqueci não, você sabe como eu odeio depender dos outros"
  jump k3m1

label k3b2:
  k "A gente conhece os nossos limites, a cada 5 minutos damos uma puxada em um tanque de oxigênio"
  n "Você percebe que tem alguns tanques de oxigênio espalhados pela sala"
  c "Mal posso esperar para tirar o cheiro de carvão de tudo isso daqui quando a gente terminar!"
  n "Cláudia parece genuinamente empolgada com faxinas"
  jump k3m1

label k3b1:
  n "Você bate na porta educadamente"
  k "Pera aí!"
  n "Katarina abre a porta para você"
  scene bg escritorio
  show smoke
  show katarina feliz
  k "Chegou bem na hora!"
  show katarina feliz at right with move
  show claudia default at left
  n "Elas estão fazendo um churrasco, o escritório inteiro está tomado por fumaça"
  menu:
    "Por que não fazer isso em um lugar arejado?":
      jump k3a3
    "Qual é a boa?":
      jump k3b3

label k3a3:
  n "Katarina e Claudia se entreolham"
  n "Elas olham para você"
  show katarina confusa
  k "Verdade né..."
  k "Claudia, por que a gente não fez isso em um lugar arejado?"
  c "Senhorita Kataria, você pediu especificamente para que o churrasco fosse realizado aqui den-"
  show katarina default
  k "Tá bom, Cláudia! Não importa, melhore na próxima!"
  jump k3m1

label k3b3:
  "Bem, esse é o problema, estava precisando de ti justamente por causa disso..."
  jump k3m1

label k3m1:
  n "Você começa a se sentir sufocado"
  n "Você vai em direção a uma das janelas para abri-la"
  "Cláudia e Katarina" "NÃO!!"
  n "Elas te impedem"
  c "Os vizinhos do prédio vão reclamar"
  n "Katarina te passa uma máscara interligada a um tanque de oxigênio"
  n "Você dá uma puxada e se sente revigorado"
  k "Bem, hoje a gente está de folga, o gatovaldo liberou a gente, então pensei:{p} Por que não comemorar?"
  k "Decidimos fazer um churrasco, mas adivinha só, a Cláudia esqueceu da carne!{p} A gente está comendo pão de alho faz umas duas horas"
  n "Claudia abaixa a cabeça"
  c "Desculpa, eu me desconcentrei..."
  k "E agora a gente precisa ir atrás de carne!"
  menu:
    "Vamos! conheço um bom lugar.":
      jump k3a4
    "Sobrou algum pão de alho?":
      jump k3b4
label k3a4:
  k "Sabia que poderia contar com você!"
  k "Enfim, bora lá"
  scene bg carro
  show katarina default
  k "Então, onde é o lugar que você disse que conhecia?"
  menu:
    "Passar a localização de um açougue caro":
      jump k3a5
    "Passar a localização de um açougue barato":
      jump k3b5

label k3b4:
  c "Claro!"
  n "Cláudia abre um pote comicamente grande"
  n "Tem MUITO pão de alho"
  c "Pode levar alguns para a viagem"
  n "Você pega alguns, quase não faz diferença"
  k "Enfim, bora lá"
  scene bg carro
  show katarina default
  n "Vocês vão até o carro, Katarina começa a dirigir"
  jump k3m3


label k3a5:
  n "Você passa a localização de um açougue que ela conseguirá pagar a conta"
  jump k3m2

label k3b5:
  n "Você passa a localização de um açougue que você conseguirá pagar a conta"
  jump k3m2

label k3m2:
  k "Espera, mas isso é dentro da cidade?"
  hide claudia
  show katarina confusa at center with move
  n "Vocês vão até o carro, Katarina começa a dirigir"
  k "Como você pretende conseguir carne dentro da cidade?"
  jump k3m3

label k3m3:
  play music "audio/floresta.mp3" volume 0.5
  scene bg floresta with gatodissolve
  show katarina smirk
  n "Katarina começa a dirigir para fora da cidade"
  n "Você percebe que ela começa a dirigir em direção a floresta"
  k "Sabia que você estava com ideia errada, aposto que queria me levar a um açougue, né?"
  menu:
    "Sim..?":
      jump k3a6
    "E o que exatamente a gente está indo fazer agora?":
      jump k3b6

label k3a6:
  k "Não confio em açougues."
  k "Só eu mesma consigo garantir a qualidade da minha carne."
  jump k3m4
label k3b6:
  k "Você sabe exatamente o que a gente está fazendo aqui."
  jump k3m4

label k3m4:
  n "Katarina pega dois rifles que estavam no banco de trás"
  k @feliz "Vamos caçar."
  n "Ela te entrega um dos rifles"
  k "Esse é o spot, confia em mim"
  n "Katarina guia você até um ponto alto"
  show katarina smirk
  n "Escuta, essa é a primeira vez que faço isso aqui, então vamos com calma"
  menu:
    "Pensei que já fosse experiente nisso":
      jump k3a7
    "Certo... calma...":
      jump k3b7

label k3a7:
  show katarina default
  k "No que? Em caçar? Sou experiente para caralho em caçar, mas é a primeira vez que ensino a alguém"
  k "Vou tentar ter a mesma dedicação que meu pai tinha quando ele me ensinou"
  jump k3m5
label k3b7:
  show katarina default
  k "Isso aí, você vai precisar prender um pouco a sua respiração para um tiro preciso"
  jump k3m5

label k3m5:
  k "Bem, vejo que temos algumas opções aqui..."
  n "Você consegue identificar alguns animais"
  k "Vou deixar essa decisão para ti, só me avisa antes."
  menu:
    "Vamos atirar no cervo":
      jump k3a8
    "Vamos atirar nos coelhos":
      jump k3b8
    "Vamos atirar no urso":
      jump k3c8
    "Vamos atirar nos patos":
      jump k3d8

label k3a8:
  $ a8 = True
  k "Cervo, certo, ótima escolha"
  k "É o seguinte, você precisa acertar no coração, e tem que ser de primeira, não quero ter que ficar finalizando animais"
  k "O meu primeiro foi um cervo também, eu errei o tiro"
  k "Ele correu, mas não chegou tão longe, errei o coração, mas ainda feri bastante ele"
  k "Eu e meu pai seguimos os rastros de sangue, ele estava prestes a acabar com o sofrimento dele{w}, mas eu que tinha começado aquilo{w}, então eu precisava terminar"
  k "Eu finalizei o cervo antes que meu pai pudesse sequer pegar a sua arma"
  k @smirk "Ele nunca me obrigaria a fazer aquilo, mas eu sei como ele se sentiu orgulhoso ao me ver tomando aquela iniciativa."
  k "Bem, agora se concentra"
  n "Você mira no cervo"
  hide katarina
  image cervo = "cervo.png"
  image cervo center = Image("cervo.png")
  show cervo center
  $ acaojogo = "atirar"
  $ tirosNecessarios = 0
  jump start_minigame

    
    
label k3a8acertou:
  hide cervo with morte
  n "Você atira no cervo"
  n "Ele cai"
  show katarina smirk
  k "Nada mal! Você tem o espírito."
  n "Vocês vão até o corpo"
  k @surpresa "O pobrezinho nem sentiu, extremamente preciso, meus parabéns."
  k @default "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  achieve churrasco
  jump k3m6


label k3a8errou:
  hide cervo with moveoutleft
  n "Você atira no cervo"
  n "Ele corre"
  show katarina default
  k @surpresa "Vamos, ele não deve chegar muito longe, você acertou ele."
  n "Vocês correm atrás do cervo, seguindo seu rastro de sangue, e o encontram deitado alguns metros a frente"
  n "Katarina finaliza ele"
  k @triste "Não tem problema, azar de principiante."
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  jump k3m6

label k3b8:
  $ b8 = True
  k @feliz "Coelhos! Certo, vou precisar te ajudar nessa, os bichinhos são pequenos, quanto mais, melhor"
  k "O meu conselho é: Tente não fazer muito estrago, olha o tamanho dessa bala e olha o tamanho deles, não se esquece que a gente vai precisar da carne"
  k @triste "Sempre tive dó dos coelhos, eles me lembram muito animais domésticos"
  k "Uma vez eu e meu pai fomos acampar, em um lugar um tanto quanto isolado, um dia a gente acordou e o nosso carro simplesmente não estava lá"
  k "Provavelmente alguns delinquentes por algum motivo passaram por lá e roubaram ele, tivemos sorte que não fizeram nada com a gente"
  k "A maioria do nosso estoque de comida estava lá, a gente precisou andar um longo caminho até acharmos um sinal de civiliação"
  k @smirk "Você não sabe o quanto eu me alegrei por termos tido a sorte de encontrar coelhos pelo caminho"
  k "Desde então eu passei a vê-los de outra forma, a carne bem temperadinha é uma delícia, acredite em mim!"
  k "Bem, agora se concentra"
  hide katarina
  $ acaojogo = "atirar"
  $ tirosNecessarios = 0
  image coelho = "coelho.png"
  image coelho center = Image("coelho.png", yalign=0.3, xalign=0.48)
  show coelho center
  jump start_minigame

label k3b8acertou:
  hide coelho with morte
  show katarina default
  n "Você atira no coelho"
  n "Ele cai"
  n "Katarina dá 3 tiros"
  k "Vamos lá conferir"
  n "Vocês vão até os coelhos, Katarina pega os 3 que ela acertou"
  n "Você pega o seu"
  k @feliz "Foi um bom tiro, 4 coelhos deve ser suficiente."
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  achieve churrasco
  jump k3m6

label k3b8errou:
  hide coelho  with morte
  show katarina default
  n "Você atira no coelho"
  n "Katarina dá 3 tiros"
  k "Vamos lá conferir"
  n "Vocês vão até os coelhos, Katarina pega os 3 que ela acertou"
  n "Você pega o seu"
  n "Você mal consegue reconhecer que aquilo é um coelho"
  k @meh "É... Vamos deixar esse daqui, 3 devem servir."
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  jump k3m6

label k3c8:
  $ c8 = True
  k @surpresa "O URSO?{w} Maluquice."
  k @smirk "Amo Maluquice!"
  k "Esse vai ser difícil, vamos precisar concentrar esforços, mas vai dar bastante carne!"
  k "A gente tinha um tapete de urso gigantesco na sala, a minha mãe odiava, dizia que era difícil de limpar"
  k "Eu sempre achei meio mórbido também, não via sentido naquilo"
  k "Um dia resolvi questionar o meu pai, ele me explicou que não havia nada de errado em guardar recordações de momentos difíceis"
  k "Ele dizia que a gente precisava se lembrar das adversidades para que pudessemos nos fortalecer quando outras piores surgissem"
  k "\"Por isso cicatrizes impõem respeito\""
  k "Ele tinha uma enorme na barriga, causada por aquele mesmo urso."
  k "Bem, agora se concentra"
  n "Você mira no urso"
  hide katarina
  $ acaojogo = "atirar"
  $ tirosNecessarios = 0
  show urso default
  k "Esse pode ser difícil, não vacila!"
  jump start_minigame

label k3c8acertou:
  $ c8_2 = True
  n "Você e Katarina atiram no urso"
  show urso bravo with morte
  n "Ele solta um rugido"
  k "Acertamos! Mas não acabou, se prepara para mais"
  jump start_minigame

label k3c8acertou2:
  hide urso with morte
  n "Você e Katarina atiram de novo"
  n "O urso cai"
  show katarina default
  k "Boa! Vamos lá, mas cuidado, talvez ainda não tenha sido suficiente"
  n "Vocês vão até o urso, ele está vivo ainda, porém sem forças"
  k @triste "Pobrezinho, a gente acabou com ele"
  k "Olhando pelo lado bom, garantimos mais uns 4 churrascos!"
  n "Katarina finaliza ele, ela é bastante cuidadosa"
  $ churrasco = True
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  achieve churrasco
  jump k3m6

label k3c8errou:
  n "Você e Katarina atiram"
  hide urso with moveoutleft
  n "Ele solta um rugido e foge"
  k @brava "Droga! Acho que não foi suficiente, a gente não é nem louco de ir atrás dele agora"
  k "Talvez a gente possa caçar outra coisa..."
  n "Katarina olha ao redor, e percebe que não há mais nenhum animal"
  k @brava "É... Eles devem ter se assustado com os tiros"
  k "..."
  k "Quer saber?"
  k @triste "Vamos de açougue mesmo, para começar, eu nem mesmo deveria ter te colocado nessa situação"
  n "Ela parece desapontada, mas você não sabe exatamente com o que"
  k "Bora, a Cláudia já deve ter assado uns 50 pães de alho."
  jump k3m6

label k3d8:
  $ d8 = True
  k @surpresa "Patos?{p} Tudo bem, alvos difíceis entretanto, assim que a gente abater o primeiro os outros vão começar a voar"
  k "Vamos precisar acertá-los no ar, não vai ser um problema para mim, mas vou me impressionar bastante se você conseguir"
  k "Eu jogava um joguinho de atirar em patos quando eu era menor"
  k "Queria muito fazer aquilo para valer, atirar em patos de verdade"
  k "Quando disse que queria caçar ao meu pai, ele me levou para atirar em um cervo, acho que eu deveria ter me explicado melhor"
  k "De qualquer maneira, esqueci completamente dessa ideia depois disso, acho que nunca tive outra oportunidade assim"
  k "Pelo menos não com patos selvagens."
  k "Se prepara, vamos precisar de agilidade."
  n "Katarina atira no primeiro pato"
  k "Vai!"
  hide katarina
  image pato = "pato.png"
  image pato center = Image("pato.png")
  show pato center
  $ acaojogo = "atirar"
  $ tirosNecessarios = 3
  jump start_minigame

label k3d8pontos:
  hide pato with moveoutleft
  n "Vocês terminam de atirar nos patos"
  show katarina default
  k "Vamos lá conferir, acho que peguei uns 4."
  n "Vocês vão conferir"
  n "Você acertou [fable_minigame_score]"
  if fable_minigame_score == 0:
    k @surpresa "Nenhum? Achei que até você conseguiria pelo menos um."
  if fable_minigame_score == 1:
    k @meh "É... fez sua parte"
  if fable_minigame_score == 2:
    k @smirk "Nada mal!"
  if fable_minigame_score == 3:
    k @smirk "Você tem jeito nisso."
    achieve churrasco
  if fable_minigame_score == 4:
    k @feliz "Uau! Mandamos bem!"
    achieve churrasco
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."
  jump k3m6

label k3m6:
  scene bg carro
  show katarina default
  n "Vocês entram no carro, Katarina para por um instante, olhando para o horizonte"
  k "O que você faria se tivesse uma máquina do tempo?"
  menu:
      "Eu venderia ela":
        jump k3a9
      "Iria para o passado":
        jump k3b9
      "Iria para o futuro":
        jump k3c9

label k3a9:
  k "Certamente daria uma grana"
  k "Eu já tenho o bastante...{w} Eu voltaria para algum momento no meu passado."
  k "Acho que sob nenhuma circunstância eu seria capaz de evitar tudo o que aconteceu"
  n "Ela aperta o volante"
  k @triste "Então eu voltaria para um momento feliz"
  k "E viveria ele mais uma vez"
  show katarina smirk
  n  "Ela dá um sorriso, e parte para o escritório"
  jump finalkat3

label k3b9:
  k "É, acho que é o que a maioria das pessoas deve responder."
  k "Vivemos de arrependimentos, abraçariamos qualquer chance de mudar algo que nos causa sofrimento."
  k "A dor me fez quem eu sou, não sei se eu mudaria algo"
  n "Ela aperta o volante"
  k "Mas com certeza seria para o passado que eu voltaria, de qualquer forma, eram tempos mais felizes"
  show katarina smirk
  n "Ela dá um sorriso, e parte para o escritório"
  jump finalkat3

label k3c9:
  k "Interessante, eu acho que nunca cogitei isso"
  k "Há tanto para se lembrar no passado e para se preocupar no presente"
  k "Eu tenho um pouco de medo do futuro, ele é incerto"
  k "Então eu voltaria para o passado, talvez seria confortante, poder viver sem incertezas."
  k @triste "Mesmo que nada pudesse ser feito..."
  n "Ela aperta o volante"
  k "Eram tempos mais simples."
  show katarina smirk
  n "Ela dá um sorriso, e parte para o escritório"
  jump finalkat3

label finalkat3:  
  if jogador1:
      $ jogador1Kat3 = True
  else:       
      $ jogador2Kat3 = True
  jump finalkat1
  

