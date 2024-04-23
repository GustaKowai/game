###########################################################################################################################        
######################################### # ----------Katarina--------------- # ###########################################
###########################################################################################################################

########################################################################################################################### 
########################################### ------------Dia 2--------------- ##############################################
########################################################################################################################### 
label d3kat1:
  play music "escritorio.mp3" volume 0.5
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
  k "A gente conhece os nossos limites, a cada 5 minutos damos uma puxada em um tanque de oxigêni"
  n "Você percebe que tem alguns tanques de oxigênio espalhados pela sala"
  c "Mal posso esperar para tirar o cheiro de carvão de tudo isso daqui quando a gente terminar!"
  n "Cláudia parece genuinamente empolgada com faxinas"
  jump k3m1

label k3b1:
  n "Você bate na porta educadamente"
  k "Pera aí!"
  n "Katarina abre a porta para você"
  scene bg escritorio
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
  k "Tá bom Cláudia! Não importa, melhore na próxima!"
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
  $ tirosNecessarios = 2
  jump start_minigame

  label acertou:
    if a8:
      jump k3a8acertou 
    if b8:
      jump k3b8acertou 
    if c8:
      jump k3c8acertou 
    if d8:
      jump k3d8acertou 
    
    

  label errou:
    if a8:
      jump k3a8errou 
    if b8:
      jump k3b8errou 
    if c8:
      jump k3c8errou 
    if d8:
      jump k3d8errou 
    
    
label k3a8acertou:
  n "Você atira no cervo"
  n "Ele cai"
  show katarina smirk
  k "Nada mal! Você tem o espírito."
  n "Vocês vão até o corpo"
  k @surpresa "O pobrezinho nem sentiu, extremamente preciso, meus parabéns."
  k default "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."


label k3a8errou:
  n "Você atira no cervo"
  n "Ele corre"
  show katarina default
  k @surpresa "Vamos, ele não deve chegar muito longe, você acertou ele."
  n "Vocês correm atrás do cervo, seguindo seu rastro de sangue, e o encontram deitado alguns metros a frente"
  n "Katarina finaliza ele"
  k @triste "Não tem problema, azar de principiante."
  k "Agora vamos levar isso aqui para a Cláudia, ela já deve ter assado uns 50 pães de alho."