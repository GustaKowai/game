label barDoZe:
    $ aleDayinv = True
    $ katDayinv = True
    play music "audio/cassino.wav"  volume 2.0
    define inventarioAtual = []
    if jogador1:
        show screen char_name_screen([nome1],[jogador1])
        $ inventarioAtual = inventarioAzul
        $ energia = energiaAzul
        show screen energy_screen([energia],[jogador1])
    else:
        show screen char_name_screen([nome2],[jogador1])
        $ inventarioAtual = inventarioLaranja
        $ energia = energiaLaranja
        show screen energy_screen([energia],[jogador1])

    scene bg bar
    show ze default
    if jogador1:
        with fadeA
    else:
        with fadeL

label conversaBar:
    if energia > 0:
        show screen energy_screen([energia],[jogador1])
        jump zeAjuda
    else:
        z "Hum..."
        z "Você parece esgotado. Beba um drink e vá para casa."
        jump fimdobar
        
##É aqui que vão as opções para a escolha
label zeAjuda:
    z "Pois bem, o que pretende me mostrar hoje?"
    menu:
        "Mostrar a folha da planta carnívora" if "planta Carnivora" in inventarioAtual:
            $ inventarioAtual.remove("planta Carnivora")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barplantacarnivora
        "Mostrar a mini pinga" if "mini Pinga" in inventarioAtual:
            $ inventarioAtual.remove("mini Pinga")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barminipinga
        "Mostrar o palito de picolé" if "palito de Picole" in inventarioAtual:
            $ inventarioAtual.remove("palito de Picole")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barpalito
        "Mostrar o palito de picolé quebrado" if "palito Quebrado" in inventarioAtual:
            $ inventarioAtual.remove("palito Quebrado")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barpalitoquebrado
        "Mostrar a carta encontrada na Revista" if "carta encontrada na Revista" in inventarioAtual:
            $ inventarioAtual.remove("carta encontrada na Revista")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barcartarevista
        "Mostrar a garrafa de vodka" if "garrafa de Vodka" in inventarioAtual:
            $ inventarioAtual.remove("garrafa de Vodka")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barvodka
        "Mostrar o salgadinho" if "salgadinho Ardido" in inventarioAtual:
            $ inventarioAtual.remove("salgadinho Ardido")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barsalgadinho
        "Mostrar o Vestido Tie-Dye" if "Vestido Tie-Dye" in inventarioAtual:
            $ inventarioAtual.remove("Vestido Tie-Dye")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump bartiedye
        "Mostrar a chave gótica" if "chave gótica" in inventarioAtual:
            $ inventarioAtual.remove("chave gótica")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barchave
        "Mostrar o papel Amassado" if "papel Amassado" in inventarioAtual:
            $ inventarioAtual.remove("papel Amassado")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barpapelamassado
        "Mostrar o lenço" if "lenço" in inventarioAtual:
            $ inventarioAtual.remove("lenço")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barlenco
        "Mostrar a nota fiscal" if "nota Fiscal" in inventarioAtual:
            $ inventarioAtual.remove("nota Fiscal")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump barnotafiscal
        "Mostrar o tofu" if "tofu" in inventarioAtual:
            $ inventarioAtual.remove("tofu")
            $ energia -= 1
            show screen energy_screen([energia],[jogador1])
            jump bartofu
        
        "Na verdade nada, só quero ir dormir.":
            if energia > 0:
                z "Tem certeza? Você ainda me parece ter energia."
                menu:
                    "sim":
                        z "Okay então, bom descanço."
                        jump fimdobar
                    "Não, acho que quero te mostrar mais algumas coisas.":
                        z "Então não me faça perder tempo por favor."
                        jump conversaBar

label fimdobar:
    if jogador1:
        $ inventarioAzul = inventarioAtual
    else:
        $ inventarioLaranja = inventarioAtual
    n "Você vai para a casa descansar"
    scene bg bar
    show ze default
    if trocaJogadorBar:
        $ trocaJogadorBar = False
        hide screen energy_screen
        jump changeDay
    $ trocaJogadorBar = True
    jump trocaPersonagem


label trocaPersonagem:
    if jogador1:
        $ jogador1 = False
    else:
        $ jogador1 = True
    jump barDoZe

###Conversas sobre os itens:
## Itens da Katarina:
label barplantacarnivora:
    z "Hum, vejo que trouxe... Uma folha?"
    z "Ok, não parece uma folha comum, vou dar uma examinada melhor."
    n "Ele tira debaixo do balcão um livro enorme  de botânica"
    n "Ele passa as folhas de maneira bem rápida, até encontrar uma folha que coincide"
    z "Essa folha é de uma espécime de planta carnívora extremamente rara"
    z "Acreditávamos que ela estava extinta..."
    z "Não sei onde conseguiu isso, mas alguém com certeza cuida muito bem dessa planta"
    z "A pessoa deve ter um apresso muito grande por ela."
    jump conversaBar


