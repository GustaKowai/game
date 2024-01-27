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

define gatodissolve = ImageDissolve("transicao.png", 2.0, ramplen=128, reverse=True) #Transição de gatinho
define fadeA = Fade(0.2,0.2,0.2,color="#1338BE") #Trasição para o início do jogador azul
define fadeL = Fade(0.2,0.2,0.2,color="#f56300") #Trasição para o início do jogador laranja
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
            play music "escritorio.mp3" volume 0.5

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
            
            play sound "alarm.wav" loop

            n "*As luzes começam a piscar em vermelho e um som de alarme começa a tocar*."

            c "Ela deve aparecer a qualquer instante!"

            with hpunch

            play sound "doorOpen.ogg"

            n "*A porta do escritório abre escancaradamente*"
           
            show katarina brava at right
            show katarina brava at siren_tint()
            with moveinright

            k "PORRA ME DIZ QUE É O MEU X-MORTADELA-MALIGNO CLAUDIA, NÃO AGUENTO MAIS ESPERAR"

            show claudia default at siren_tint()

            c  "Senhorita katarina! essa pessoa veio procurar por ti, ela é de poucas palavras, parece ser algo importante."

            show katarina feliz at siren_tint()

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

            play sound "doorOpen.ogg"

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

            k "Bem, vamos falar de negócios, sugeri ao seu chefe que a gente fosse explodir alguma coisa..."
            
            show katarina meh

            k "...mas ele achou melhor não, fiquei muito frustrada, vou ser franca contigo, entrei na revolução para explodir coisas!"

            show katarina brava

            k "Aquela ratazana imunda acha que pode simplesmente acabar com uma das minhas fontes de renda e ainda deixar milhares de gatinhos por ai com fome? Fala sério! Eu quero mais é explodir tudo mesmo"

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
                    jump missaokat1
        label k1b2:

            show katarina feliz

            k "Não se preocupe, elas são falsas, menos a do jacaré, a do leão, a do urso..."

            n "Ela diz mais alguns nomes"

            n "Aparentemente no máximo umas 3 delas são falsas"

            show katarina triste

            k "Eram do meu pai, eu as herdei quando ele morreu, assim como as joias, apenas uni as duas coisas..."

            show katarina feliz

            k "Acho que já podemos ir, eu vou dirigindo!"

            menu:
                "Ir para a missão":
                    jump missaokat1

        label missaokat1:

            n "Vocês dirigem até uma estrada deserta, não há nada além de um posto de gasolina abandonado e uma grande torre de telefone nas redondezas"
            show katarina irritada
            k "Que calor da porra, ainda bem que eu vim preparada"

            n "Ela tira uma garrafa de vodka da mochila"

            menu:
                "Você não deveria fazer isso em uma missão":
                    jump k1a3
                "Me dá um pouco?":
                    jump k1b3

        label k1a3:

            show katarina confusa

            k "Isso o que? beber água?"

            n "Você percebe que aquilo na realidade era água, e não entende o porquê de ela usar garrafas de vodka ao invés de garrafas térmicas, parece estar bem quente"

            menu:
                "Qual é a vantagem de carregar garrafas de vidro contigo?":
                    jump k1a4
                "Se jogar numa panela da pra fazer um miojo":
                    jump k1b4
                    

        label k1b3:
            
            show katarina feliz

            k "Claro, eu tenho mais duas!"

            n "Você percebe que aquilo na realidade era água, e não entende o porquê de ela usar garrafas de vodka ao invés de garrafas térmicas, parece estar bem quente"

            menu:
                "Qual é a vantagem de carregar garrafas de vidro contigo?"
                    jump k1a4
                "Se jogar numa panela da pra fazer um miojo"
                    jump k1b4

        label k1a4:
            
            show katarina feliz

            k "Nunca se sabe quando você irá precisar de uma arma improvisada, e além disso, você já quebrou uma garrafa para uma briga de bar? é super divertido"
            
            jump k1m2

        label k1b4:

            show katarina feliz

            k "Sim! se to no inferno vou logo abraçar o capeta, minha bebida favorita do inverno é milkshake."

            jump k1m2

        label k1m2: 

            show katarina default

            k "Bem, acho que a gente ainda tem um tempo"

            k "Aliás, acho que você não deve ter a menor ideia do que a gente está fazendo aqui"

            k "Basicamente, teu chefe, o gato falante, está desconfiando de uma empresa de sorvetes, ele acha que ela está realizando tráfico ilegal de queijos para a sede do governo"

            k "Você sabe, estamos sendo governados por um rato, deve ser mais barato traficar do que lidar com todos os trâmites legais e impostos para a importação desses queijos chiques para cá"

            k "Ou talvez o gatovaldo só queria tomar um sorvetinho e não estava sabendo pedir, então, caso ele esteja errado, pelo menos sairemos daqui com picolés!"

            k "Mas antes, bora naquele posto de gasolina abandonado e depois a gente sobe naquela torre telefonica pra ter uma visão melhor dos arredores e começar a se preparar"

            n "Vocês andam até o posto de gasolina abandonado..."

            n "É definitivamente um posto de gasolina..."

            n "Está definitivamente abandonado..."

            show katarina surpresa

            k "Que maneiro, parece que algumas coisas das prateleiras ainda estão aqui, bora dar uma olhada"

            n "Katarina vira de costas para você, tem uma tarântula enorme nela"

            menu:
                "AHHH (matar a aranha)":
                    jump k1a5
                "er... tem uma tarântula enorme nas suas costas":
                    jump k1b5

        label k1a5:

            show katarina confusa

            k "Que porra foi essa? por que você bateu em m... {w} espera, isso estava nas minhas costas?"

            show katarina surpresa

            k "PUTA QUE PARIU"

            show katarina triste

            k "Não acredito que você fez isso, nunca tinha visto uma dessa espécie, que droga, argh, tudo bem, vamos entrar."

            n "Ela tira uma foto da aranha estraçalhada no chão"
            
            k "Puta que pariu... era uma demonius Dosinfernus..."

            n "Vocês entram na loja, parece ter algumas coisas para explorar"
            
            menu:
                "Procurar nas prateleiras":
                    jump k1a7
                "Procurar no caixa":
                    jump k1b7
                "Procurar no banheiro":
                    jump k1c7
                "Procurar no escritório":
                    jump k1d7

        label k1b5:

            show katarina surpresa

            k "SÉRIO? RÁPIDO, abre o segundo bolso da minha mochila, você vai entender o que fazer"

            n "Você abre o segundo bolso, tem um pote de vidro, um desodorante aerosol e um isqueiro"

            menu:
                "Tacar fogo na aranha":
                    jump k1a6
                "Colocar ela no pote":
                    jump k1b6

        label k1a6:

            n "FUUUUSH"

            n "Você torra a aranha"

            show katarina brava

            k "O QUE CARALHOS VOCÊ ACABOU DE FAZER? EU FALEI O SEGUNDO BOLSO."

            show katarina triste

            k "Ah, espera, droga, acho que guardei meu lança chamas no lugar errado, que porra..."

            k "Enfim, bora entrar nessa loja conveniente"

            n "Vocês entram na loja, parece ter algumas coisas para explorar"

            menu:
                "Procurar nas prateleiras":
                    jump k1a7
                "Procurar no caixa":
                    jump k1b7
                "Procurar no banheiro":
                    jump k1c7
                "Procurar no escritório":
                    jump k1d7


        label k1b6:

            n "Você coloca ela no pote, ela entra sem resistir"

            show katarina muitofeliz

            k "CARALHO, QUE FODA, É UMA DEMONIUS DOSINFERNUS, nunca tinha visto uma dessa espécie, muito obrigada! vou levar ela para o meu zoológico particular."

            show katarina default

            k "Enfim, bora entrar nessa loja conveniente"

            n "Vocês entram na loja, parece ter algumas coisas para explorar"

            n "Vocês entram na loja, parece ter algumas coisas para explorar"

            menu:
                "Procurar nas prateleiras":
                    jump k1a7
                "Procurar no caixa":
                    jump k1b7
                "Procurar no banheiro":
                    jump k1c7
                "Procurar no escritório":
                    jump k1d7

        label k1a7:

            n "Você procura por coisas nas prateleiras, e acha um salgadinho super ardido, ele venceu há 2 anos"

            k "Eai, algo que preste?"

            show katarina muitofeliz

            k "Caralho! esse era edição limitada, valeu!"

            jump k1m3


        label k1b7:
            
            n "Você procura por coisas no caixa, e acha uma escopeta escondida debaixo da maquina registradora"

            k "Eai, algo que preste?"

            show katarina feliz

            "Que massa, mais uma pro meu arsenal."

            jump k1m3

        label k1c7:

            n "Você procura por coisas no banheiro..."

            n "Parece que alguém recentemente deu um uso a ele"

            n "Você se arrepende de sua escolha*"

            k "Eai, algo que preste?"

            show katarina smirk

            "Pelo seu silêncio, julgo que coisa boa não foi"

            jump k1m3


        label k1d7:

            n "Você procura por coisas no escritório, e acha um dvd antigo de um filme de terror trash norueguês"

            k "Eai, algo que preste?"

            show katarina feliz

            "Porra, to querendo ver esse tem meses, obrigada!"

            jump k1m3

        label k1m3:

            show katarina triste

            k "Bom, eu achei isso aqui"

            n "Ela te mostra uma revista, na capa, você vê uma garota usando rosa com o seu pai, o título é: sucesso entre os felinos! pai e filha revelam alguns dos segredos  dos petiscos mais cobiçados pelos gatunos"

            k "Eu até que gostava dele."

            k "Na realidade, eu gostava dele, mas era jovem demais para entender isso."

            k "Eu perdi mais do que um braço naquele atentado"

            menu:
                "Atentado?":
                    jump k1a8
                "Meus sentimentos...":
                    jump k1b8

        label k1a8:

            show katarina irritada

            k "Não quero falar sobre isso no momento, acho que já ta na hora da gente se preparar"

            jump k1m4

        label k1b8:

            show katarina triste

            k "É... obrigado, bora ir se preparar agora"

            jump k1m4

        label k1m4:

            n "Vocês vão até a torre e começam a subir nela, ela parece instável, mas a confiança e animação de katarina te passa uma segurança inexplicávelapós chegarem a uma certa altura, vocês se sentam na beirada, e percebem que definitivamente não há mais nada por perto além dessa torre e daquele posto de gasolina"

            k "É... parece que a gente ta bem isolado aqui mesmo, mas vai ser bom para ver quando o caminhão estiver chegando, bora fazer alguma coisa enquanto isso, abre o terceiro bolso da minha mochila ai e pega alguma coisa"

            menu:
                "Pegar tabuleiro de xadrez":
                    jump k1a9
                "Pegar garrafa de vodka":
                    jump k1b9
                "Pegar rifle de precisão":
                    jump k1c9
        
        label k1a9:
            
            show katarina feliz

            k "Ótima escolha!"

            n "Ela abre o tabuleiro, dentro dele há uma coleção de mini pingas"

            menu:
                "Pegar uma":
                    jump k1a10
                "Recusar":
                    jump k1b10


        label k1b9:

            show katarina feliz

            k "Boa!! tava querendo fazer isso mesmo"

            n "Ela pega a garrafa da sua mão, a arremessa para frente e aguarda ansiosamente ela espatifar no chão "

            show katarina default

            k "Aqui é alto mesmo né"

            n "Vocês permanecem em silêncio por um tempo"

            n "Plaft"

            k "Maneiro..."

            jump k1m5

        label k1c9:

            show katarina default

            k "Não sei se vai ter muito o que fazer com isso aqui, mas bora tentar, toma, ve se você acha alguma coisa"

            n "Você observa pela mira, e avista algumas coisas"

            menu:
                "Atirar em um urubu voando":
                    jump k1a11
                "Atirar no posto de gasolina":
                    jump k1b11
                "Atirar em um animal morto":
                    jump k1c11
                "Não atirar":
                    jump k1d11

        label k1a10:

            show katarina feliz

            k "Toma essa aqui, é massa"

            n "Ela te da uma pinga sabor planta carnívora"

            n "Você já deveria ter aprendido a não confiar nas preferências gastronômicas dela"

            k "Feita em casa!"

            jump k1m5

        label k1b10:

            show katarina meh

            k "Poxa, mas elas estao tao gostosinhas..."

            n "Ela pega uma sabor rabo de rato"

            show katarina smirk

            k "Você deve ter paladar infantil"

            jump k1m5

        label k1a11:

            show katarina default

            n "Você tenta atirar em um urubu voando, mas erra"

            show katarina smirk

            k "Boa tentativa, passa isso ai pra mim"

            n "Ela pega a arma da sua mão, e atira para cima sem mirar"

            n "3 urubus caem do seu lado"

            k "Viu só?"

            jump k1m5

        label k1b11:

            show katarina default

            n "Você atira em uma bomba de combustível no posto"

            n "Nada acontece"

            show katarina feliz

            k "Você é dos meus, infelizmente esse posto ai já tá desativado há um bom tempo."

            n "Mas deria daora se ele explodisse"

            jump k1m5

        label k1c11:

            show katarina default

            n "Você atira em uma carcaça de coiote na distância"

            show katarina feliz

            jump k1m5

        label k1d11:

            show katarina defaul

            n "Você simplesmente não atira"

            show katarina smirk

            k "Ahh, então você é um pacifistinha? tudo bem, nada contra, tenho até amigos que são..."

            jump k1m5

        label k1m5:

            n "Um som de veículo começa a ser ouvido na distância"

            show katarina surpresa

            k "Espera! acho que é o nosso caminhão se aproximando"

            n "Você observa um caminhão de sorvete se aproximando"

            show katarina feliz

            k "É isso mesmo! bora descer"

            n "Vocês descem a torre, a escada é bem precária, você tem a sensação de quase morte ao pisar em um degrau e ele quebrar"

            show katarina default

            k  "Olha, é o seguinte, eu sei que eu sou uma das financiadoras disso daqui, e que você provavelmente questiona muito as minhas decisões e não confia em mim, mas eu peço, deixa que eu lido com isso daqui, siga o meu plano."

            n "Ela abre a mochila, e te dá uma garrafa de ketchup"

            k "Você sabe o que fazer"

            n "Você não sabe o que fazer"

            show katarina feliz

            k "Ok, vejo na sua cara que você não sabe o que fazer, vai lá na estrada, deita, e joga bastante ketchup na sua perna e perto dela, você vai chorar e gritar de dor, pedindo por ajuda"

            show katarina smirk

            k "Se ele acelerar e passar por cima de você, teremos certeza que eles trabalham para o governo e estão preparados para lidar com emboscadas, se ele parar para te ajudar, a gente vai saber que ele provavelmente é só um motorista inocente, você irá dizer que é uma pegadinha, e tudo ficará certo, pode ser?"

            menu:
                "Me sinto feliz de morrer pela causa!":
                    jump k1a12
                "Você quer me usar como um sacrifício humano?":
                    jump k1b12

        label k1a12:
            
            show katarina smirk

            k "Sempre desconfiei que você fosse meio biruta, mas não, não irei deixar você morrer, se ele acelerar eu acerto um tiro no meio da testa dele e você sai correndo, tenho uma boa mira"

            jump k1m6



        label k1b12:

            show katarina surpresa

            k "Claro que não! só estava zoando com a sua cara, eu dou um jeito pra ele não fazer isso, mas fique preparada para correr caso precise"

            jump k1m6

        label k1m6:

            n "Você sente que não tem outra alternativa a não ser a confiar nela, flashs da sua vida inteira passam pela sua cabeça, e o caminhão ainda nem está vindo na sua direção"

            n "Então você vai, deita na rodovia, e espalha o ketchup porcamente na sua perna, só uma pessoa muito ingênua mesmo cairia nisso"

            n "O caminhão se aproxima cada vez mais, você sente um frio na espinha, mas começa a gritar por ajuda, sua atuação é terrível, nem a alma mais inocente da terra seria capaz de acreditar nisso"

            n "Ele chega a uma distância consideravelmente perto de ti... {w} ele se aproxima...{w} e de repente..."

            n "Ele para"

            n "Um senhorzinho muito fofo sai da cabine"

            vo "Meu Deus! você está bem? o que houve?"
            
            menu:
                "É pegadinha!!!! kkkkkk caiu igual um patinho!!!":
                    jump k1a13
                "*Continuar atuando*":
                    jump k1b13

        label k1a13:
            
            vo "O que? mas o que você está fazendo aqui nesse meio do nada?"

            jump k1m7

        label k1b13:

            vo "Minha nossa! esse machucado parece estar feio!"

            jump k1m7

        label k1m7:

            n "Você percebe que ele genuinamente acredita em ti e está evitando olhar para a sua perna"

            n "Você vê katarina chegando de mansinho com um rifle e usando uma bandana na cara"

            show katarina brava

            k "Mãos ao alto velhote!"

            vo "Mas o que"

            k "Isso mesmo! mãos ao alto! isso é um assalto!"

            n "Ele paralisa, parece estar muito assustado"

            show katarina feliz

            k "To te zoando!"

            n "Ela abaixa a arma"

            k "É só uma pegadinha para o meu canal do youtube!"

            vo "Ah.. haha.. entendi... por favor me deixem ir eu tenho familia"

            n "Ele ainda está bem assustado"

            k "Calma! toma aqui"

            n "Ela tira um maço de dinheiro da mochila"

            k "Me vê três picolés!"

            vo "C-claro, s-s-só preciso pegar eles ali na p-parte de trás"

            n "Vocês vão até a parte de trás do caminhão, ele entra, e sai com três picolés de baunilha"

            vo "A-aqui o troco"

            show katarina confusa

            k "Troco? desde quando picolés são tão baratos assim? ah quer saber, pode ficar, pelo susto, vai"

            n "O senhor entra de volta no caminhão, e sai acelerado"

            show katarina brava

            k "Logo o de baunilha... que sabor mais sem graça... é, bem, ele está limpo, precisamos analisar a nossa próxima hipótese"

            menu:
                "Você mandou bem!":
                    jump k1a14
                "É... acho que você precisa tomar um pouco mais de cuidado ao lidar com civis...":
                    jump k1b14

        label k1a14:

            show katarina smirk

            k "Ah, eu sei né! falei poxa, confia em mim!"

            jump k1m8

        label k1b14:

            show katarina smirk

            k "Aquele velhote vai valorizar muito mais a vida dele depois desse susto, tava precisando parar de ser besta também, você é péssimo atuando, não sei como ele caiu naquilo!"
            
            jump k1m8
        
        label k1m8:

            n "Vocês voltam até o carro, o picolé já está quase derretido, o calor está insuportável"

            show katarina feliz

            k "Hey, acho que a gente precisa se conhecer mais, você deve ter percebido que isso é importante para mim, tenho um problema em conviver com estranhos, quem sabe eu não te conto mais sobre o meu pai,eu sei que está curioso"

            n "Você tenta dar uma resposta, mas ela imediatamente liga o som do carro em um volume estrondoso, e começa a acelerar o carro, vocês partem"

            menu:
                "Continuar para a próxima missão":
                    jump finalka1

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
