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
        menu:
          "Tirar ele":
            n "Apesar disso você acha melhor devolver ele para o local apropriado"
          "Continuar vestindo":
              n "Você decide continuar vestido o vestido tie-dye"
              $ adicionarItem("VestidoTieDye")
              $ usandoeVestido = True
          "Levar com você":
              $ adicionarItem("vestidoTieDye")
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
    jump d1ale1inv