label barminipinga:
    z "To vendo que vc trouxe uma mini Pinga!"
    z "Essa é das boas. Parece feita de planta carnívora."
    z "Onde arranjou? Faz tempo que não vejo uma assim..."
    z "Analisando melhor o rótulo, parece de fabricação caseira."
    z "Mas é uma receita de família, da para ver pela assinatura."
    z "Só o cheiro disso aqui é capaz de desmaiar um elefante. Tem mais álcool aqui do que no negócio que a gente ta usando para lavar as mãos."
    z "Ela é boa. Com certeza foi feita por alguém habilidoso."
    $ minipingabar = True
    if salgadinhonobar and vodkanobar:
        achieve estoque_bar
    jump conversaBar

label barpalito:
    z "Um palito de picolé?"
    z "Por que você me trouxe isso? Está premiado?"
    n "Ele olha melhor para o palito"
    z "Ahh... Então parece que temos algo aqui..."
    n "Ele tira uma maleta de ferramentas de baixo do balcão"
    n "Ele abre a maleta e tira diversas ferramentas de precisão e começa a analisar o palito"
    z "Hum... Isso parece um rastreador."
    z "Mas acho que isso você já sabia. Fazendo a análise de transmissão é possível detectar quem está rastreando vocês."
    z "..."
    z "Isso é um rastreador do governo. Onde conseguiu isso? Alguém do governo sabe exatamente onde você está agora."
    z "Pode deixar isso aqui comigo, vou dar um jeito deles acharem que você está bem longe..."
    jump conversaBar

label barpalitoquebrado:
    z "Um palito de picolé... quebrado?"
    z "Você quer que eu jogue isso no lixo?"
    n "Faíscas pulam do palito"
    z "Ah, parece que temos algo aqui..."
    n "Ele olha de perto"
    z "Parece um rastreador"
    z "Da forma que está eu não consigo identificar quem estava rastreando você..."
    z "Cuidado com quem te deu isso."
    jump conversaBar

label barcartarevista:
    n "Ele pega a carta e a lê"
    z "O conteúdo dessa carta é bem preocupante..."
    $ cartaLida = True
    if papelLido:
        z "A letra disso me parece familiar... Eu lembro de ter visto algo parecido em algum lugar..."
        z "É uma letra bem diferente mas não posso dar certeza."
    else:
        z "É uma letra bem estranha. Parece que a pessoa se esforçou para que não reconhecessem a letra dela"
        z "Ou apenas tem uma letra muito feia"
    z "O papel também não parece muito antigo. Deve ter sido escrita há pouco tempo."
    jump conversaBar
    

label barvodka:
    n "Ele pega a garrafa da sua mão"
    z "Essa nós não temos aqui"
    z "Na verdade, acho que isso é inclusive ilegal."
    z "Mas eu não falo russo..."
    n "Ele coloca a mão embaixo do balcão, procurando por algo"
    z "Droga, eu esqueci que emprestei meu dicionário de russo..."
    n "Ele liga para alguém em video-chamada com o celular dele"
    z "Alô? Você pode traduzir umas paradas para mim?"
    n "Não seria mais fácil usar o tradutor do celular?"
    z "Hum, ok... Entendi..."
    z "Obrigado."
    n "Ele desliga o celular"
    z "Essa garrafa tem uma vodka super rara, extremamente forte."
    z "É praticamente uma bomba."
    z "Duvido que alguém conseguiria beber isso tranquilamente"
    z "Esse tipo de álcool hoje em dia é usado para fazer bombas."
    z "Pode ser útil para nós."
    z "Vou ficar com isso por questões de segurança..."
    $ vodkanobar = True
    if salgadinhonobar and minipingabar:
        achieve estoque_bar
    jump conversaBar

label barsalgadinho:
    z "Isso é o salgadinho Ultra Mega Blaster Insanamente Ardido?!"
    z "Fazem anos que eu não via um desses, era um sucesso de vendas!"
    z "Ah, está vencido há dois anos..."
    z "Será que a fiscalização se importaria?"
    z "Isso aqui era uma raridade, é sabor queijo picante."
    z "Foi descontinuado desde que aquele rato tomou controle"
    z "Ele disse que era um desperdício de queijo fazer um salgadinho que quase ninguém aguentaria comer"
    z "Maldito..."
    z "Apesar disso, alguns ratos ainda são fanáticos por isso."
    z "Vou guardar isso comigo, você não vai querer ser pego pela fiscalização carregando algo do tipo."
    $ salgadinhonobar = True
    if vodkanobar and minipingabar:
        achieve estoque_bar
    jump conversaBar

