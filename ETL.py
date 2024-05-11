import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")

def main():
    # Cargar el DataFrame
    df_alcohol = pd.read_csv('BBDD Alcohol.csv')

    # Filtrar el DataFrame según los criterios especificados
    df_filtrado = df_alcohol[
        (df_alcohol['FILTRO_A'] == 2) & 
        (df_alcohol['FILTRO_B'] == 1) & 
        (df_alcohol['FILTRO_C'] > 18) & 
        (df_alcohol['FILTRO_C'] < 65) & 
        (df_alcohol['FILTRO_C2'] > 1) & 
        (df_alcohol['FILTRO_C2'] < 7) & 
        (df_alcohol['NSE'] > 0) & 
        (df_alcohol['NSE'] < 5)
    ]

    # Reemplazar valores vacíos con valor nulo
    df_filtrado.replace([' '], pd.NA, inplace=True)

    def extraer_numeros(celda):
        if isinstance(celda, str):  # Verifica si el valor es una cadena de texto
            numeros = re.findall(r'\d+', celda)
            numero = ''.join(numeros)
            return pd.to_numeric(numero, errors='coerce')  # Convierte a numérico o NaN
        return pd.to_numeric(celda, errors='coerce')  # Asegura que todos los valores sean numéricos o NaN

    # Lista de columnas que no deben ser tocadas
    columnas_no_modificar = ['NSE2', 'VPOND1', 'VPOND2']

    # Aplica la función a las columnas que no están en la lista de exclusión
    for columna in df_filtrado.columns:
        if columna not in columnas_no_modificar:
            df_filtrado[columna] = df_filtrado[columna].apply(extraer_numeros)

    # Convertir las columnas modificadas a Int64
    for columna in df_filtrado.columns:
        if columna not in columnas_no_modificar:
            df_filtrado[columna] = df_filtrado[columna].astype('Int64')

    # Filtro de datos del perfil, para evitar outliers
    df_filtro_2 = df_filtrado.loc[
        (df_filtrado['P1'].isin([1, 2])) &
        (df_filtrado['P2'] > 0) & (df_filtrado['P2'] < 50) &
        (df_filtrado['P3'] > 0) & (df_filtrado['P3'] < 9)
    ]

    # Guardar o imprimir el DataFrame final
    # Guardar el DataFrame final si es necesario
    df_filtro_2.to_parquet('bd_alcohol.parquet', index=False)

if __name__ == "__main__":
    main()
