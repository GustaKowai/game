# The script of the game goes in this file.
#transicoes:

define fadeA = Fade(0.2,0.2,0.2,color="#1338BE")
define fadeL = Fade(0.2,0.2,0.2,color="#f56300")
default jogador1 = True ##Jogador azul = true, jogador laranja = False
default JogadorAtivo = 5 #Variavel usada para captar os pontos da missão, ao final da missão é dado para o jogador ativo

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Gatovaldo", image="gatovaldo")
define n = Character("", what_prefix='{i}*', what_suffix='*{/i}')
define c = Character("Claudia", image="claudia")

#Define as conquistáveis e suas respectivas confianças nos jogadores azul e laranja
define character.k = Character("Katarina Kabrera")
default k.azul = 0
default k.laranja = 0
define character.a = Character("Alessandra Mallet")
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

    scene bg quartel

    "Antes de começarmos..."
    python:
        nome1 = renpy.input("Qual o nome do jogador azul?")
        nome1 = nome1.strip() or "Azul"
        nome2 = renpy.input("Qual o nome do jogador laranja?")
        nome2 = nome2.strip() or "Laranja"

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

    

    show gatovaldo default

    # These display lines of dialogue.
    # -------------Prologo-----------------
    label jogadorAzul:
        azul "Olá, eu começo."
        jump prologo0
    label jogadorLaranja:
        laranja "Olá, eu começo."
        jump prologo0

    label prologo0:

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

        g "mas, basicamente, essa porcentagem representa  a quantidade de ovelhas que eu conto antes de dormir enquanto penso no assunto. "
    menu:

        "Caramba, você conta ovelhinhas e pensa sobre a revolução ao mesmo tempo?":
            jump prologoa2
        
        "86,4 ovelhas? o que seria essa \"0,4 ovelha\"?":
            jump prologob2

    label prologoa2:

        g "sim, para os gatos isso é um grande sinal de que você se importa com algo, a hora da soneca é algo sagrado, fazer qualquer outra coisa se não contar ovelhinhas quando você está prestes a dormir demonstra um grandíssimo interesse por aquilo"
        jump prologom1

    label prologob2:

        g @serio "Nao queiram saber."
        jump prologom1

    label prologob1:

        g "Sim! Impressionante como minha posição permite impressionar meus subordinados com números que nem fazem sentido para humanos"
        jump prologom1

    label prologom1:
        g "A proposito, a afeição de vocês é [a.azul] e [a.laranja]"
        g @feliz "Vocês ainda vão se surpreender ainda mais com a minha grandeza, meus planos nunca deram errado, {size=-10}eu normalmente desisto deles antes que isso aconteça{/size}, mas não dessa vez!"
    
    menu:

        "Hum.... Ok?":
            jump prologoa3

        "SIM CAPITÃO":
            jump prologob3

    label prologoa3:

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

            g @serio "Aquele rato desgramento nem fala direito, o arrombadinho usa um sintetizador, poucos sabem da minha existência, até onde sabem ele foi o único afetado pelo experimento."
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

            n "* ele vira as costas e sai da sala, vocês dois se encaram confusos e se perguntam \"que diabos de ditado foi esse?\"*"

        menu:

            "Para o escritório da Katarina":
                jump d1kat1

            "Para o Atelier da Alessandra":
                jump d1ale1

    # ------------Dia 1---------------
    #-----------Katarina--------------
        label d1kat1:

            scene bg recepcao
            if jogador1:
                with fadeA
            else:
                with fadeL

            "*Você entra em uma sala de recepção com uma decoração atípica*"
        
            "*Há uma parede cheia de cabeças de animais empalhados, com os olhos trocados por pedras preciosas*"
        
            "*Em um balcão extravagante, próximo a duas espingardas rosas cruzadas entre o símbolo da marca de rações de katarina*"
        
            "*Uma simpática recepcionista te atende*"

            show claudia default

            c "Boa tarde! Como posso te ajudar?"

            
    #----------Alessandra-------------
        label d1ale1:
    

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
