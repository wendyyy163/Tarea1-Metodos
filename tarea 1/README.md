\# Tarea 1: Introducción a los Métodos Numéricos y Entorno de Trabajo



\* \*\*Unidad de Enseñanza-Aprendizaje:\*\* Métodos Numéricos en Ingeniería (Clave 1151039)

\* \*\*Trimestre:\*\* 26-O, Otoño 2026

\* \*\*Licenciatura:\*\* Ingeniería Ambiental

\* \*\*Nombre:\*\* Wendy Sismai Jiménez Mejía

\* \*\*Matrícula:\*\* 2233000794

\* \*\*Profesor:\*\* M. en C. Gabriel Hurtado Avilés

\* \*\*Fecha:\*\* 15 de octubre de 2026



\---



\## 1. ¿Qué son los métodos numéricos?

Los métodos numéricos son técnicas algorítmicas que permiten formular problemas matemáticos para resolverlos mediante operaciones aritméticas simples. A diferencia de las soluciones analíticas (que entregan fórmulas exactas), los métodos numéricos proporcionan soluciones aproximadas debido al uso de representaciones finitas en computadora y al truncamiento de series. El análisis de error permite cuantificar la precisión y asegurar la convergencia hacia la solución real.



\## 2. Aplicación en Ingeniería Ambiental

1\. \*\*Balance de Oxígeno Disuelto en Ríos (Modelo de Streeter-Phelps):\*\* Permite evaluar el impacto de descargas de aguas residuales. Debido a la variación temporal y espacial de la temperatura y las tasas de reaireación, se requieren métodos numéricos para integrar las ecuaciones diferenciales ordinarias asociadas.

2\. \*\*Transporte de Contaminantes en Aguas Subterráneas:\*\* Modela la dispersión de plumas de contaminación en el suelo. La heterogeneidad del medio poroso impide el uso de fórmulas cerradas, por lo que se emplean métodos numéricos de diferencias finitas o elementos finitos.



\## 3. Herramientas para Métodos Numéricos

\* \*\*Lenguajes compilados:\*\* C, C++, Fortran (alta velocidad y control de memoria).

\* \*\*Entornos matriciales:\*\* MATLAB, GNU Octave (protopitado interactivo de matrices).

\* \*\*Python científico:\*\* NumPy, SciPy, Matplotlib (ecosistema abierto y versátil).

\* \*\*Álgebra simbólica:\*\* SymPy, Mathematica (cálculo exacto).

\* \*\*Bibliotecas de base:\*\* BLAS, LAPACK (álgebra lineal optimizada).



\## 4. Herramientas del Curso

\* \*\*Docker:\*\* Plataforma de contenedores ligeros que aíslan el entorno. Se usa frente a una máquina virtual por su menor consumo de recursos.

\* \*\*Comandos de Docker:\*\* `Dockerfile` define la imagen, `compose.yaml` los servicios. Comandos principales: `up -d` (inicia), `exec` (ejecuta), `stop` (detiene), `down` (elimina el contenedor), `ps` (muestra estado) y `logs` (registros).

\* \*\*Versiones del entorno:\*\*

&#x20; \* \*\*GNU Octave:\*\* 7.3.0

&#x20; \* \*\*Python:\*\* 3.11.2

&#x20; \* \*\*GCC (C):\*\* 12.2.0



\---



\## Capturas del Entorno



!\[Docker Up](img/01-up.png)

!\[Docker PS](img/02-ps.png)

!\[Versiones de Software](img/03-versiones.png)

!\[Docker Desktop](img/04-docker-desktop.png)

!\[Programas Ejecutándose](img/05-programas.png)



\---



\## Pregunta del Ejercicio 4 (Suma)

\*\*¿Por qué 0.1 + 0.2 no da exactamente 0.3?\*\*

En el estándar IEEE 754 de punto flotante de doble precisión, números decimales como `0.1` y `0.2` no tienen representación binaria exacta. La suma genera un pequeño error de redondeo (`0.30000000000000004`). Los tres lenguajes (C, Python y Octave) coinciden en el resultado porque los tres utilizan la misma especificación del estándar IEEE 754.



\---



\## Tabla de Casos de Prueba (Calculadora)



| Caso de Prueba | Entrada 1 | Entrada 2 | Operación | Resultado / Mensaje Esperado |

| :--- | :--- | :--- | :--- | :--- |

| Operación Normal | `15.5` | `4.5` | Suma (`1`) | `20` |

| División entre Cero | `10` | `0` | División (`4`) | "¡Advertencia/Error! No se puede dividir entre cero." |

| Entrada No Numérica | `abc` -> `10` | `5` | Resta (`2`) | "¡Error! La entrada debe ser un número..." e ingresa `10`. Resultado: `5`. |

| Salir del programa | N/A | N/A | Salir (`5`) | Finaliza la ejecución correctamente. |



\---



\## Referencias (Formato APA 7ª edición)

\* Burden, R. L., \& Faires, J. D. (2011). \*Análisis Numérico\* (9a ed.). Cengage Learning.

\* Chapra, S. C., \& Canale, R. P. (2015). \*Métodos Numéricos para Ingenieros\* (7a ed.). McGraw-Hill.

