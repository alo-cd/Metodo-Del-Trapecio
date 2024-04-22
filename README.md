#Integración Numérica con el Método del Trapecio
Este proyecto contiene un script de Python que implementa el método del trapecio para calcular la integral numérica de una función dada en un intervalo específico.

#Descripción
El script permite al usuario ingresar la expresión de la función f(x) que desea integrar, así como los valores de a y b que definen el intervalo de integración, y el valor de n que determina el número de tramos a utilizar en el método del trapecio.

Utilizando la librería sympy, el script convierte la expresión ingresada en una función de Python que puede ser evaluada con valores numéricos. Luego, implementa el método del trapecio para calcular la integral numérica de la función en el intervalo especificado.

Finalmente, el script muestra el resultado de la integral calculada y genera una gráfica que visualiza la función, los trapecios utilizados en el cálculo y el área bajo la curva.

#Requisitos
Python 3.x
Bibliotecas: numpy, matplotlib, sympy
#Uso
Clona este repositorio o descarga los archivos.
Asegúrate de tener instaladas las bibliotecas requeridas (numpy, matplotlib, sympy). Puedes instalarlas con pip:

Copy code

pip install numpy matplotlib sympy

#Ejecuta el script integracion_numerica.py.
Cuando se te solicite, ingresa la expresión de la función f(x) que deseas integrar. Por ejemplo: x**2 + 2*x + 1.
Ingresa los valores de a y b que definen el intervalo de integración.
Ingresa el valor de n que determina el número de tramos a utilizar en el método del trapecio.
El script calculará la integral numérica y mostrará el resultado en la salida.
Además, se generará una ventana con una gráfica que muestra la función, los trapecios utilizados en el cálculo y el área bajo la curva.
Ejemplos de funciones
Aquí tienes algunos ejemplos de funciones que puedes ingresar:

x**2 + 2*x + 1
np.sin(x)
np.exp(x)
1/(1 + x**2)
np.sqrt(x**2 + 1)
Puedes combinar diferentes funciones y operaciones para crear expresiones más complejas.

#Contribuciones
Si encuentras algún error o tienes sugerencias de mejora, no dudes en abrir un issue o enviar un pull request.
