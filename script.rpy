﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Gatovaldo")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg quartel

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show gatovaldo default

    # These display lines of dialogue.

    g "Saudações, (nome 1) e (nome2),  espero poder contar com vocês nessa."

    g "Como já sabem, em breve todos nós teremos grandes missões a serem cumpridas. "

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

        show gatovaldo serio

        g "Nao queiram saber."
        jump prologom1

    label prologob1:

        g "Sim! impressionante como minha posição permite impressionar meus subordinados com números que nem fazem sentido para humanos"
        jump prologom1

    label prologom1:

        show gatovaldo feliz

        g "vocês ainda vão se surpreender ainda mais com a minha grandeza, meus planos nunca deram errado, eu normalmente desisto deles antes que isso aconteça, mas não dessa vez!"
    
    menu:

        "Hum.... Ok?":
            jump prologoa3

        "SIM CAPITÃO":
            jump prologob3

    label prologoa3:

        show gatovaldo serio

        g "Vocês não acreditam no meu potencial, né ? Só porque eu sou um gatinho fofinho? Meu QI é maior do que o de TODAS as gerações de vocês dois JUNTAS!"

        g  "vou provar que estão errados."
        jump prologom2
    
    label prologob3:

        show gatovaldo feliz

        g "É disso que eu estou falando."
        jump prologom2

    label prologom2:

        show gatovaldo default

        g "Enfim, como eu ia dizendo, tenho que apresentá-los às novatas da revolução:"

        show gatovaldo withkat

        g "Katarina Kabrera, herdeira, dona da maior produtora de rações para gatos do país"

        g "Ah, e tentem não se irritar, ela pode parecer descolada, mas continua sendo uma patricinha metida, e, como já devem imaginar, a sua participação na revolução é muito valiosa"

        show gatovaldo feliz

        g "Se é que me entendem"

        show gatovaldo default

        g "Aliás, ela se voluntariou a participar do movimento após as sanções que o governo impos aos seus produtos... Vocês devem imaginar o porquê."

    menu:

        "Aquele maldito rato...":
            jump prologoa4
        
        "Pobres gatos...":
            jump prologob4

    label prologoa4:

        show gatovaldo serio

        g "Sim! É por isso que estamos aqui, e conto com vocês para tirar aquele bostinha do poder" 
        jump prologom3

    label prologob4:
        
        g "São tempos difíceis, mas não sinta dó de uma raça superior"

        show gatovaldo feliz

        g "Aquele idiota não parou para pensar que diminuir as rações felinas e incentivar o crescimento da população de roedores apenas faria com que nós passássemos a come-lôs mais ainda!"

        g "Muahahahahaha"
        jump prologom3

    label prologom3:

        show gatovaldo withale

        g "Bem, dito isso, conheçam tambem Alessandra Mallet."
        
        g "Talvez já tenham ouvido esse nome, uma grande estilista que entrou nas sombras um tempo atrás."

        g "Presumiram que ela tivesse morrido, mas aparentemente esqueceram de procurá-la no seu ateliê!"

        g "Acontece que minha tia-avó já fez morada no forro de lá"

        g "hoje ela está em um lugar melhor..."

        g "Em uma noite chuvosa e melancólica a nostalgia acabou me levando ao seu covil, e lá estava ela, desenhando uma roupa super estilosa como se nada tivesse acontecido"

        g "Falei com ela sobre o nosso movimento e ela aceitou participar, engraçado que não tenha questionado um gato falante e aceitado tudo numa boa, mas tudo bem!"

        menu:

            "Meus pesames pela sua tia-avó":
                jump prologoa5

            "Animais falantes não são normais hoje em dia?":
                jump prologob5

        label prologoa5:

            show gatovaldo default

            g "Mas ela não está morta!"

            g "Em nenhum momento disse isso, aliás, ela foi quem mais cuidou de mim depois daquele fatídico acontecimento que me tornou assim"

            g "Eu simplesmente aluguei uma cobertura para ela como agradecimento, é definitivamente um lugar melhor do que aquele forro."
            jump prologom4

        label prologob5:

            show gatovaldo serio

            g "Claro que não!"

            g "Aquele rato desgramento nem fala direito, o arrombadinho usa um sintetizador, poucos sabem da minha existência, até onde sabem ele foi o único afetado pelo experimento."
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

            g "\"Deus dá as suas tarefas mais árduas aos seus soldados mais bobinhos\"" 
            
            g "Eu, claramente, sou Deus e vocês são os meus soldados mais bobinhos, mas eu gosto de vocês, e confio em vocês, agora, se me permitem, preciso me esconder dentro de algum sofá."

            hide gatovaldo

            "* ele vira as costas e sai da sala, vocês dois se encaram confusos e se perguntam \"que diabos de ditado foi esse?\"*"

    # This ends the game.

    return