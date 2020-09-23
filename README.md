# Meetup de PyAr
Aca les dejo un repo con el codigo que se mostro en la charla de PyAr


# CLI de Vue.js
Para inicar un proyecto en Vue.js es el siguiente comando 

``vue init webpack _nombreDeLaCarpeta_``

# Comandos para inicar App
para inicaiar el backend primero se tiene que instalar **Flask** para esto hay que instalar las dependencias en el archivo _requirements.txt_ en cualquiera de las 2 carpetas del backend se puede encontrar este archivo. Una vez hecho esto se tiene que utilizar el comando

``python server.py``

Para iniciar el frontend se tiene que posisionar en la carpeta frontend y ejecutar el comando:

``npm run dev``

# Integracion

Para hacer la integracion de Flask y Vue se tiene que compilar los archivos de Vue se tiene que posisionar en la carptea frontend y con el comando:

``npm run build``

una vez compilado todo el codigo solo falta ir a la carpeta backend y ejecutar el codigo:

``python server.py``