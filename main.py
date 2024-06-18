# importacion del metodo para la solucion

import lectura
#inicio del objeto 
main=lectura.lectura()
#inicio de los llamados de los metodos parte 1 
main.fortamo()
main.mubMax()
main.fortamo()

main.resfil()
main.fortamo()
main.rescol()
main.fortamo()
main.descartar()
#fin del llamdo de metodos parte 1 
#Comprobar que cumpla las solucion obtica sino realizar segunda parte 
if ((len(main.col)+len(main.fil))!=len(main.mat)):
    main.sol()
main.fortamo()
main.resul()