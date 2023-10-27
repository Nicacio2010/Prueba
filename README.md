Para empezar el sensor de color LEGO Spike tiene sus Características clave las cuáles son:

Frecuencia de muestreo del sensor: 100 Hz
Distancia de lectura óptima: 16 mm (dependiendo del tamaño, color y superficie del objeto)
Tres LED controlados individualmente (solo Python)

https://github.com/Nicacio2010/Prueba/blob/main/docs/Imagen%20del%20Sensor%20de%20color%20Spike.jpg

Ademas este sensor de color LEGO tiene 3 modos principales:
Color: 
En este modo el sensor detecta 8 colores diferentes, cada color que detecta el sensor de LEGO está representado por un valor,
el sensor también puede generar los valores sin procesar de rojo, verde y azul (RGB) por separado. 
Los valores de los colores son:
Modo	Rango de salida
Color	-1 = Sin objeto 0 = Negro (LEGO:26; R:0, G:0, B:0)
1 = Magenta (LEGO:124; R:144, G:31, B:118)
3 = Azul (LEGO :23; R:30, G:90, B:168)
4 = Turquesa (LEGO:322; R:104, G:195, B226)
5 = Verde (LEGO:28; R:0, G:133, B :43)
7 = Amarillo (LEGO:24; R:250, G:200, B:10) 9
= Rojo (LEGO:21; R:180, G:0, B:0)
10 = Blanco (LEGO:01 ; R:244, G:244, B:244)
Luz reflejada	0% = sin reflejo, 100% = muy reflectante
Luz ambiental ( solo Python )	0% = oscuro, 100% = brillante

Intensidad de luz reflejada:
En este modo el sensor de color emite una luz y mide la cantidad reflejada hacia si mismo desde la superficie que se está probando. En cuanto a la intensidad 
de la luz, se mide como porcentaje del 0 al 100. Siendo 0 el mas oscuro y 100 el más brillante.

Intensidad de luz ambiental (solo Python): en este modo, el sensor de color mide la cantidad de luz en su entorno, sin producir su propia fuente de luz. La intensidad
de luz ambiental, se mide como un porcentaje del 0 al 100. Siendo 0 muy oscuro y 100 muy brillante.
Esto significa que su robot puede estar programado para emitir una alarma al salir el sol por la mañana o para detenerse si las luces se apagan.







