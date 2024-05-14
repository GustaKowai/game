# The script of the game goes in this file.
#transicoes:

init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="textSound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="textSound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="textSound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textSound")


#Efeito de luz de sirene
transform siren_tint:
    matrixcolor TintMatrix("f00")
    linear 2.0 matrixcolor TintMatrix("fff")
    linear 2.0 matrixcolor TintMatrix("f00")
    repeat

#Efeito Zoom
transform easeinzoom:
    center
    ease 0.7 zoom 1.5 yoffset 500

transform easeoutzoom:
    center
    ease 0.7 zoom 1.0 yoffset 0


#Efeito de fumaça
transform smokespin:
    xpos 0.5
    ypos 0.5
    linear 5 rotate 360 # take 1 second to rotate 360 degrees
    rotate 0 # reset position counter
    repeat
image smoke = SnowBlossom(At("smoke.png", smokespin), count=1000, border = 200, yspeed=(-200, -5))

define gatodissolve = ImageDissolve("transicao.png", 2.0, ramplen=128, reverse=True) #Transição de gatinho
define morte = Fade(0.2,0,0,color="#fc0505")
define fadeA = Fade(0.2,0.2,0.2,color="#1338BE") #Trasição para o início do jogador azul
define fadeL = Fade(0.2,0.2,0.2,color="#f56300") #Trasição para o início do jogador laranja
define flashbulb = Fade(0.1, 0.0, 0.5, color="#fff")
define explosion = Fade(0.5, 0.5, 0.5, color="#fc0505")
default jogador1 = True ##Jogador azul = true, jogador laranja = False
default JogadorAtivo = 0 #Variavel usada para captar os pontos da missão, ao final da missão é dado para o jogador ativo
default alguem = False

#Variáveis para o jogo de tiro:
default tirosNecessarios = 0
default a8 = False
default b8 = False
default c8 = False
default c8_2 = False
default d8 = False

#Variáveis da investigação:
default xadrez = True
default rifle = False
default vestidotiedye = True
default tofu = False
default vestidorosa = False

## Variáveis dos dias ##
default aleDay1 = True
default katDay1 = True
default aleDay1inv = True
default katDay1inv = True
default aleDay2 = False
default katDay2 = False
default day1 = True
default day2 = False
default day3 = False
default aleDay3 = False
default katDay3 = False

##Variáveis de achievements##

default doppelganger = False
default gamsoGamer = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pag = Character(' ', kind=nvl, color="#c8c8ff")
define e = Character("Eileen", what_prefix='"', what_suffix='"')
define g = Character("Gatovaldo", image="gatovaldo", callback = low_beep, what_prefix='"', what_suffix='"')
define n = Character("", callback = low_beep)
define c = Character("Claudia", image="claudia", callback = low_beep, what_prefix='"', what_suffix='"')
define vo = Character("Vovô sorveteiro", image="vovo", callback = low_beep, what_prefix='"', what_suffix='"')
define gar = Character("Garçom", image="garcom", callback = low_beep, what_prefix='"', what_suffix='"')
define traf = Character("Traficante", image="traficante", callback = low_beep, what_prefix='"', what_suffix='"')
define ate = Character("Atendente", image="atendente", callback = low_beep, what_prefix='"', what_suffix='"')
define rdj = Character("Robert Downey Jr.", image="rdj", callback = low_beep, what_prefix='"', what_suffix='"')
define padre = Character("Padre", image="padre", callback = low_beep, what_prefix='"', what_suffix='"')
define urso = Character("Urso", image="urso", callback = low_beep)
#Define as conquistáveis e suas respectivas confianças nos jogadores azul e laranja
define character.k = Character("Katarina Kabrera", image="katarina", callback = low_beep, what_prefix='"', what_suffix='"')
default k.azul = 0
default k.laranja = 0
define character.a = Character("Alessandra Mallet", image="alessandra", callback = low_beep, what_prefix='"', what_suffix='"')
default a.azul = 0
default a.laranja = 0

#Define os valores padroes de confianca para cada jogador

# define azulAlessandra = 0
# define laranjaAlessandra = 0
# define azulKatarina = 0
# define larankaKatarina = 0

# The game starts here.

