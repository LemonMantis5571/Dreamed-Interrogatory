# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Meifeng = Character("Meifeng", color="#FFD700")
define Arroliga = Character("Arroliga", color = "#ADD8E6")
define Yienesi = Character("Yienesi", color = "#ff007f")
define Unknown = Character("???", color="#FFD700")
define Guayaba = Character("Guayaba", color="#ff0066")
default retorno = 0
default email = 0
default emaildone = 0

image background_yenesi = Movie(size=(1920,1080), channel ="movie", play="images/backgroundyenesi.ogv", loop = True)
# The game starts here.

label start:
    play music "audio/bgm_pyrite.mp3" fadein 1.0 volume 0.3
    scene bg chele

    Meifeng "*Aparece Epicamente*"
    show meifeng at left
    Meifeng "Hola soy Meifeng!"
    Meifeng "Esta es una novela visual de prueba, donde se desarrollara una anecdota en cuanto a la perspectiva que tengo como autor"
    Meifeng "Los que son cercanos al protagonista se daran cuenta de cosas que no sabian y algunos no concordaran con lo mostrado aqui."
    Meifeng "...xD"
    Meifeng "La historia se altero en algunas partes para proteger la privacidad de los protagonistas."
    hide meifeng
    jump inicio

#capitulo 1
label inicio:
     "*En esta historia protagonizaras a \"Arroliga\"* "
menu:
     "El C plo":
       jump opcion_uno_a

     "Chatel Prix":
       jump opcion_uno_b

#menu 1

label opcion_uno_a:
    "El c pajer"
    "Bueno empezemos"
    jump chapter_one

label opcion_uno_b:
    "Quien le dio droga a la llama?"
    "Comenzemos..."
    jump chapter_one

label chapter_one:

    #Cuarto de Arroliga
  scene bg chante
  Arroliga "BUahhh, que dia de mierda como todos...colegio mas hijueputa."
  Arroliga "Realmente solo voy por ella."
  show rroliga at right
  Arroliga "ZzZ...toca supongo."
  "*Se toma una ducha y se dirige disque a desayunar* (Nunca lo hace)"
    #Se dirige a tomar una ducha
  scene bg toilet03
  show rroliga shower at left
  Arroliga "Lo peor de ir a clases es esperar esa ruta de mierda!"
  show rroliga angrys at left
  Arroliga "Esa 112 solo pasa cuando le da la gana."
  show rroliga shower at left
  Arroliga "Bah, no me estresare mas... vere que hay de hartarse."

  #Va a tomar su desayuno
  scene bg chele
  show rroliga uniforme at left
  "*Come*"
  show rroliga uniform at left
  Arroliga "Que porqueria...mejor me tiro un lol y no voy a ese colegio cerote."
  Arroliga "Aunque..."
  show rroliga uniformb at left
  Arroliga "Realmente me da ansias saber como vestira hoy..."
  show yienesinude at right
  Arroliga "...hhm"
  Arroliga "ASasdjaksdja"
  hide yienesinude
  Arroliga "Calmate Jose, que estas pensando?..."
  show rroliga uniform at left
  Arroliga "..."

  # scena de la calle
  "*Va directo a la parada*"
  scene bg street
  show rroliga uniform at left

  Arroliga "...?"

  show rroliga uniforma at left

  Arroliga "Que mierda?, pero si son las 6:50."
  Arroliga "Me da tiempo de hasta culearme un perro!, voy demasiado temprano. -.-"

  show rroliga uniformtired

  Arroliga "Bah."
  Arroliga "Segun mis calculos llegare a las 7:40."
  Arroliga "Y me comere algo antes de que termine la primera hora."
  "-Nota del Autor: Las clases empezaban a las 7:00 AM, pero este loco siempre llegaba 1 hora tarde o a veces ni llegaba."
  Arroliga "Definitivamente, estoy pasadito..."

  Arroliga "..."
  Arroliga "...."
  Arroliga "....."

  Arroliga "Como que la ruta ya nunca aparecio..."

  show rroliga uniforma at left

  Arroliga "Que puta mierda!"
  "Que hacer?"
  #menu 2
  menu:
        "Seguir esperando la ruta":
            show rroliga uniformtired at left
            Arroliga "Supongo que puedo esperar un poco mas, no tengo prisa la verdad."
            jump chapter_one_school

        "Volver a casa":
            Arroliga "Me voy al chante, su madre."
            jump chapter_one_school


