style char_name1_style:
    ypos 50
    color "#1338BE"

style char_name2_style:
    ypos 50
    color "#f56300"

screen char_name_screen(message, jogador, okay=Return(True), cancel=Return(False)):
    if jogador1:
        #add "jogador1.jpg"
        vbox:
            style "char_name1_style"
            xalign 0.05
            text "Jogador: [message]" 
    else:
        #add "jogador2.jpg"
        vbox:
            style "char_name2_style"
            xalign 0.05
            text "Jogador: [message]"