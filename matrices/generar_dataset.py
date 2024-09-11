import numpy as np
import os


# Función para escribir las matrices en un archivo .txt legible por C++
def guardar_matrices_txt(matriz1, matriz2, ruta_archivo):
    tamano = f"{matriz1.shape[0]} {matriz1.shape[1]} {matriz2.shape[0]} {matriz2.shape[1]}\n"
    print(tamano)
    with open(ruta_archivo, 'a') as f:
        f.write(tamano)  # Dimensiones de la primera matriz
        for fila in matriz1:
            f.write(" ".join(map(str, fila)) + "\n")  # Guardar filas de la matriz 1
        for fila in matriz2:
            f.write(" ".join(map(str, fila)) + "\n")  # Guardar filas de la matriz 2
    print(f"Matrices guardadas en {ruta_archivo}")


# Función para generar pares de matrices cuadradas
def generar_pares_cuadradas(tamanos, tipo_matriz='densa', valor_min=-10, valor_max=10, porcentaje_ceros=0.5,
                            ruta_salida="dataset/cuadradas"):
    os.makedirs(ruta_salida, exist_ok=True)
    for tamano in tamanos:
        for _ in range(3):
            if tipo_matriz == 'densa':
                matriz1 = np.random.randint(valor_min, valor_max, size=(tamano, tamano))
                matriz2 = np.random.randint(valor_min, valor_max, size=(tamano, tamano))
            elif tipo_matriz == 'dispersa':
                matriz1 = np.random.choice([0, np.random.randint(valor_min, valor_max)], size=(tamano, tamano),
                                           p=[porcentaje_ceros, 1 - porcentaje_ceros])
                matriz2 = np.random.choice([0, np.random.randint(valor_min, valor_max)], size=(tamano, tamano),
                                           p=[porcentaje_ceros, 1 - porcentaje_ceros])
            elif tipo_matriz == 'diagonal':
                matriz1 = np.diag(np.random.randint(valor_min, valor_max, size=tamano))
                matriz2 = np.diag(np.random.randint(valor_min, valor_max, size=tamano))

            archivo_salida = f"{ruta_salida}/matrices_cuadradas.txt"
            guardar_matrices_txt(matriz1, matriz2, archivo_salida)


# Función para generar pares de matrices rectangulares
def generar_pares_rectangulares(tamanos, tipo_matriz='densa', valor_min=-10, valor_max=10, porcentaje_ceros=0.5,
                                ruta_salida="dataset/rectangulares"):
    os.makedirs(ruta_salida, exist_ok=True)

    for filas, columnas in tamanos:

        for _ in range(3):

            if tipo_matriz == 'densa':
                matriz1 = np.random.randint(valor_min, valor_max, size=(filas, columnas))
                matriz2 = np.random.randint(valor_min, valor_max, size=(
                columnas, filas))  # La segunda debe ser compatible para multiplicación
            elif tipo_matriz == 'dispersa':
                matriz1 = np.random.choice([0, np.random.randint(valor_min, valor_max)], size=(filas, columnas),
                                           p=[porcentaje_ceros, 1 - porcentaje_ceros])
                matriz2 = np.random.choice([0, np.random.randint(valor_min, valor_max)], size=(columnas, filas),
                                           p=[porcentaje_ceros, 1 - porcentaje_ceros])
            elif tipo_matriz == 'diagonal':
                matriz1 = np.zeros((filas, columnas))
                min_dim1 = min(filas, columnas)
                np.fill_diagonal(matriz1[:min_dim1, :min_dim1], np.random.randint(valor_min, valor_max, size=min_dim1))

                matriz2 = np.zeros((columnas, filas))
                min_dim2 = min(columnas, filas)
                np.fill_diagonal(matriz2[:min_dim2, :min_dim2], np.random.randint(valor_min, valor_max, size=min_dim2))

            archivo_salida = f"{ruta_salida}/matrices_rectangulares.txt"
            guardar_matrices_txt(matriz1, matriz2, archivo_salida)


# Función principal para generar pares de matrices cuadradas y rectangulares en formato .txt
def generar_datasets_multiplicacion():
    print("Generación de pares de matrices cuadradas:")
    tamanos_cuadradas = [8, 16, 32, 64, 128, 256, 512, 1024]  # Tamaños de matrices cuadradas
    generar_pares_cuadradas(tamanos_cuadradas, tipo_matriz='densa', valor_min=-10, valor_max=10,
                            ruta_salida="matrices/dataset")

    print("\nGeneración de pares de matrices rectangulares:")
    tamanos_rectangulares = [(16, 8), (8, 16),
                             (32, 16), (16, 32),
                             (64, 32), (32, 64),
                             (128, 64), (64, 128),
                             (256, 128), (128, 256),
                             (512, 256), (256, 512),
                             (1024, 512), (512, 1024)]  # Tamaños de matrices rectangulares
    generar_pares_rectangulares(tamanos_rectangulares, tipo_matriz='densa', valor_min=-10, valor_max=10,
                                ruta_salida="matrices/dataset")


# Ejecutar la función principal para generar los datasets
generar_datasets_multiplicacion()