label chapter_one_school:
     "*Escuchas pasos*"
     show rroliga uniformsur at left
     Arroliga "Huh?"
     stop music fadeout 1.0
     Unknown "..."
     play music "audio/bgm_unknown_ost.mp3" fadein 0.0 volume 0.2
     pause 1.0
     show unknown at right
     Unknown "Tan culito y sin turca"
     Unknown "Tarde como siempre eh?"
     show rroliga uniforma at left
     Arroliga "Y en que posicion estas de decirlo?, ."
     show unknown surprised
     Unknown "xD"
     Unknown "Vamonos a pie, vas a llegar mas tarde si seguis esperando esa ruta, el chofer se tiro carrera desde el zumen con la 210 y ambos mataron como a 3 personas ._. xD"
     "-Si, casi siempre pasaba eso."
     Arroliga "Supongo que no queda de otra..."
     scene bg black
     "*Caminas durante 20 minutos hasta que llegan al zumen*"
     stop music fadeout 1.0
     scene bg zumen
     play music "audio/bgm_zumen.mp3" fadein 1.0 volume 0.3
     show unknown surprised at right
     Unknown "Va, hueles eso?, es el olor a mierda de Altagracia, ya estamos cerca"
     show rroliga uniform
     Arroliga "No me sorprenderia que por respirar obtuvieramos una enfermedad veneria aqui."
     jump chapter_one_school_zumen

label chapter_one_school_zumen:
     #zumen
     scene bg black
     "*Has llegado al zumen*"


label chapter_one_school_zumen_options:
     stop music fadeout 1.0
     play music "audio/bgm_zumen.mp3" fadein 1.0 volume 0.3
     scene bg zumencity
     "Que hacer ahora?"
     menu:
         "Ir al colegio":
                $ retorno += 1
                jump chapter_one_school_entry

         "Regresar a casa":
            if retorno <1:
                play music "audio/bgm_unknown_ost.mp3" fadein 1.0 volume 0.1
                show unknown at right
                Unknown "Donde hijueputa vas?, vamos al colegio"
                hide unknown
                "No puedes regresar ahora, tienes que ir al colegio, se te hara tarde!"
                jump chapter_one_school_zumen_options


            else:
                jump chapter_one_school_house


label chapter_one_school_entry:
     #cafeteria
     scene bg black
     "*Has llegado al colegio, justamente a la cafeteria*"
     scene bg cafeteria
     stop music fadeout 1.0
     play music "audio/bgm_school.mp3" fadein 1.0 volume 0.3
     pause 1.0
     show rroliga uniforma at left
     show unknown surprised at right
     Unknown "Parece que hemos llegado."
     Unknown "Tarde pero seguro xD."
     Unknown "Bueno te dejo..."
     hide unknown
     show rroliga uniformtired
     Arroliga "Bueno, su lechita de 10 y su resposteria chatel."
     Arroliga "Incluso llegue antes de lo que esperaba, nombe si soy la mera verga."
     show rroliga uniforme at left with moveinright
     Arroliga "Milagro el pan no salio vencido como siempre..."
     Arroliga "Espero que en un futuro no le suban el precio a la lechita."
     "*Actualmente vale el doble*"
     play sound "audio/campana.mp3" volume 0.1
     Arroliga "Parece que ya termino la primera hora."
     Arroliga "Denuevo a clase, ahhh."
     Arroliga "Nada..."

     #pasillo de la escuela
     scene bg pasillo
     show rroliga uniform
     Arroliga "Debo darme prisa."

     #escena de la negra
     scene bg black
     "*Corres rapidamente a tu aula cuando de la nada vez una silueta*"
     stop music fadeout 1.0
     play music "audio/yenesi.mp3" fadein 0.5 volume 0.1
     hide rroliga
     show background_yenesi
     pause
     "*Ves a una chica muy bonita pasar en un abrir y cerrar de ojos*"
     "*Debe ser ella...*"
     "*Vaya que si es hermosa*"
     scene bg pasillo_yenesi
     pause
     stop music fadeout 1.0

     #comienzo de la escena del aula de clase para el evento de la flores
     scene bg pasillo
     show rroliga uniformsur
     Arroliga "Eh, debo darme prisa, el esteril del profe no me va a dejar entrar..."
     show rroliga uniformtired
     Arroliga "Ya de por si solo llego a pelearme con el. heh."



