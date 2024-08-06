#######----Escolha de onde investigar -----################
default escolhido = []
default energiaAzul = 0
default energiaLaranja = 0
default itemInvestigado = ""
default inventarioLaranja = []
default inventarioAzul = []


#Cria a função que adiciona os itens nos respectivos inventários
init python:
    def adicionarItem(itemInvestigado):
        if jogador1:
            inventarioAzul.append(itemInvestigado)
        else:
            inventarioLaranja.append(itemInvestigado)
        itemInvestigado = ""

label investigacao:
    play music "abandoned.ogg" volume 2.0
    scene bg quartel
    with gatodissolve
    default energia = 4
    $ energia = 4
    if day1 == True and katDay1inv == True and aleDay1inv == True:
        n "Agora durante a noite vocês terão a chance de investigar um pouco mais sobre nossas novatas."
        n "Para isso vocês terão um sistema de Energia, que é mostrado na parte superior direita da tela"
        n "Cada ação feita consumirá um de energia, se a energia chegar a zero vocês não poderão mais investigar."
        n "A energia de cada jogador é medida separadamente, porém os itens que são coletados são armazenados em conjunto."
        n "A energia também é usada no Bar do Zé. Lá vocês poderão pedir mais informações sobre algo que encontraram de interessante."
        n "Lembrem-se de guardar um pouco de energia para conversar com o Zé, ele é uma pessoa difícil."
        n "Nos próximos dias eu não explicarei novamente, portanto espero que tenham entendido."
    
    $ JogadorAtivo = 0
    if jogador1:
        $ jogador1 = False
        show screen char_name_screen([nome2],[jogador1])
        show screen energy_screen([energia],[jogador1])
    else:
        $ jogador1 = True
        show screen char_name_screen([nome1],[jogador1])
        show screen energy_screen([energia],[jogador1])
    if katDay1inv or aleDay1inv:
        if jogador1:
            "E agora {color=#1338BE}[nome1]{/color}, para onde vamos?"
        else:
            "E agora {color=#F56300}[nome2]{/color}, para onde vamos?"
    menu:
        "Para o escritório da Katarina" if katDay1inv:
            jump d1kat1inv
        "Para o Ateliê da Alessandra" if aleDay1inv:
            jump d1ale1inv
    
    hide screen energy_screen
    jump barDoZe

    ##################---Investigações---######################

    ####################----Katarina----########################

    label d1kat1inv:
        $ katDay1inv = False
        scene bg escritorio

        if energia > 0:
            show screen energy_screen([energia],[jogador1])

            if jogador1:
                azul "Onde irei investigar?"
            else:
                laranja "Onde irei investigar?"

            menu:
                set escolhido
                "Planta Carnívora":
                    $ energia -= 1
                    jump lugar1k
                "Tabuleiro de xadrez" if (xadrez):
                    $ energia -= 1
                    jump lugar2k
                "Palito de picolé":
                    $ energia -= 1
                    jump lugar3k
                "Revista antiga":
                    $ energia -= 1
                    jump lugar4k
                "Garrafa de vodka" if (garrafa):
                    $ energia -= 1
                    jump lugar5k
                "Rifle de precisão":
                    $ energia -= 1
                    jump lugar6k
                "Salgadinho" if (salgadinho):
                    $ energia -= 1
                    jump lugar7k
                
                "Já vi o suficiente":
                    n "Você considera que já viu o suficiente"
                    $escolhido.remove("Já vi o suficiente")
                    if jogador1:
                        $ energiaAzul = energia
                    else:
                        $ energiaLaranja = energia

                    jump investigacao


        n "A investigação de hoje termina por aqui"
        jump investigacao

    label lugar1k:
        n "Você vai até a planta carnívora"
        n "Ela parece uma planta carnívora normal"
        jump d1kat1inv
    
    label lugar2k:
        n "Você vai até o tabuleiro de xadrez"
        n "Ao pegar ele percebe que na verdade a caixa não tem peças de xadrez dentro, mas mini garrafas de pinga"
        menu:
            "Beber uma":
                n "Ela tem um gosto estranho"
                n "Você se sente sendo julgado pela planta carnivora do outro lado da sala"
            "Deixar de lado":
                n "Você pega uma das mini garragas de pinga e depois coloca o tabuleiro de xadrez de volta no lugar dele"
                $ adicionarItem("miniPinga")
        n "agora o jogador azul tem [inventarioAzul] e o jogador laranja tem [inventarioLaranja]"
                
        jump d1kat1inv
    
    label lugar3k:
        n "Você encontra um palito de picolé"
        n "Examinando melhor o palito ele parece ter algo estranho"
        menu:
            "Investigar melhor":
                n "Investigando melhor você consegue ver um equipamento eletrônico no palito"
                n "Parece um rastreador"
            "Quebrar o palito":
                n "Você escuta uns sons de faíscas ao quebrar o palito"
        jump d1kat1inv
    
    label lugar4k:
        n "Você pega a revista"
        n "Ela parece bem antiga"
        n "Na capa aparece uma garota jovem de cabelos ruivos e seu pai, ambos parecem felizes"
        n "Ao folhear a revista encontra a matéria falando sobre eles"
        menu:
            "Ler a matéria":
                pag "O ramo de ração de gatos tem se mostrando incrivelmente lucrativo!"
                pag "A empresa VSF de ração de gatos decolou"
                pag "As ações apenas crescem"
                pag "A filha do dono parece feliz rodeada de gatinhos"
                nvl clear
                n "O resto da matéria é de opiniões das pessoas sobre a qualidade da ração"
            "Continuar folheando a revista":
                n "Uma carta cai de dentro"
                n "Ela está escrita com uma letra estranha e ela está com uma parte faltando"
                pag "Sim, eu sei quem matou ele"
                pag "A escolha é sua de acreditar em mim ou não"
                pag "Podemos nos encontrar no..."
                nvl clear
                n "A partir dai o resto da carta parece ter sido destruida"
        jump d1kat1inv
    
    label lugar5k:
        n "Você investiga a garrafa de vodka"
        menu:
            "Beber a vodka":
                n "Você da um gole na vodka"
                n "A sensação é de que você bebeu fogo líquido"
                n "Você sente um pouco da sua sanidade morrer ali"
            "Ler o rótulo":
                n "O rótulo parece estar escrito em russo mas você não ter certeza"
                n "A única coisa que você consegue identificar é o símbolo de caveira típico de \"perigo\""
                n "Talvez isso não seja feito para o consumo humano"
        jump d1kat1inv
    
    label lugar6k:
        n "Você investiga Rifle de precisão"
        n "Ele parece ter sido bem usado"
        n "Apesar disso ele está em um ótimo estado, a Katarina deve fazer manutenção frequente nele"
        if rifle:
            n "Você sente que ele ainda está com um pouco de areia da missão de hoje"

        jump d1kat1inv
    
    label lugar7k:
        n "Você investiga o pacote de salgadinho"
        n "Está escrito \"Aqui diz Ultra Mega Blaster Insanamente Ardido\""
        menu:
            "Provar":
                n "O sabor é extremamente ardido, você sente como se tivesse colocado um pedaço do inferno na sua boca"
                n "Não é apenas marketing"
                n "Você precisa urgentemente de leite para aliviar a queimação"
                n "Você gasta um tempo para se recuperar do dano causado pelo salgadinho"
                $ energia -= 1
            "Deixar de lado":
                n "Você acha melhor não comer isso."

    ################----Alessandra----#######################

    label d1ale1inv:
        $ aleDay1inv = False
        scene bg atelie

        if energia > 0:
            show screen energy_screen([energia],[jogador1])

            if jogador1:
                azul "Onde irei investigar?"
            else:
                laranja "Onde irei investigar?"

            menu:
                set escolhido
                "Carta":
                    $ energia -= 1
                    jump lugar1a
                "Vestido Tie-Dye" if (vestidotiedye):
                    $ energia -= 1
                    jump lugar2a
                "Coleção de CDs do Slipknot":
                    $ energia -= 1
                    jump lugar3a
                "Capacete de moto":
                    $ energia -= 1
                    jump lugar4a
                "Vestido rosa" if (vestidorosa):
                    $ energia -= 1
                    jump lugar5a
                "Um tofu" if (tofu):
                    $ energia -= 1
                    jump lugar6a
                "Já vi o suficiente":
                    n "Você considera que já viu o suficiente"
                    if jogador1:
                        $ energiaAzul = energia
                    else:
                        $ energiaLaranja = energia

                    jump investigacao


        n "A investigação de hoje termina por aqui"
        jump investigacao

    label lugar1a:
        n "Você encontra uma carta em cima de uma mesa no Atelie"
        n "A primeira vista parece só uma carta de alguém fazendo uma encomenda de roupa com a Alessandra"
        menu:
            "Ler com mais atenção":
                n "Você lê com mais atenção e percebe que provavelmente tem um código escondido na carta"
                n "O código parece marcar um local de encontro"
                n "Você não consegue identificar o local"
            "Alterar as medidas descritas na carta":
                n "Você altera as medidas do vestido descritas na carta"
                n "Você se sente super badass depois de fazer isso"
        jump d1ale1inv
    
    label lugar2a:
        n "Você vê um vestido Tie-Dye"
        n "Ao se aproximar percebe que ele tem exatamente as suas medidas"
        n "Parece que foi feito para você"
        menu:
            "Provar":
                n "Você experimenta o vestido"
                n "Você se sente super na moda"
            "Deixar de lado":
                n "Você coloca o vestido de volta no cabide"
                n "Um arrepio sobe a sua espinha ao se imaginar usando aquilo"
        jump d1ale1inv
    
    label lugar3a:
        n "Você encontra uma coleção de CDs do Slipknot"
        menu:
            "Olhar dentro das caixas de cds":
                n "Ao abrir a caixa percebe que dentro tem um cd dos barões da pisadinha"
                n "Ela provavalmente trocou as capas para não deixar óbvio o gosto musical dela"
            "Dar play no radio ao lado":
                n "O rádio começa a tocar calcinha preta"
                n "Você se lembra que está em uma missão secreta e desliga o rádio rapidamente"
        jump d1ale1inv
    
    label lugar4a:
        n "Você Vai até o capacete de moto"
        n "Você não imaginava que a Alessandra andasse de moto"
        n "Logo ao lado tem outro capacete parecido"
        n "Será que ela tem algum amigo que anda de moto com ela?"
        menu:
            "Examinar o capacete":
                n "Olhando nos capacetes você percebe que tem nomes escritos neles"
                n "Em um deles está escrito o nome da Alessandra"
                n "No outro está escrito \"Danran\""
                n "Ela aparenta ter um senso de humor bem duvidoso"
            "Deixar de lado":
                n "Você coloca o capacete de lado"
                n "Perto do capacete você encontra um papel"
                pag "Não se esqueça do nosso encontro"
                nvl clear
                n "A mensagem é impressa então não é possível identificar a letra da pessoa"
                
        jump d1ale1inv
    
    label lugar5a:
        n "Você investiga o vestido rosa"
        n "Ele não parece ter as medidas da Alessandra"
        menu:
            "Procurar nos bolsos":
                n "Você procura nos bolsos do vestido"
                n "Dentro deles tem um papel amassado com o endereço de um restaurante chique"
                n "\"Não se esqueça de trazer o bagulho\""
                n "O papel está assinado pela Alessandra"
            "Experimentar o vestido":
                n "O vestido não tem um bom caimento"
                n "Ele aperta em alguns locais e fica largo em outros"
                n "Você tira o vestido rosa e se sente muito melhor"
        jump d1ale1inv
    
    label lugar6a:
        n "Você vê um tofu embrulhado para viagem"
        menu:
            "Comer o tofu":
                n "Você come o tofu"
                achieve Comer_tofu
                n "Tem sabor de tofu"
                n "Por algum motivo você sente que pode ter cometido um crime"
            "Deixar o tofu de lado":
                n "Você se pergunta onde deveria guardar o tofu:"
                menu:
                    "Colocar de volta no mesmo lugar":
                        n "Você coloca o tofu de volta onde ele estava"
                    "Guardar na geladeira":
                        n "Você embrulha o tofu de volta e o leva até uma geladeira"
                        n "Você se questiona por um momento o por que tem uma geladeira em um atelie"
                        n "Dentro da geladeira você encontra diversas embalagens fechadas e sem identificação"
                        menu:
                            "Olhar as embalagens":
                                n "Você tenta identificar as embalagens"
                                n "A geladeira começa a apitar por conta da porta aberta"
                                n "Você acha melhor fechar ela antes de ser descoberto"
                            "Deixar de lado":
                                n "Você guarda o tofu na geladeira"
        jump d1ale1inv