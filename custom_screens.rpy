style char_name1_style:
    ypos 10
    color "#1338BE"

style char_name2_style:
    ypos 10
    color "#f56300"

screen char_name_screen(message, jogador, okay=Return(True), cancel=Return(False)):
    if jogador1:
        #add "jogador1.png"
        vbox:
            style "char_name1_style"
            xalign 0.04
            text "{color=#1338BE}Jogador: [message]{/color}" 
    else:
        #add "jogador2.png"
        vbox:
            style "char_name2_style"
            xalign 0.04
            text "{color=#f56300}Jogador: [message]{/color}"

screen energy_screen(message, jogador, okay=Return(True), cancel=Return(False)):
    if jogador1:
        vbox:
            style "char_name1_style"
            xpos 1500
            text "{color=#1338BE}Energia: [message]{/color}"
    else:
        vbox:
            style "char_name2_style"
            xpos 1500
            text "{color=#f56300}Energia: [message]{/color}"