label lugar1k:
    n "Você vai até a planta carnívora"
    n "Ela parece uma planta carnívora normal"
    menu:
        "Pegar uma folha":
            n "Você pega uma folha da planta carnivora"
            n "Ela tenta te morder, parece que ela não ficou feliz com isso"
            $ adicionarItem("planta Carnivora")
            n "Dentro da boca dela parece ter algo"
            menu:
                "Tentar pegar":
                    n "Você pega rapidamente um papel dentro da boca da planta carnívora"
                    n "No papel tem um texto"
                    n "k4t4r1n4"
                    n "Você sente que isso pode ser importante"
                "Deixar ela em paz":
                    n "Você acha melhor não mexer mais com a planta"
        "Cutucar a planta":
            n "Você cutuca a planta carnívora"
            n "Ela morde seu dedo"
            n "Você não esperava ser mordido por uma planta"
            n "Dentro da boca dela parece ter algo"
            menu:
                "Tentar pegar":
                    n "Você pega rapidamente um papel dentro da boca da planta carnívora"
                    n "No papel tem um texto"
                    n "k4t4r1n4"
                    n "Você sente que isso pode ser importante"
                "Deixar ela em paz":
                    n "Você acha melhor não mexer mais com a planta"
        "Deixar de lado":
            n "Você sai de perto da planta carnívora"
    jump d1kat1inv
    
label lugar2k:
    n "Você vai até o tabuleiro de xadrez"
    n "Ao pegar ele percebe que na verdade a caixa não tem peças de xadrez dentro, mas mini garrafas de pinga"
    menu:
        "Beber uma":
            n "Ela tem um gosto estranho"
            n "Você se sente sendo julgado pela planta carnivora do outro lado da sala"
        "Pegar uma":
            n "Você pega uma das mini garragas de pinga e depois coloca o tabuleiro de xadrez de volta no lugar dele"
            $ adicionarItem("mini Pinga")
        "Deixar de lado":
            n "Você guarda a mini pinga de volta e coloca o tabuleiro no lugar"
    n "agora o jogador azul tem [inventarioAzul] e o jogador laranja tem [inventarioLaranja]"
            
    jump d1kat1inv

label lugar3k:
    n "Você encontra um palito de picolé"
    n "Examinando melhor o palito ele parece ter algo estranho"
    menu:
        "Investigar melhor":
            n "Investigando melhor você consegue ver um equipamento eletrônico no palito"
            n "Parece um rastreador"
            menu:
                "Deixar ele no mesmo lugar":
                    n "Você devolve ele para o lugar dele"
                "Levar ele com você":
                    $ adicionarItem("palito de Picole")
                    n "Você acha melhor levar ele com você"
        "Quebrar o palito":
            n "Você escuta uns sons de faíscas ao quebrar o palito"
            menu:
                "Jogar fora":
                    n "Você joga o palito quebrado no lixo"
                "Devolver para o mesmo lugar":
                    n "Você coloca o palito quebrado no mesmo lugar que encontrou ele"
                "Levar com você":
                    $ adicionarItem("palito Quebrado")
                    n "Você leva o palito quebrado com você"
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
            menu:
                "Deixar a carta na revista":
                    n "Você devolve a carta para dentro da revista"
                "Levar a carta com você":
                    $ adicionarItem("carta encontrada na Revista")
                    n "Você dobra a carta e a coloca no bolso"
    jump d1kat1inv

label lugar5k:
    n "Você investiga a garrafa de vodka"
    menu:
        "Beber a vodka":
            n "Você da um gole na vodka"
            n "A sensação é de que você bebeu fogo líquido"
            n "Você sente um pouco da sua sanidade morrer ali"
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
        "Ler o rótulo":
            n "O rótulo parece estar escrito em russo mas você não ter certeza"
            n "A única coisa que você consegue identificar é o símbolo de caveira típico de \"perigo\""
            n "Talvez isso não seja feito para o consumo humano"
            menu:
                "Colocar ela de volta":
                    n "Você acha que a Katarina pode dar pela falta da vodka dela e resolve coloca-la de volta no lugar"
                "Levar com você":
                    $ adicionarItem("garrafa de Vodka")
                    n "Você sente que pode precisar dessa garrafa mais tarde e resolve leva-la com você"
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
    n "Está escrito \"Ultra Mega Blaster Insanamente Ardido\""
    menu:
        "Provar":
            n "O sabor é extremamente ardido, você sente como se tivesse colocado um pedaço do inferno na sua boca"
            n "Não é apenas marketing"
            n "Você precisa urgentemente de leite para aliviar a queimação"
            n "Você gasta um tempo para se recuperar do dano causado pelo salgadinho"
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
        "Deixar de lado":
            n "Você acha melhor não comer isso."
        "Levar com você":
            $ adicionarItem("salgadinho Ardido")
            n "Apesar dela falar que adora o salgadinho, você acha melhor leva-lo com você"
    jump d1kat1inv