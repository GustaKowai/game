# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pag = Character(' ', kind=nvl, color="#c8c8ff")
define e = Character("Eileen", what_prefix='"', what_suffix='"')
define g = Character("Gatovaldo", image="gatovaldo", callback = low_beep, what_prefix='"', what_suffix='"')
define n = Character("", callback = low_beep, what_prefix='{i}', what_suffix='{/i}')
define c = Character("Claudia", image="claudia", callback = beep_2, what_prefix='"', what_suffix='"')
define vo = Character("Vovô sorveteiro", image="vovo", callback = low_beep, what_prefix='"', what_suffix='"')
define gar = Character("Garçom", image="garcom", callback = low_beep, what_prefix='"', what_suffix='"')
define traf = Character("Traficante", image="traficante", callback = low_beep, what_prefix='"', what_suffix='"')
define ate = Character("Atendente", image="atendente", callback = low_beep, what_prefix='"', what_suffix='"')
define rdj = Character("Robert Downey Jr.", image="rdj", callback = low_beep, what_prefix='"', what_suffix='"')
define padre = Character("Padre", image="padre", callback = low_beep, what_prefix='"', what_suffix='"')
define urso = Character("Urso", image="urso", callback = low_beep)
define z = Character("Zé", image = "Ze", callback = beep_5, what_prefix='"', what_suffix='"')
#Define as conquistáveis e suas respectivas confianças nos jogadores azul e laranja
define character.k = Character("Katarina Kabrera", image="katarina", callback = beep_3, what_prefix='"', what_suffix='"')
default k.azul = 0
default k.laranja = 0
define character.a = Character("Alessandra Mallet", image="alessandra", callback = low_beep, what_prefix='"', what_suffix='"')
default a.azul = 0
default a.laranja = 0