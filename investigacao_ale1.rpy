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
        $ medidasAlteradas = True
  jump d1ale1inv

label lugar2a:
    n "Você vê um vestido Tie-Dye"
    n "Ao se aproximar percebe que ele tem exatamente as suas medidas"
    n "Parece que foi feito para você"
    menu:
      "Provar":
        n "Você experimenta o vestido"
        n "Você se sente super na moda"
        menu:
          "Tirar ele":
            n "Apesar disso você acha melhor devolver ele para o local apropriado"
          "Continuar vestindo":
              n "Você decide continuar vestido o vestido tie-dye"
              $ adicionarItem("Vestido Tie-Dye")
              $ usandoVestido = True
          "Levar com você":
              $ adicionarItem("vestido Tie-Dye")
              n "Você decide levar o vestido com você"
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
        n "Ao olhar na outra caixa de CDs você encontra uma chave com um estilo gótico"
        menu:
          "Pegar a chave":
            $ adicionarItem("chave gótica")
            $ chavegotica = True
            play sound "item importante adquirido.mp3"
            n "Você guarda a chave com você"
          "Deixar a chave ali":
            n "Você acha melhor deixar a chave ali"
      "Dar play no radio ao lado":
        n "O rádio começa a tocar calcinha preta"
        n "Você se lembra que está em uma missão secreta e desliga o rádio rapidamente"
        n "Você resolve pegar uma caixa de cds para guardar o cd que estava no rádio"
        n "Ao abrir a caixa de CDs você encontra uma chave com um estilo gótico"
        menu:
          "Pegar a chave":
            $ adicionarItem("chave gótica")
            $ chavegotica = True
            play sound "item importante adquirido.mp3"
            n "Você guarda a chave com você"
          "Deixar a chave ali":
            n "Você acha melhor deixar a chave ali"
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

label lugar99a:
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

label lugar5a:
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
      "Levar o tofu com você":
        n "Você pega o tofu embrulhado para a viagem e guarda com você."
        n "Você não tem certeza se isso conta como roubo ou sequestro."
        $ adicionarItem("tofu")
    jump d1ale1inv

label lugar6a:
    n "Você se aproxima da nota fiscal."
    n "Ao observar ela melhor, percebe que é a nota fiscal do restaurante"
    n "Ela contém os itens pedidos no restaurante Ardórsia"
    menu:
        "Levar com você":
            n "Você coloca a nota fiscal no bolso"
            $ adicionarItem("nota Fiscal")
        "Observar os valores":
            n "Você olha os valores gastos no restaurante"
            n "O preço tem muitos mais zeros do que você esperava"
            n "Trabalhar com moda deve realmente pagar muito bem"
    jump d1ale1inv

label lugar7a:
    n "Você encontra um papel amassado em um canto do ateliê"
    n "Você se aproxima dele"
    menu:
      "Jogar ele no lixo":
        n "Você resolve ajudar na limpeza do ateliê e joga ele no lixo"
      "Abrir e ler":
        n "está escrito: \"Ajeite essa coluna\""
        menu:
          "Jogar no lixo":
            n "Você apenas joga ele no lixo"
          "Guardar com você":
            n "Você guarda ele no bolso"
            $ adicionarItem("papel Amassado")
    jump d1ale1inv

label lugar8a:
  n "Você encontra um lenço jogado em cima de uma mesa"
  n "Ele parece estar usado"
  n "Não parece que a Alessandra tem a intenção de lava-lo tão cedo"
  n "Olhando bem você consegue ver que tem um autógrafo da Taylor Swift nele"
  menu:
    "Guardar ele com você":
      n "Você decide levar ele com você"
      n "Por motivos puramente profissionais"
      $ adicionarItem("lenço")
    "Deixar ele em cima da mesa":
      n "Você decide não mexer muito nele"
      n "Talvez ela esteja guardando ele assim por algum motivo"
  jump d1ale1inv
      