label start:

    
    play music "abandoned.ogg"  volume 2.0
    scene bg quartel

    n "Antes de começarmos..."


    #Inicia o minigame do tiro. Ficará aqui enquanto eu não souber onde colocar.
    #jump start_minigame

    python:
        nome1 = renpy.input("Qual o nome do jogador azul?")
        nome1 = nome1.strip() or "Azul"
        nome2 = renpy.input("Qual o nome do jogador laranja?")
        nome2 = nome2.strip() or "Laranja"
    if nome1 == nome2:
        n "Vocês estão de brincadeira comigo? {p} Por favor, escolha um nome melhor."
        python:
            nome2 = renpy.input("Qual o nome do jogador laranja?")
            nome2 = nome2.strip() or "Laranja"
    if nome1 == nome2:
        with vpunch
        n "Ok!{w} Vocês que se virem para saber quem é quem!"
        $ doppelganger = True
        $ renpy.notify("Doppelganger")

    if nome1 == "GAMSo" or nome2 == "GAMSo":
        play sound "honk.ogg"
        "HONK"
        $ gamsoGamer = True
        $ renpy.notify("GAMSo Gamer")
    define azul = Character("[nome1]",color="#1338BE",what_prefix='{color=#1338BE}', what_suffix='{/color}')
    define laranja = Character("[nome2]",color="#f56300",what_prefix='{color=#f56300}', what_suffix='{/color}')

    "Quem irá ser o primeiro a jogar?{w} Recomendamos uma conversa amigável para decidir, porém vocês podem usar de maneiras diferentes."

    "Só por favor, precisamos de ambos os jogadores vivos para dar continuidade"

    menu:
        "[nome1] começa":
            $jogador1 = True
            show screen char_name_screen([nome1],[jogador1])
            jump jogadorAzul
        
        "[nome2] começa":
            $jogador1 = False
            show screen char_name_screen([nome2],[jogador1])
            jump jogadorLaranja

    

    

    # These display lines of dialogue.
    # -------------Prologo-----------------
    label jogadorAzul:
        azul "Olá, eu começo."
        jump prologo0
    label jogadorLaranja:
        laranja "Olá, eu começo."
        jump prologo0

    label prologo0:

        show gatovaldo default

        g "Saudações, {color=#1338BE}[nome1]{/color} e {color=#F56300}[nome2]{/color},  espero poder contar com vocês nessa."

        g @feliz "Como já sabem, em breve todos nós teremos grandes missões a serem cumpridas. "

        g "Será um grande evento, e de acordo com as minhas contas nossa chance de sucesso é de 86,4\%!"
        menu:

            "Como isso sequer pode ser calculado?":
                jump prologoa1

            "Uau!":
                jump prologob1
    
    label prologoa1:

        g "É algo que vai além da compreensão da pequena mente humana de vocês..."

        g "...Mas, basicamente, essa porcentagem representa a quantidade de ovelhas que eu conto antes de dormir enquanto penso no assunto. "
    menu:

        "Caramba, você conta ovelhinhas e pensa sobre a revolução ao mesmo tempo?":
            jump prologoa2
        
        "86,4 ovelhas? O que seria essa \"0,4 ovelha\"?":
            jump prologob2

    label prologoa2:

        g "Sim, para os gatos isso é um grande sinal de que você se importa com algo. A hora da soneca é algo sagrado, fazer qualquer outra coisa se não contar ovelhinhas quando você está prestes a dormir demonstra um grandíssimo interesse por aquilo."
        jump prologom1

    label prologob2:

        g @serio "Não queiram saber."
        jump prologom1

    label prologob1:

        g "Sim! Impressionante como minha posição permite impressionar meus subordinados com números que nem fazem sentido para humanos."
        jump prologom1

    label prologom1:
        g @feliz "Vocês ainda vão se surpreender ainda mais com a minha grandeza, meus planos nunca deram errado. {size=-10}Eu normalmente desisto deles antes que isso aconteça{/size}, mas não dessa vez!"
    
    menu:

        "Hum.... Ok?":
            jump prologoa3

        "SIM CAPITÃO!":
            jump prologob3

    label prologoa3:
        with hpunch
        g serio "Vocês não acreditam no meu potencial, né? Só porque eu sou um gatinho fofinho? Meu QI é maior do que o de {size=+10}TODAS{/size} as gerações de vocês dois {size=+10}JUNTAS!{/size}"

        g  "{cps=*0.2}Vou provar que estão errados.{/cps}"
        jump prologom2
    
    label prologob3:

        g feliz "É disso que eu estou falando."
        jump prologom2

    label prologom2:

        g default "Enfim, como eu ia dizendo, tenho que apresentá-los às novatas da revolução:"

        g withkat "Katarina Kabrera, herdeira rica, dona da maior produtora de rações para gatos do país."

        g "Ah, e tentem não se irritar, ela pode parecer descolada, mas continua sendo uma patricinha metida. E, como já devem imaginar, a sua participação na revolução é muito valiosa."

        g @feliz "...Se é que me entendem."

        show gatovaldo default

        g default "Aliás, ela se voluntariou a participar do movimento após as sanções que o governo impôs aos seus produtos... {p}Vocês devem imaginar o porquê."

    menu:

        "Aquele maldito rato...":
            jump prologoa4
        
        "Pobres gatos...":
            jump prologob4

    label prologoa4:

        g @serio "Sim! É por isso que estamos aqui, e conto com vocês para tirar aquele bostinha do poder." 
        jump prologom3

    label prologob4:
        
        g "São tempos difíceis, mas não sinta dó de uma raça superior."

        g feliz "Aquele idiota não parou para pensar que diminuir as rações felinas e incentivar o crescimento da população de roedores apenas faria com que nós passássemos a come-lôs mais ainda!"

        g "Muahahahahaha!"
        jump prologom3

    label prologom3:

        g withale "Bem, dito isso, conheçam também Alessandra Mallet."
        
        g "Talvez já tenham ouvido esse nome, uma grande estilista que entrou nas sombras um tempo atrás."

        g "Presumiram que ela tivesse morrido, mas aparentemente esqueceram de procurá-la no seu ateliê!"

        g "Acontece que minha tia-avó já fez morada no forro de lá, {w} hoje ela está em um lugar melhor..."

        g "Em uma noite chuvosa e melancólica a nostalgia acabou me levando ao seu covil, e lá estava ela, desenhando uma roupa super estilosa como se nada tivesse acontecido."

        g "Falei com ela sobre o nosso movimento e ela aceitou participar, engraçado que não tenha questionado um gato falante e aceitado tudo numa boa, mas tudo bem!"

        menu:

            "Meus pesames pela sua tia-avó":
                jump prologoa5

            "Animais falantes não são normais hoje em dia?":
                jump prologob5

        label prologoa5:

            g default "Mas ela não está morta!"

            g "Em nenhum momento disse isso, aliás, ela foi quem mais cuidou de mim depois daquele fatídico acontecimento que me tornou assim."

            g "Eu simplesmente aluguei uma cobertura para ela como agradecimento, é definitivamente um lugar melhor do que aquele forro."
            jump prologom4

        label prologob5:

            g "Claro que não!"

            g @serio "Aquele rato desgramento nem fala direito, o arrombadinho usa um sintetizador,"
            
            show gatovaldo feliz

            extend "poucos sabem da minha existência, até onde sabem, ele foi o único afetado pelo experimento."
            jump prologom4

        label prologom4:

            show gatovaldo default

            g "Enfim, preciso que interajam com elas, pois provavelmente serão suas parceiras de missão."

            g "Elas, de bom grado, ofereceram seus locais de trabalho para que possamos usá-los como postos avançados da revolução, fiquem a vontade para visitarem lá quando quiserem."

            g "Vez ou outra também caso queiram falar comigo provavelmente estarei ou aqui resolvendo assuntos importantes. Ou no cassino do Zé me divertindo."

            g "Fiquem a vontade para me procurar."

            g "Ah, e só para deixar claro..."

            show gatovaldo serio

            g "Não sei se confio muito nelas."

            g "Então deixo na mão de vocês investigar se elas são quem realmente dizem ser."

            show gatovaldo default

            g "Como diz o ditado:"

            show gatovaldo feliz

            g "Deus dá as suas tarefas mais árduas aos seus soldados mais bobinhos." 
            
            g "Eu, claramente, sou Deus e vocês são os meus soldados mais bobinhos, mas eu gosto de vocês, e confio em vocês, agora, se me permitem, preciso me esconder dentro de algum sofá."

            hide gatovaldo

            n "Ele vira as costas e sai da sala. {w}Vocês dois se encaram confusos e se perguntam: \"que diabos de ditado foi esse?\""

            jump whereToGo

        menu:

            "Para o escritório da Katarina":
                jump d1kat1

            "Para o Atelier da Alessandra":
                jump d1ale1

    ########################################################################################################################### 
    #####################################--------------FIM-----------------####################################################
    ########################################################################################################################### 

    ########################################################################################################################### 
    ######################################----------Troca de jogador--------###################################################
    ########################################################################################################################### 

        label whereToGo:
            play music "abandoned.ogg" volume 2.0
            scene bg quartel
            with gatodissolve
            $ JogadorAtivo = 0

            if jogador1:
                $ jogador1 = False
                show screen char_name_screen([nome2],[jogador1])
            else:
                $ jogador1 = True
                show screen char_name_screen([nome1],[jogador1])

            if katDay1 or aleDay1:

                if jogador1:
                    "E agora {color=#1338BE}[nome1]{/color}, para onde vamos?"
                else:
                    "E agora {color=#F56300}[nome2]{/color}, para onde vamos?"

            menu:

                "Para o escritório da Katarina" if katDay1:
                    jump d1kat1

                "Para o Ateliê da Alessandra" if aleDay1:
                    jump d1ale1

                "Para o escritório da Katarina" if katDay2:
                    jump d2kat1
                
                "Para o Ateliê da Alessandra" if aleDay2:
                    jump d2ale1

                "Para o escritório da Katarina" if katDay3:
                    jump d3kat1
                
                "Para o Ateliê da Alessandra" if aleDay3:
                    jump d3ale1
            
            jump investigacao #irei deixar comentado enquanto a parte noturna está em desenvolvimento.
            jump changeDay                                    

    ########################################################################################################################### 
    #######################################-----------Troca de Dia-----------##################################################
    ########################################################################################################################### 

        label changeDay:
            
            play music "abandoned.ogg" volume 2.0
            scene bg quartel
            with Fade(0.5, 1.0, 0.5)

            "É melhor descansarem durante o resto da noite..."
            #"A pontuação de vocês hoje foi:{p=0.1}[nome1]: [k.azul],[a.azul]{p=0.1}[nome2]: [k.laranja],[a.laranja]"

            if (k.azul+a.azul >= k.laranja+a.laranja):
                $ jogador1 = False
            if (k.azul+a.azul <= k.laranja+a.laranja):
                $ jogador1 = True
            #determina quem jogou melhor e coloca ele para jogar primeiro no dia seguinte

            if day2:
                $ day3 = True
                $ katDay3 = True
                $ aleDay3 = True
                $ day2 = False

            if day1:
                $ day2 = True
                $ katDay2 = True
                $ aleDay2 = True
                $ day1 = False

            #"As variáveis atuais são:" 
            #"day1[day1], day2[day2], day3[day3]" 
            #"katDay1[katDay1], katDay2[katDay2], katDay3[katDay3]"
            #"aleDay1[aleDay1], aleDay2[aleDay2], aleDay3[aleDay3]"

            jump whereToGo

                #jump demoFinal

    ########################################################################################################################### 
    #######################################----------Final da Demo-----------##################################################
    ###########################################################################################################################

        label demoFinal:

            show gatovaldo default

            g "Vocês terminaram a demo! Espero que tenham se divertido."

            g "Para saberem, {color=#1338BE}[nome1]{/color} fez \n[k.azul] de 10 pontos disponíveis com a Katarina \ne [a.azul] de 10 pontos disponíveis com a Alessandra"

            
            g "E {color=#F56300}[nome2]{/color} fez \n[k.laranja] de 10 pontos disponíveis com a Katarina \ne [a.laranja] de 10 pontos disponíveis com a Alessandra"

            g "Espero que tenham se divertido, em breve teremos mais missões."
