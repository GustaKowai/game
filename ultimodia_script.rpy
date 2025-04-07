label UltimoDia:
  hide screen char_name_screen
  $ k.azul += 3
  $ a.laranja +=3
  n "Vocês chegam ao mesmo tempo no quartel, um silêncio ensurdecedor ecoa pelos corredores."
  n "O silêncio é imediatamente interrompido por um ruído, e os rádios começa a funcionar"
  r "Um grupo de rebeldes está tomando as ruas da cidade, eles parecem caminhar até a sede do governo"
  r "As forças governamentais estão sendo movimentadas, reforçamos que todos os cidadãos devem permanecer em casa, qualquer pessoa encontrada vagando pelas ruas será imediatamente considerada uma ameaça."
  k "COMO VOCÊ PODE?"
  n "Vocês ouvem uma voz vindo do escritório de Gatovaldo, e correm imediatamente para lá."
  n "Ao chegarem, encontram uma cena devastadora."

  scene bg quartel2
  show gatovaldo espancado
  n "Gatovaldo está muito ferido, como se tivesse sido espancado."
  show katarina irritada at right
  n "Katarina está apontando uma arma para ele," 
  show alessandra default at left
  n "e Alessandra está encostada na parede com os braços cruzados."
  tuto "A partir de agora, ambos os jogadores deverão tomar as decisões."
  tuto "A cada questionamento, será perguntado a vocês qual jogador deverá fazer as perguntas, ele então poderá escolher qual personagem ele quer questionar."
  tuto "Personagens tendem a responder melhor quando perguntados por pessoas as quais elas tem {b}afinidade{/b}."
  tuto "Tentem conseguir as informações da melhor forma possível."
  menu:
    tuto "Quem irá perguntar primeiro?"
    "[nome1]":
      $ jogador1 = True
      show screen char_name_screen([nome1],[jogador1])
      $ choice_button_color = "blue"
    "[nome2]":
      $ jogador1 = False
      show screen char_name_screen([nome2],[jogador1])
      $ choice_button_color = "orange"

  menu:
    "Katarina, o que está acontecendo?":
      jump finalday1a
    "Alessandra, por que estão fazendo isso?":
      jump finalday1b

label finalday1a:
  a "A Katarina está tendo o momento pelo qual tanto aguardou"
  g "Ajud…"
  n "Katarina dá uma coronhada em Gatovaldo."
  k "SILÊNCIO!"
  n "Você corre até Gatovaldo, para checar sua situação"
  if (jogador1 and k.azul>1) or (not jogador1 and k.laranja>1):
    n "Katarina parece hesitar em mirar a arma em ti."
    a "Katarina."
    k "S-sai daí!"
    n "Você recua."
  else:
    k "SAI DAÍ!"
    "Ela mira a arma em ti."
    "Você recua."
  jump finalday2

label finalday1b:
  a "A Katarina fez, e ele merece."
  g "Ajud…"
  n "Katarina dá uma coronhada em Gatovaldo."
  k "SILÊNCIO!"
  n "Você corre até Gatovaldo, para chegar sua situação"
  if (jogador1 and a.azul>1) or (not jogador1 and a.laranja>1):
    a "Ele não vai sair daí."
    a "Katarina, pede para ele se afastar."
    k "S-se afaste."
    n "Você recua."
  else:
    a "Katarina."
    n "Katarina mira a arma em ti."
    n "Você recua."
  jump finalday2
label finalday2:
  if sucessoMissao1Ale:
    r "O conflito se intensifica, temos baixas de ambos os lados, mas os revolucionários parecem tomar vantagem," 
    r "eles parecem ter posse de uma tecnologia desconhecida que está transformando os soldados das forças governamentais em tofu,"
    r "outros soldados na região parecem estar confusos com o que está acontecendo."
  else:
    r "O conflito se intensifica, temos baixas de ambos os lados, mas os revolucionários estão sendo subjugados pelas forças governamentais, que têm um arsenal muito mais potente."

  menu:
    "Quem irá perguntar agora?"
    "[nome1]":
      $ jogador1 = True
      show screen char_name_screen([nome1],[jogador1])
      $ choice_button_color = "Blue"
    "[nome2]":
      $ jogador1 = False
      show screen char_name_screen([nome2],[jogador1])
      $ choice_button_color = "orange"

  menu:
    "Questionar Katarina":
      jump finalday2a
    "Questionar Alessandra":
      jump finalday2b

label finalday2a:
  n "Você questiona Katarina para entender o que está acontecendo."
  k "Meu pai…"
  k "Foi ele, foi tudo ele!"
  k "Eu vi, eu tenho certeza!"
  menu:
    "Você precisa se acalmar!":
      jump finalday2c
    "O que você viu?":
      jump finalday2d

label finalday2c:
  if (jogador1 and k.azul>1) or (not jogador1 and k.laranja>1):
    k "Eu não queria que fosse assim…"
    k "EU NÃO QUERIA QUE FOSSE ASSIM!"
    n "Ela começa a chorar, é como se ódio e desolação lutassem pelo controle de suas ações."
  else:
    k "Você não precisa me dizer nada."
    n "Ela aperta a arma com força."
  jump finalday3
label finalday2d:
  k "A Alessandra… Ela me mostrou."
  k "Todas as evidências, tudo."
  k "O acidente, a morte do meu pai, foi ele."
  k "FOI TUDO ELE!"
  n "Ela aperta a arma com força."
  jump finalday3

