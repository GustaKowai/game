style char_name1_style:
    ypos 10
    color "#1338BE"

style char_name2_style:
    ypos 10
    color "#f56300"

screen char_name_screen(message, jogador, okay=Return(True), cancel=Return(False)):
    if jogador1:
        add "jogador1.png"
        vbox:
            style "char_name1_style"
            xalign 0.04
            text "Jogador: [message]" 
    else:
        add "jogador2.png"
        vbox:
            style "char_name2_style"
            xalign 0.04
            text "Jogador: [message]"