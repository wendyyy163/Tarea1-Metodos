\# Tarea 1: Introducción a los Métodos Numéricos y Entorno de Trabajo



\* \*\*Unidad de Enseñanza-Aprendizaje:\*\* Métodos Numéricos en Ingeniería (Clave 1151039)

\* \*\*Trimestre:\*\* 26-O, Otoño 2026

\* \*\*Licenciatura:\*\* Ingeniería Ambiental

\* \*\*Nombre:\*\* Wendy Sismai Jiménez Mejía

\* \*\*Matrícula:\*\* 2233000794

\* \*\*Profesor Responsable:\*\* M. en C. Gabriel Hurtado Avilés

\* \*\*Fecha:\*\* 15 de octubre de 2026



\---



\## Ejercicio 2. El README



\### 1. ¿Qué son los métodos numéricos?

Los métodos numéricos son técnicas algorítmicas y formulaciones matemáticas mediante las cuales es posible formular problemas de tal forma que puedan resolverse mediante operaciones aritméticas simples (sumas, restas, multiplicaciones y divisiones) (Chapra \& Canale, 2015). 



Se distinguen de las soluciones analíticas en que estas últimas entregan respuestas exactas expresadas en fórmulas explícitas o continuas. Sin embargo, en la práctica ingenieril, la mayoría de los problemas físicos complejos no cuentan con una solución analítica cerrada (Burden \& Faires, 2011). 



El resultado de un método numérico es siempre una \*\*aproximación\*\*. Esto se debe al uso de representaciones finitas de números en las computadoras y a la necesidad de discretizar ecuaciones continuas. En este contexto, el \*\*error\*\* juega un papel central: el análisis numérico busca cuantificar, controlar y minimizar tanto el error de redondeo (derivado de la precisión finita de la máquina) como el error de truncamiento (derivado de aproximar un proceso infinito mediante uno finito), garantizando que la solución numérica converja adecuadamente a la solución real (Burden \& Faires, 2011; Chapra \& Canale, 2015).



\---



\### 2. ¿Cómo se aplican en Ingeniería Ambiental?

Como estudiante de \*\*Ingeniería Ambiental\*\*, los métodos numéricos son fundamentales para modelar y predecir el comportamiento de sistemas naturales complejos. A continuación se describen dos problemas concretos del área:



1\. \*\*Balance de Oxígeno Disuelto en Ríos (Modelo de Streeter-Phelps):\*\*

&#x20;  \* \*Qué se calcula:\* La variación de la concentración de oxígeno disuelto ($DO$) y la demanda bioquímica de oxígeno ($BOD$) a lo largo del cauce de un río tras recibir una descarga de aguas residuales.

&#x20;  \* \*Por qué no basta con una fórmula cerrada:\* En condiciones reales, los ríos presentan geometrías variables, cambios de temperatura con el tiempo, múltiples puntos de descarga y tasas no constantes de reaireación y descomposición orgánica. Esto genera sistemas de ecuaciones diferenciales ordinarias o parciales acopladas que no poseen una solución analítica única y requieren métodos numéricos de integración (como Euler o Runge-Kutta) para simular la calidad del agua a lo largo del tiempo y espacio (Chapra \& Canale, 2015).



2\. \*\*Transporte de Contaminantes en Aguas Subterráneas (Ecuación de Advección-Dispersión):\*\*

&#x20;  \* \*Qué se calcula:\* La pluma de dispersión y la concentración de un contaminante químico o pesado a través de un acuífero profundo en función del tiempo.

&#x20;  \* \*Por qué no basta con una fórmula cerrada:\* Las propiedades físicas del suelo (porosidad, permeabilidad e hidráulica) son heterogéneas e irregulares en las tres dimensiones del espacio. Resolver la ecuación diferencial en derivadas parciales del transporte de masa exige métodos discretos como el Método de Diferencias Finitas (FDM) o el Método de Elementos Finitos (FEM) (Chapra \& Canale, 2015).



\---



\### 3. ¿Qué herramientas se usan para trabajar con métodos numéricos?

El desarrollo de métodos numéricos emplea diversas familias de herramientas computacionales, según los requisitos de velocidad, facilidad de prototipado y flexibilidad:



\* \*\*Lenguajes compilados (C, C++, Fortran):\*\* Ofrecen la máxima velocidad de ejecución y gestión eficiente de la memoria de bajo nivel, siendo la elección estándar para cómputo de alto rendimiento (HPC).

\* \*\*Lenguajes interpretados / Entornos matriciales (MATLAB, GNU Octave):\*\* Diseñados para la manipulación interactiva de vectores y matrices sin necesidad de compilación previa, ideales para prototipado rápido de algoritmos.

\* \*\*Python científico (NumPy, SciPy, Matplotlib):\*\* Ecosistema de código abierto altamente flexible que combina la facilidad de sintaxis con bibliotecas optimizadas en C y Fortran para cálculo matricial, análisis estadístico y graficación.

\* \*\*Álgebra simbólica (SymPy, Mathematica):\*\* Herramientas enfocadas en la manipulación analítica y exacta de expresiones matemáticas (derivación simbólica, integración explícita) antes de aplicar esquemas numéricos.