#aula de clase y cafeterias principales del juego
label chapter_one_school_classroom:
    play music "audio/bgm_school.mp3" fadein 1.0 volume 0.3
    scene bg aula
    "*LLegas al aula de clase*"
    pause
    show rroliga uniform
    Arroliga "Denuevo en esta mierda..."
    hide rroliga
    "Pasan las horas..."
    "."
    ".."
    "..."
    show rroliga uniform at left
    Guayaba "Hey, tito, que onda?"
    hide rroliga
    show guayaba at right
    Guayaba "No te tiene podrido esta clase?"
    show guayaba at right
    show rroliga uniform at left
    Arroliga "La verdad es que si...nos salimos?"
    Guayaba "Me parece perfecto, pero antes"
    show guayaba smile
    Guayaba "Ya viste a la Yenesi?, se miraba guapa hoy, a que si!"
    Arroliga "..."
    Guayaba "Hmm"
    Guayaba "No planeas regalarle algo?, digo... mañana es San Valentin"
    Arroliga "Pero que estas diciendo?"
    Guayaba "Nada."
    Arroliga "(Regalarle algo?, es muy buena idea...)"
    Arroliga "(Digo, unas flores no estaria mal, despues de todo es lo mas comun.)"
    Arroliga "Bueno, vamonos de esta paja"

    #recreo
    scene bg receso
    show unknown at left
    show rroliga uniform at right
    show guayaba
    Unknown "te saliste de clase por lo que veo"
    Arroliga "Sip, me da lo mismo, solo es hablar de la \"friendzone\" ese disque psicologo imbecil."
    Guayaba ":v"
    show unknown surprised at left
    Unknown "Veo que trajiste al malparido osito este"
    Arroliga "Si, me esta acompañando"
    show guayaba smile
    pause 2.0
    hide guayaba
    Unknown "A todo esto, viste a la Y?, se dirigia a la cafeteria cuando me fui."
    show rroliga uniforma
    Arroliga "Sobre eso queria hablar, ya que esta en tu seccion, que tipo de flores le gusta?"
    Unknown "Oie, mañana enfrente de todos? xD"
    Unknown "Pues le gustan los girasoles. Carisima te salio la chica baco."
    show rroliga uniformb
    Arroliga "Y no sabes quien me puede conseguirlas justo para mañana?, realmente no tengo tiempo de ir por ellas."
    show rroliga uniformsur
    Unknown "Tengo un amigo, pero tendrias que enviarle un correo, recientemente lo asaltaron en batahola y lo apuñalaron como 59 veces."
    Unknown "Se encuentra bien, pero aun no puede caminar, seguramente si le envias un correo te lo lea."
    Arroliga "Y porque no un mensaje de texto?, digo no es mas conveniente?."
    Unknown "Te acabo de decir que lo asaltaron."
    show rroliga uniforma
    Arroliga "..."
    play sound "audio/campana.mp3" volume 0.1
    Arroliga "Bueno, ire a mi casa, le enviare el correo."
    Unknown "xD, vale."
    $ email += 1




label chapter_one_school_house:
  scene bg black
  "*Has llegado  a tu casa, estas en tu cuarto*"
  stop music fadeout 1.0
  play music "audio/bgm_pyrite.mp3" fadein 1.0 volume 0.3
  #Cuarto de Arroliga