#------função usada no final do dia para determinar quanta afeição o personagem ganhou com a Alessandra:

            # if jogador1:
            #     $a.azul += JogadorAtivo
            # else:
            #     $a.laranja += JogadorAtivo

#------função usada no final do dia para determinar quanta afeição o personagem ganhou com a Katarina:

            # if jogador1:
            #     $k.azul += JogadorAtivo
            # else:
            #     $k.laranja += JogadorAtivo
    # This ends the game.

    return

########################################################################################################################### 
############################### -------------Splashcreen------------------################################################# 
########################################################################################################################### 


image splash = "splash.png"
image splash1 = "splash/1.png"
image splash2 = "splash/2.png"
image splash3 = "splash/3.png"
image splash4 = "splash/4.png"
image splash5 = "splash/5.png"
image splash6 = "splash/6.png"

label splashscreen:
    scene black
    with Pause(1)
    play music "windleaves.wav"

    play sound "honk.ogg"
    show text "GAMSo apresenta..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    play sound "honk.ogg"
    show splash5 with dissolve
    with Pause(0.1)

    play sound "honk.ogg"
    show splash3 with dissolve
    with Pause(0.1)
    
    play sound "honk.ogg"
    show splash4
    with Dissolve(1)
    
    play sound "honk.ogg"
    show splash1 with dissolve
    with Pause(1)
    
    play sound "honk.ogg"
    show splash6 with dissolve
    with Pause(1.5)
    stop music fadeout 1.5

    scene black with dissolve
    with Pause(1)


    return
