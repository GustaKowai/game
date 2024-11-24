#transicoes:

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset 20
    easeout .175 yoffset 0
    easein .175 yoffset 20
    easeout .175 yoffset 0
    yoffset 0


transform shake:
    pause .15
    xoffset 0
    easein .1 xoffset 5
    easeout .1 xoffset 0
    easein .1 xoffset 5
    easeout .1 xoffset 0
    easein .1 xoffset 5
    easeout .1 xoffset 0
    xoffset 0

#Efeito de luz de sirene
transform siren_tint:
    matrixcolor TintMatrix("f00")
    linear 2.0 matrixcolor TintMatrix("fff")
    linear 2.0 matrixcolor TintMatrix("f00")
    repeat

#Efeito Zoom

transform easeinzoom:
    center
    ease 0.7 zoom 1.5 yoffset 500

transform easeinzoom2:
    center
    ease 0.7 zoom 1.2 yoffset 200

transform dissolvezoom:
    center
    zoom 1.5 yoffset 500


transform easeoutzoom:
    center
    ease 0.7 zoom 1.0 yoffset 0


#Efeito de fumaça
transform smokespin:
    xpos 0.5
    ypos 0.5
    linear 5 rotate 360 # take 1 second to rotate 360 degrees
    rotate 0 # reset position counter
    repeat
image smoke = SnowBlossom(At("smoke.png", smokespin), count=1000, border = 200, yspeed=(-200, -5))

define gatodissolve = ImageDissolve("transicao.png", 2.0, ramplen=128, reverse=True) #Transição de gatinho
define morte = Fade(0.2,0,0,color="#fc0505")
define fadeA = Fade(0.2,0.2,0.2,color="#1338BE") #Trasição para o início do jogador azul
define fadeL = Fade(0.2,0.2,0.2,color="#f56300") #Trasição para o início do jogador laranja
define flashbulb = Fade(0.1, 0.0, 0.5, color="#fff")
define explosion = Fade(0.5, 0.5, 0.5, color="#fc0505")
define katanahit = Fade(0.1, 0.0, 0.5, color="#fc0505")