\* \*\*Bibliotecas de base (BLAS, LAPACK):\*\* Rutinas de bajo nivel escritas en Fortran/C que proporcionan la infraestructura básica súper optimizada para operaciones de álgebra lineal numérica (multiplicación de matrices, sistemas de ecuaciones).



\#### Herramientas empleadas en la bibliografía consultada:

\* \*\*Chapra \& Canale (2015):\*\* Utiliza MATLAB, VBA (Excel), Mathcad y pseudocódigo enfocado en C y Fortran.

\* \*\*Burden \& Faires (2011):\*\* Presenta algoritmos generales en pseudocódigo y ejemplos implementados en C, MATLAB y MAPLE.



\---



\### 4. ¿Qué herramientas usamos en este curso?

\* \*\*Docker:\*\* Plataforma de virtualización a nivel de sistema operativo que permite empaquetar aplicaciones y sus dependencias en contenedores aislados y portables.

\* \*\*Docker frente a una Máquina Virtual:\*\* A diferencia de una máquina virtual (VM) que emula un sistema operativo completo con su propio hipervisor y kernel, un contenedor de Docker comparte el kernel del sistema operativo anfitrión. Esto hace que Docker sea infinitamente más ligero, rápido de iniciar y eficiente en el consumo de memoria RAM y CPU.

\* \*\*Herramientas de Docker en el curso:\*\* 

&#x20; \* `Dockerfile`: Archivo de texto con las instrucciones para construir la imagen del contenedor.

&#x20; \* `compose.yaml`: Archivo de configuración para definir y ejecutar servicios de Docker.

&#x20; \* \*Comandos principales:\* `docker compose up -d` (inicia los contenedores en segundo plano), `exec` (ejecuta comandos o terminales dentro del contenedor activo), `stop` (detiene temporalmente los contenedores), `down` (detiene y elimina los contenedores y redes creadas), `ps` (muestra el estado actual de los contenedores) y `logs` (muestra los registros de salida).

&#x20; \* \*Apagar vs. Borrar a un contenedor:\* Apagar un contenedor (`stop`) suspende su ejecución conservando su estado y archivos creados, mientras que borrarlo (`down` o `rm`) destruye la instancia del contenedor liberando los recursos de almacenamiento.

\* \*\*GNU Octave:\*\* Entorno de cálculo numérico interactivo ejecutable mediante el comando `octave`. \*\*Versión obtenida del contenedor:\*\* `7.3.0`.

\* \*\*Python:\*\* Lenguaje interpretado de propósito general ejecutable mediante `python3`. \*\*Versión obtenida del contenedor:\*\* `3.11.2`.

\* \*\*C con GCC:\*\* Compilador estándar de C ejecutable mediante `gcc`. \*\*Versión obtenida del contenedor:\*\* `12.2.0` (Debian 12.2.0-14+deb12u1).



\---



\## Ejercicio 3. Capturas del Entorno Corriendo



!\[01-up](img/01-up.png)

\*Figura 1. Ejecución del comando docker compose up -d --build finalizado con estado Started.\*



!\[02-ps](img/02-ps.png)

\*Figura 2. Estado de los contenedores mediante docker compose ps en estado Up.\*



!\[03-versiones](img/03-versiones.png)

\*Figura 3. Verificación de versiones de octave, python3 y gcc dentro del contenedor.\*



!\[04-docker-desktop](img/04-docker-desktop.png)

\*Figura 4. Vista de Docker Desktop mostrando el contenedor activo del curso.\*



!\[05-programas](img/05-programas.png)

\*Figura 5. Ejecución interactiva de los dos programas dentro del contenedor.\*



\---



\## Ejercicio 4. Documentación de los Programas



\### Programa 1: Suma de dos números

\* \*\*Archivos:\*\* `suma.c`, `suma.py`, `suma.m`.

\* \*\*Funcionamiento:\*\* Lee dos números desde la línea de comandos o de forma interactiva por la pantalla; en caso de omitirse, utiliza por defecto `0.1` y `0.2`. Imprime el resultado con diecisiete cifras significativas (`%.17g`).



\#### ¿Por qué 0.1 + 0.2 no da exactamente 0.3?

En el estándar de punto flotante de doble precisión IEEE 754 (utilizado por la mayoría de las arquitecturas de computadoras modernas), números decimales simples como `0.1` y `0.2` no poseen una representación exacta en código binario (se convierten en fracciones binarias periódicas infinitas). Al almacenar y sumar estos valores, ocurre un pequeño error de redondeo en el bit menos significativo, produciendo internamente `0.30000000000000004`. Los tres lenguajes (C, Python y Octave) coinciden exactamente en este comportamiento porque los tres implementan de manera estricta el estándar IEEE 754.



\#### Instuccione de Compilación y Ejecución:

```bash

\# Cambiar a la carpeta del programa

cd programa1-suma



\# Ejecución en C (Compilación previa con GCC)

gcc -o suma suma.c

./suma



\# Ejecución en Python

python3 suma.py



\# Ejecución en GNU Octave

octave suma.m