##Itens da alessandra:

label bartiedye:
    if usandoVestido:
        z "Que \"belo\" vestido você está usando."
        z "Parece que ele foi feito para você..."
        z "Literalmente parece que ele foi feito para você, ele está com suas medidas EXATAS"
        z "Você deve ter tido trabalho tirando todas essas medidas..."
        z "Fica bem em você. Foi feito por uma pessoa habilidosa."
        z "Talvez tenha sido feito para alguma ocasião especial?"
    else:
        z "Não imaginei que traria um vestido para mim."
        z "Não acho que serviria em mim... Também não faz muito o meu estilo."
        z "Apesar disso, ele é bem feito. A pessoa que costurou isso é muito boa."
        z "Olhando na etiqueta, parece ser parte de uma coleção específica..."
        z "Mas não consigo identificar direito, parece que foi rasgada"
        z "Ve..."
        z "Algo do tipo."
    jump conversaBar

label barchave:
    z "Uma chave?"
    z "Bem, ela é bem diferente... Acho que seria interessante você guardar ela com você."
    z "Ela pode ser importante no futuro."
    jump conversaBar

label barpapelamassado:
    n "Ele pega o papel amassado e lê"
    z "\"Ajeite essa coluna\""
    z "Está querendo dizer algo para mim?"
    z "..."
    n "O clima fica um pouco pesado entre vocês"
    n "Você percebe que ele tenta ajeitar um pouco mais a ja excelente postura dele"
    n "Pela sua cara ele percebe que talvez tenha entendido algo errado."
    z "Ah, você encontrou isso?"
    $ papelLido = True
    if cartaLida:
        z "A letra disso me parece familiar... Eu lembro de ter visto algo parecido em algum lugar..."
        z "É uma letra bem diferente mas não posso dar certeza."
    else:
        z "É uma letra bem estranha. Parece que a pessoa se esforçou para que não reconhecessem a letra dela"
        z "Ou apenas tem uma letra muito feia"
    z "O papel está bem amassado, parece que foi escrito com pressa."
    jump conversaBar

label barlenco:
    n "Ele pega o lenço da sua mão"
    z "Esse negócio... Ta usado, não ta não?"
    z "Que tal lavar ele?"
    z "Espera... Tem uma assinatura aqui"
    z "Isso é um autógrafo... De alguém chamado Taylor Swift?"
    z "Não conheço, mas você deve gostar bastante para guardar um lenço usado assim..."
    jump conversaBar

label barnotafiscal:
    z "Hum... Isso é uma nota fiscar do Ardórsia"
    z "Você deve estar nadando em dinheiro se foi comer lá."
    z "Deveria jantar aqui, é bem mais barato."
    z "Quero dizer, olha o preço disso! Daria para comprar um carro com o quanto gastou nessa noite..."
    z "Talvez dois, se não fizer questão de ar condicionado..."
    n "Ele fica pensativo por um tempo, como se estivesse calculando exatamente quantos adicionais poderia colocar em cada carro com o valor da conta"
    z "Na verdade... Parece que não foi você que pagou né?"
    z "Tem uma gorgeta adicionada paga em dinheiro pela Alessandra, mas a conta mesmo parece que foi paga por outra pessoa"
    jump conversaBar

label bartofu:
    z "Um tofu?"
    z "Isso daqui... Você não quer que eu sirva isso no meu bar, quer?"
    z "As pessoas daqui não aceitariam isso. Isso aqui não é nem carne nem queijo"
    z "Dizem que comidas só podem ser realmente saudáveis se alguém morreu para produzir ela."
    z "O que pretende fazer com isso?"
    menu:
        "Eu vou comer.":
            n "Você come o tofu antes que ele possa falar qualquer coisa"
            achieve Comer_tofu
            z "Er..."
            z "Na verdade, eu sei o por que você trouxe esse tofu."
            z "Estou ciente da missão da arma de tofu."
            n "Um silêncio se firma entre vocês"
            n "Vocês concordam com o olhar de nunca mais falar sobre isso"
        "Na verdade... Isso não é exatamente um tofu":
            n "Você explica para ele sobre a arma tofuzadora"
            z "Ah sim, eu sei. Estava só tirando uma com a sua cara."
            z "Estou ciente da missão."
            z "Se você quer transformar ele de volta em gente..."
            z "Talvez tenha algo que eu possa fazer."
            z "Mas não tenho certeza, como ele estava no raio de 15 metros provavelmente não se lembrará quem é"
            z "Lembra? Todo mundo esquece dele, inclusive ele."
            n "Zé leva o tofu para uma geladeira nos fundos enquanto murmura algo para si mesmo"
            z "....Será que tofus tem memória?...."
    jump conversaBar


