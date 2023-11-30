# Analizador Lexico para PHP

## Integrantes
1. Daniel Mateo
2. Cristopher Arroba
3. Roberto Patiño

Este proyecto consiste en un analizador léxico sintáctico y semántico para evaluar el lenguaje de programación PHP. 
El mismo cuenta con IDE en línea para probar las sentencias de código deseadas.
## Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.x
- Node.js y npm

## Instalación

1. Abre una terminal o línea de comandos.
2. Desde la raíz del proyecto, instala las dependencias de Python ejecutando:
    ```bash
    pip install -r requirements.txt
    ```
3. Ingresa al directorio `gui`:
    ```bash
    cd gui
    ```
4. Instala los módulos requeridos de Node.js usando:
    ```bash
    npm install
    ```

## Ejecución

1. Inicia el servidor Python desde la raíz del proyecto:
    ```bash
    python server.py
    ```
2. Abre Visual Studio Code y asegúrate de tener la extensión "Live Server" instalada.
3. Abre el archivo HTML en Visual Studio Code y, luego, inicia la extensión "Live Server" para interactuar con el IDE.

## Uso

Una vez que el servidor esté en funcionamiento y la extensión "Live Server" esté ejecutándose en Visual Studio Code, podrás interactuar con el IDE accediendo a la dirección local proporcionada por la extensión "Live Server".

Lo siguiente será escribir las sentencias de código en el espacio correspondiente, y una vez se desee validar el mismo se debe dar click en el botón run.
En la terminal de la parte inferior se mostrarán detalles en caso de existir algún posible error.
