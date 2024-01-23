# The script of the game goes in this file.
#transicoes:

init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("bip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

transform siren_tint:
    matrixcolor TintMatrix("f00")
    linear 2.0 matrixcolor TintMatrix("fff")
    linear 2.0 matrixcolor TintMatrix("f00")
    repeat

define gatodissolve = ImageDissolve("transicao.png", 2.0, ramplen=128, reverse=True)
define fadeA = Fade(0.2,0.2,0.2,color="#1338BE")
define fadeL = Fade(0.2,0.2,0.2,color="#f56300")
default jogador1 = True ##Jogador azul = true, jogador laranja = False
default JogadorAtivo = 0 #Variavel usada para captar os pontos da missão, ao final da missão é dado para o jogador ativo

## Variáveis dos dias ##
default aleDay1 = True
default katDay1 = True
default aleDay2 = False
default katDay2 = False
default day1 = True
default day2 = False

##Variáveis de achievements##

default doppelganger = False
default gamsoGamer = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Gatovaldo", image="gatovaldo", callback = low_beep)
define n = Character("", what_prefix='{i}*', what_suffix='*{/i}', callback = low_beep)
define c = Character("Claudia", image="claudia", callback = low_beep)

#Define as conquistáveis e suas respectivas confianças nos jogadores azul e laranja
define character.k = Character("Katarina Kabrera", image="katarina", callback = low_beep)
default k.azul = 0
default k.laranja = 0
define character.a = Character("Alessandra Mallet", image="alessandra", callback = low_beep)
default a.azul = 0
default a.laranja = 0

#Define os valores padroes de confianca para cada jogador

# define azulAlessandra = 0
# define laranjaAlessandra = 0
# define azulKatarina = 0
# define larankaKatarina = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "abandoned.ogg"  volume 2.0
    scene bg quartel

    n "Antes de começarmos..."

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
            show screen char_name_screen([nome1])
            jump jogadorAzul
        
        "[nome2] começa":
            $jogador1 = False
            show screen char_name_screen([nome2])
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

        g "...mas, basicamente, essa porcentagem representa  a quantidade de ovelhas que eu conto antes de dormir enquanto penso no assunto. "
    menu:

        "Caramba, você conta ovelhinhas e pensa sobre a revolução ao mesmo tempo?":
            jump prologoa2
        
        "86,4 ovelhas? o que seria essa \"0,4 ovelha\"?":
            jump prologob2

    label prologoa2:

        g "Sim, para os gatos isso é um grande sinal de que você se importa com algo, a hora da soneca é algo sagrado, fazer qualquer outra coisa se não contar ovelhinhas quando você está prestes a dormir demonstra um grandíssimo interesse por aquilo"
        jump prologom1

    label prologob2:

        g @serio "Nao queiram saber."
        jump prologom1

    label prologob1:

        g "Sim! Impressionante como minha posição permite impressionar meus subordinados com números que nem fazem sentido para humanos"
        jump prologom1

    label prologom1:
        g @feliz "Vocês ainda vão se surpreender ainda mais com a minha grandeza, meus planos nunca deram errado, {size=-10}eu normalmente desisto deles antes que isso aconteça{/size}, mas não dessa vez!"
    
    menu:

        "Hum.... Ok?":
            jump prologoa3

        "SIM CAPITÃO":
            jump prologob3

    label prologoa3:
        with hpunch
        g serio "Vocês não acreditam no meu potencial, né ? Só porque eu sou um gatinho fofinho? Meu QI é maior do que o de {size=+10}TODAS{/size} as gerações de vocês dois {size=+10}JUNTAS!{/size}"

        g  "{cps=*0.2}Vou provar que estão errados.{/cps}"
        jump prologom2
    
    label prologob3:

        g feliz "É disso que eu estou falando."
        jump prologom2

    label prologom2:

        g default "Enfim, como eu ia dizendo, tenho que apresentá-los às novatas da revolução:"

        g withkat "Katarina Kabrera, herdeira, dona da maior produtora de rações para gatos do país"

        g "Ah, e tentem não se irritar, ela pode parecer descolada, mas continua sendo uma patricinha metida, e, como já devem imaginar, a sua participação na revolução é muito valiosa"

        g @feliz "Se é que me entendem"

        show gatovaldo default

        g default "Aliás, ela se voluntariou a participar do movimento após as sanções que o governo impôs aos seus produtos... {p}Vocês devem imaginar o porquê."

    menu:

        "Aquele maldito rato...":
            jump prologoa4
        
        "Pobres gatos...":
            jump prologob4

    label prologoa4:

        g @serio "Sim! É por isso que estamos aqui, e conto com vocês para tirar aquele bostinha do poder" 
        jump prologom3

    label prologob4:
        
        g "São tempos difíceis, mas não sinta dó de uma raça superior"

        g feliz "Aquele idiota não parou para pensar que diminuir as rações felinas e incentivar o crescimento da população de roedores apenas faria com que nós passássemos a come-lôs mais ainda!"

        g "Muahahahahaha"
        jump prologom3

    label prologom3:

        g withale "Bem, dito isso, conheçam tambem Alessandra Mallet."
        
        g "Talvez já tenham ouvido esse nome, uma grande estilista que entrou nas sombras um tempo atrás."

        g "Presumiram que ela tivesse morrido, mas aparentemente esqueceram de procurá-la no seu ateliê!"

        g "Acontece que minha tia-avó já fez morada no forro de lá, {w} hoje ela está em um lugar melhor..."

        g "Em uma noite chuvosa e melancólica a nostalgia acabou me levando ao seu covil, e lá estava ela, desenhando uma roupa super estilosa como se nada tivesse acontecido"

        g "Falei com ela sobre o nosso movimento e ela aceitou participar, engraçado que não tenha questionado um gato falante e aceitado tudo numa boa, mas tudo bem!"

        menu:

            "Meus pesames pela sua tia-avó":
                jump prologoa5

            "Animais falantes não são normais hoje em dia?":
                jump prologob5

        label prologoa5:

            g default "Mas ela não está morta!"

            g "Em nenhum momento disse isso, aliás, ela foi quem mais cuidou de mim depois daquele fatídico acontecimento que me tornou assim"

            g "Eu simplesmente aluguei uma cobertura para ela como agradecimento, é definitivamente um lugar melhor do que aquele forro."
            jump prologom4

        label prologob5:

            g "Claro que não!"

            g @serio "Aquele rato desgramento nem fala direito, o arrombadinho usa um sintetizador,"
            
            show gatovaldo feliz

            extend "poucos sabem da minha existência, até onde sabem ele foi o único afetado pelo experimento."
            jump prologom4

        label prologom4:

            show gatovaldo default

            g "Enfim, preciso que interajam com elas, pois provavelmente serão suas parceiras de missão"

            g "Elas de bom grado ofereceram seus locais de trabalho para que possamos usá-los como postos avançados da revolução, fiquem a vontade para visitarem lá quando quiserem"

            g "Vez ou outra também caso queiram falar comigo provavelmente estarei ou aqui resolvendo assuntos importantes ou no cassino do Zé me divertindo"

            g "Fiquem a vontade para me procurar. "

            g "Ah, e só para deixar claro..."

            show gatovaldo serio

            g "Não sei se confio muito nelas"

            g "Então deixo na mão de vocês investigar se elas são quem realmente dizem ser"

            show gatovaldo default

            g "Como diz o ditado :"

            show gatovaldo feliz

            g "{i}\"Deus dá as suas tarefas mais árduas aos seus soldados mais bobinhos\"{/i}" 
            
            g "Eu, claramente, sou Deus e vocês são os meus soldados mais bobinhos, mas eu gosto de vocês, e confio em vocês, agora, se me permitem, preciso me esconder dentro de algum sofá."

            hide gatovaldo

            n " ele vira as costas e sai da sala, vocês dois se encaram confusos e se perguntam \"que diabos de ditado foi esse?\""

            jump whereToGo

        menu:

            "Para o escritório da Katarina":
                jump d1kat1

            "Para o Atelier da Alessandra":
                jump d1ale1

    # ------------Dia 1---------------
    # ----------Katarina--------------
        label d1kat1:
            play music "escritorio.mp3"

            $ katDay1 = False

            scene bg recepcao
            if jogador1:
                with fadeA
            else:
                with fadeL
            "*Você entra em uma sala de recepção com uma decoração atípica*"
        
            "*Há uma parede cheia de cabeças de animais empalhados, com os olhos trocados por pedras preciosas*"
        
            "*Em um balcão extravagante, próximo a duas espingardas rosas cruzadas entre o símbolo da marca de rações de katarina*"
        
            "*Uma simpática recepcionista te atende*"

            show claudia default at left
            with dissolve

            c "Boa tarde! Como posso te ajudar?"

            menu:
                "Katarina.":
                    jump k1a1

                "Boa tarde, a senhorita Katarina encontra-se no recinto?":
                    jump k1b1
        label k1a1:

            c "KATARINA!"

            n "*A recepcionista grita, mas não obtem nenhuma resposta*"

            c "Peço perdão, só um instante, ela provavelmente deve estar em uma reunião importante"

            n "*Ela disca um número, mas aparentemente não obtem resposta*"

            c "Certo..."

            n "*A recepcionista se levanta de sua cadeira e anda em direção a um grande botão vermelho escrito 'ATAQUE NUCLEAR'*"

            show bg recepcao at siren_tint()

            n "*As luzes começam a piscar em vermelho e um som de alarme começa a tocar*."

            c "Ela deve aparecer a qualquer instante!"

            with hpunch

            n "*A porta do escritório abre escancaradamente*"

            show katarina brava at right
            with moveinright

            k "PORRA ME DIZ QUE É O MEU X-MORTADELA-MALIGNO CLAUDIA, NÃO AGUENTO MAIS ESPERAR"

            show claudia default

            c  "Senhorita katarina! essa pessoa veio procurar por ti, ela é de poucas palavras, parece ser algo importante."

            show katarina feliz

            k "Ah! você faz parte do movimento, o gatovaldo me disse que apareceria."

            k "Claúdia, sempre que algum esquisito assim aparecer por aqui pode liberar direto para a minha sala"

            k "faz parte de uma nova terapia que estou experimentando"

            jump k1m1

            label k1b1:

            c @default "Ela está sim! se não se importa em esperar um pouco, ela está em sua sessão diária de Post-Generic-Slovenian-Punk-Rock."

            c "Enquanto isso, aceita um chá de camomila fervido em sangue de carneiro? é uma bebida típica sueca."

            n "*Ela não aguarda por uma resposta e te serve uma xicará de um líquido viscoso esquisito..."

            n "*Você definitivamente não quer tomar isso*"

            c "Ah! já ia me esquecendo, com licença, preciso acender o incenso do dia, você sabe, para atrair boas energias"

            n "*Ela se dirige a um armário rústico e começa a procurar em uma gaveta*"

            c "Lavanda, orvalho do amanhecer, lírios holandeses, não... hoje é terça, cade o de terça? aqui! te achei, moshpit do slipknot!"

            n "*Ela acende o incenso, e um cheiro de rebeldia toma conta do ambiente, você nem imaginava que seria possível perceber isso olfativamente*"

            with hpunch

            n "*A porta do escritório abre escancaradamente*"

            show katarina irritada at right
            with moveinright

            k "Claudia, mosh pit do slipknot agora é o incenso de quinta, você não viu as alterações que eu te mandei por email?"

            c "Senhorita katarita! Peço perdão, não acontecerá novamente, já irei providenciar o incenso diário correto." 
            
            c"Ah, aliás, essa pessoa veio te procurar, ela recusou o chá sueco, eu te avisei que capim-limão ornava melhor."

            show katarina feliz

            k "Ah! Você faz parte do movimento, o Gatovaldo me disse que apareceria."

            k "Claúdia, sempre que algum esquisito assim aparecer por aqui pode liberar direto para a minha sala"

            k "Faz parte de uma nova terapia que estou experimentando"

            jump k1m1

        label k1m1:

            k "Me acompanhe, meu querido, temos trabalho a fazer."
            
            scene bg escritorio
            hide claudia
            hide katarina
            with gatodissolve

            show katarina default at center
            with moveinleft

            n "*Você acompanha katarina até o seu escritório, ele é recheado de esculturas bizarras e pinturas que remetem ao caos e à destruição, tudo em tons de branco e rosa*"

            show katarina smirk

            k "Você parece espantado, gostou do meu cantinho? descobri quem era o bansky e tranquei ele aqui com baldes de tinta durante 3 dias."

            k "Na verdade, 3 dias para cada vez que eu abrisse a porta e não gostasse do que estava vendo, ele acabou ficando uns 2 meses trancado aqui, mas no fim o resultado foi espetacular!"

            show katarina default

            k "Ele até deu uma sumida da ruas, acho que deve ter ido procurar terapia, mas sinceramente, não entendo o porquê, minha sala tem ar condicionado e eu sempre o alimentava com minhas refeições preferidas"

            n "*Você se lembra de uma aberração gastronômica sendo mencionada anteriormente...*"

            n "*...coitado dele*"

            show katarina feliz

            k "Bem, vamos falar de negócios, sugeri ao seu chefe que a gente fosse explodir alguma coisa, mas ele achou melhor não, fiquei muito frustrada, vou ser franca contigo, entrei na revolução para explodir coisas!"

            show katarina brava

            k "Aquela ratazana imunda acha que pode simplesmente acabar com uma das minhas fontes de renda e ainda deixar milhares de gatinhos por ai com fome? fala sério! eu quero mais é explodir tudo mesmo"

            show katarina smirk

            k "Antes de sair, a gente precisa se conhecer um pouco, pra começar, qual é seu nome?"

            if jogador1:
                azul "Me chamo [nome1]" 
            else:
                laranja "Me chamo [nome2]"

            n "*Após dizer seu nome, ela começa a digitar e ler algumas coisas no computador dela*"

            show katarina default

            k "Huuum... certo, já te conheço, sua vez, me faz uma pergunta"

            menu:
                "Você pesquisou informações minhas na internet?":
                    jump k1a2
                "O que são aquelas cabeças empalhadas com joias no lugar dos olhos?":
                    jump k1b2       

        label k1a2:

            show katarina default

            k "Na realidade não, só pesquisei o significado do seu nome, isso já basta pra mim."

            k "Acho que já podemos ir, eu vou dirigindo!"

            menu:
                "Ir para a missão":
                    jump finalkat1
        label k1b2:

            show katarina feliz

            k "Não se preocupe, elas são falsas, menos a do jacaré, a do leão, a do urso..."

            n "*Ela diz mais alguns nomes*"

            n "*Aparentemente no máximo umas 3 delas são falsas*"

            show katarina triste

            k "Eram do meu pai, eu as herdei quando ele morreu, assim como as joias, apenas uni as duas coisas..."

            show katarina feliz

            k "Acho que já podemos ir, eu vou dirigindo!"

            menu:
                "Ir para a missão":
                    jump finalkat1

        label finalkat1:

            if jogador1:
                $ k.azul += JogadorAtivo
            else:
                $ k.laranja += JogadorAtivo

            jump whereToGo

            
    # ----------Alessandra-------------
        label d1ale1:

            $ aleDay1 = False


    ####################################
    #--------------FIM-----------------#
    ####################################

    #----------Troca de jogador--------
        label whereToGo:
            play music "abandoned.ogg" volume 2.0
            scene bg quartel
            with dissolve

            if katDay1 or aleDay1:

                "E agora, para onde vamos?"

            if jogador1:
                $ jogador1 = False
                show screen char_name_screen([nome2])
            else:
                $ jogador1 = True
                show screen char_name_screen([nome1])


            menu:

                "Para o escritório da Katarina" if katDay1:
                    jump d1kat1

                "Para o Ateliê da Alessandra" if aleDay1:
                    jump d1ale1
            
            jump changeDay                                    

    #-----------Troca de Dia-----------
        label changeDay:
            
            play music "abandoned.ogg" volume 2.0
            scene bg quartel
            with Fade(0.5, 1.0, 0.5)

            "É melhor descansarem durante a noite..."
            #"A pontuação de vocês hoje foi:{p=0.1}[nome1]: [k.azul],[a.azul]{p=0.1}[nome2]: [k.laranja],[a.laranja]"

            if day1:
                $ day2 = True
                $ katDay2 = True
                $ aleDay2 = True
                $ day1 = False

                jump demoFinal

        label demoFinal:
            "Vocês terminaram a demo! Espero que tenham se divertido."

            "Para saberem, [nome1] fez \n[k.azul] de x pontos disponíveis com a Katarina \n e [a.azul] de x pontos disponíveis com a Alessandra"

            
            "E [nome2] fez \n[k.laranja] de x pontos disponíveis com a Katarina \n e [a.laranja] de x pontos disponíveis com a Alessandra"

            "Espero que tenham se divertido, em breve teremos mais missões."
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