label chapter_one_school_house_options:
  scene bg chante
  "Que hacer?"
  show rroliga uniform at right
  menu chapter_one_house:
                          
                            "Tomar una siesta":
                                hide rroliga
                                Arroliga "ZzZ"
                                scene bg chante_noche
                                Arroliga "ZzZ"
                                Arroliga "ZzZZZ"
                                scene bg chante
                                jump chapter_one_house

                            "Revisar tu E-mail":
                                       if email < 1:
                                            "*Revisas tu correo, pero no hay nada interesante*"
                                            jump chapter_one_house

                                       #si ya le hablaron del correo del mae, este menu hace un loop dependiendo de la varaible email.
                                       elif email >= 1:
                                                        menu:
                                                            "Bandeja de entrada":
                                                                $ email = 2
                                                                "Tienes un correo de: Redacted"
                                                                Unknown "Hey, te fuiste tan rapido que se me olvido darte su direccion E-mail"
                                                                Unknown "Es la siguiente, nosubogordas173@yaju.ni."
                                                                Unknown "Saludos."
                                                                Unknown "Por cierto, su nombre es francostyles."
                                                                jump chapter_one_house

                                                            "Redactar E-mail":
                                                                              "Introduzca la direccion E-mail y el mensaje"
                                                                              if email == 2 and emaildone == 0:
                                                                                            menu:

                                                                                                 "nosubogordas173@yaju.ni":
                                                                                                    "Introduzca su mensaje:"
                                                                                                    menu:
                                                                                                         "Que onda, te escribo este correo por el motivo de....(flores)":
                                                                                                                    "Correo enviado correctamente"
                                                                                                                    Arroliga "Perfecto, ahora es solo esperar que me conteste."
                                                                                                                    jump chapter_one_house
                                                                                                                    $ emaildone +=1 #esta variable hace que no se este sumando el email y por lo tanto lo pueda reproducir todo el tiempo.
                                                                                                                    jump chapter_one_house

                                                                                                         "Te invito a culear vagabundos en granada. sexo asegurado":
                                                                                                                   Arroliga "Definitivamente, no se porque le envie eso."
                                                                                                                   Arroliga "Concentrate, envia el correo correspondiente, es por ella."
                                                                                                                   jump chapter_one_house

                                                                                                         "Con Paquetigo Gamer disfrutá de los mejores juegos sin gastar internet. ¡Aprovechá ahora!":
                                                                                                                   Arroliga "heh..."
                                                                                                                   Arroliga "Concentrate alacienputa"
                                                                                                                   jump chapter_one_house

                                                                                                 "Enacal@yimeil.com":
                                                                                                                     Arroliga "No creo que este sea el correo indicado"
                                                                                                                     jump chapter_one_house

                                                                                                 "teMaldigoClaro@jotmeil.ni":
                                                                                                                       Arroliga "Estos hijos de puta de claro, de todas formas no responden correo."
                                                                                                                       jump chapter_one_house
                                                                              elif emaildone ==1:
                                                                                            menu:
                                                                                                 "nosubogordas173@yaju.ni":
                                                                                                                Arroliga "Ya tengo el correo listo, ahora es solo esperar que me responda."
                                                                                                 "Enacal@yimeil.com":
                                                                                                                Arroliga "No creo que este sea el correo indicado"
                                                                                                                jump chapter_one_house

                                                                                                 "teMaldigoClaro@jotmeil.ni":
                                                                                                                Arroliga "Estos hijos de puta de claro, de todas formas no responden correo."
                                                                                                                jump chapter_one_house
                                                                              else:
                                                                                  menu:
                                                                                                 "Enacal@yimeil.com":
                                                                                                                Arroliga "No creo que este sea el correo indicado"
                                                                                                                jump chapter_one_house

                                                                                                 "teMaldigoClaro@jotmeil.ni":
                                                                                                                Arroliga "Estos hijos de puta de claro, de todas formas no responden correo."
                                                                                                                jump chapter_one_house
                            "Salir de la casa":
                                               if emaildone < 1:
                                                "*No puedes salir ahora, debes enviar el correo.*"
                                                jump chapter_one_school_zumen_options

                                               else:
                                                    "*Sales de la casa*"
                                                    scene bg street
                                                    "A donde quieres ir?"
                                                    menu:
                                                              "Zumen":
                                                                "*Te diriges al zumen*"
                                                                jump chapter_one_school_zumen

                                                              "Colegio":
                                                                "*Te diriges al colegio*"
                                                                jump chapter_one_school_entry

                                                              "Regresar a casa":
                                                                jump chapter_one_school_house