label finalday2b:
  n  "Você questiona Alessandra para entender o que está acontecendo."

  a "O Gatovaldo foi o responsável pelo meu sequestro."
  a "Ele foi responsável pela morte do pai dela."
  a "Ele é responsável por tudo de ruim, ele acabou com as nossas vidas."

  menu:
    "Como você pode ter certeza?":
      jump finalday2e
    "A gente precisa parar com isso agora, antes que algo mais grave aconteça!":
      jump finalday2f

label finalday2e:
  if (jogador1 and a.azul>1) or (not jogador1 and a.laranja>1):
    a "Eu investiguei."
    a "Eu passei anos investigando."
    a "Todas essas perseguições…"
    n "Alessandra parece abalada"
    a "Vocês precisam confiar em mim."

  else:
    a "Ele é um rato."
    a "Não passa disso."
    a "Usa essa máscara de lutar por uma causa, mas é mais podre do que a pior pessoa desse governo."
    a "Não acho que ele seja literalmente um rato, mas talvez devêssemos arrancar a sua cabeça e descobrir."
  jump finalday3

label finalday2f:
  a "Já é tarde demais."
  n "Alessandra tira uma tesoura do bolso e corta um pedaço da orelha de gatovaldo, que grita de dor."
  a "Vocês precisam entender que estamos fazendo o correto."
  jump finalday3


label finalday3:
  if sucessoMissao1Kat:
    r "O que parece ser um rato está em frenesi, atacando e matando violentamente todos os soldados das forças governamentais que vê pela frente" 
    r "os rebeldes parecem estar alimentando-o com queijos caros, o que pode estar surtindo um efeito psicótico no animal."
  elif rato:
    r "O que parece ser um rato em uma armadura robótica está lutando ao lado dos rebeld-"
    r "As forças governamentais acabaram de explodi-lo."
    r "Recebemos informações de mais baixas dos rebeldes, as tropas parecem estar tomando controle das ruas, os militares informam que em breve tudo passará."
  else:
    r "Recebemos informações de mais baixas dos rebeldes, as tropas parecem estar tomando controle das ruas, os militares informam que em breve tudo passará."

  menu:
    "Quem irá perguntar agora?"
    "[nome1]":
      $ jogador1 = True
      show screen char_name_screen([nome1],[jogador1])
      $ choice_button_color = "Blue"
    "[nome2]":
      $ jogador1 = False
      show screen char_name_screen([nome2],[jogador1])
      $ choice_button_color = "orange"

  menu:
    "Tentar conseguir mais informações de Alessandra":
      jump finalday3a
    "Tentar conseguir mais informações de Katarina":
      jump finalday3b

label finalday3a:
  n "Você insiste em perguntar mais sobre a situação, para obter mais informações."
  if (jogador1 and a.azul>1) or (not jogador1 and a.laranja>1):
    a "Hoje mais cedo eu procurei Katarina, ela estava em uma situação… complicada em seu escritório."
    a "Eu levei ela ao meu ateliê, e mostrei tudo."
    a "Gatovaldo era um mercenário na época, trabalhando a mando de um executivo rival do pai de Katarina."
    a "Ele que causou o acidente."
    g "Mas…"
    k "SILÊNCIO!"
  else:
    a "O Gatovaldo matou o pai da Katarina."
    a "Tudo isso é uma farsa."
    a "Ele está com o governo."
    g "É MENT-"
    k "SILÊNCIO!"
    n "Katarina bate em Gatovaldo."
    a "Vocês precisam estar conosco nessa."
  jump finalday4

label finalday3b:
  n "Você insiste em perguntar mais sobre a situação, para obter mais informações."
  if (jogador1 and k.azul>1) or (not jogador1 and k.laranja>1):
    k "A Alessandra me procurou hoje de manhã."
    k "Ela me mostrou tudo."
    k "Tudo fez sentido."
    k "Eu fiquei descontrolada quando descobri, comecei a destruir tudo que via pela frente."
    k "Alessandra é uma boa amiga, ela não me impediu."
    k "Ele trabalhava como assassino de aluguel para um inimigo de papai."
    k "Ele será o próximo."
    n "Katarina segura a arma com força."
    n "Gatovaldo fica em silêncio."
  else:
    k "Esse VERME não passa de um pau mandado."
    k "Ele me enganou, ele enganou Alessandra, ele enganou vocês!"
    k "A gente precisa terminar o serviço."
  jump finalday4

label finalday4:
  if sucessoMissao2Kat:
    r "Um homem em uma armadura de ferro está dizimando os soldados, armas anti-aéreas devem ser posicionadas logo, mas as baixas das forças governamentais sobem. Ratotávio se pronuncia: “Peguem esse pássaro maldito.”"
  else:
    r "Os rebeldes recuam, eles parecem enfraquecidos. Os militares avançam com as tropas. Em declarações, Ratotávio se pronuncia: “É uma questão de tempo até ganharmos.”"

  menu:
    "Quem irá perguntar agora?"
    "[nome1]":
      $ jogador1 = True
      show screen char_name_screen([nome1],[jogador1])
      $ choice_button_color = "Blue"
    "[nome2]":
      $ jogador1 = False
      show screen char_name_screen([nome2],[jogador1])
      $ choice_button_color = "orange"

  menu:
    "Tentar convencer Alessandra a parar":
      jump finalday3a
    "Tentar convencer Katarina a parar":
      jump finalday3b

  
