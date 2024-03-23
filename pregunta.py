"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.dropna()
    df=df.apply(lambda x: x.astype(str))
    df=df.apply(lambda x: x.str.replace(",", ""))
    df=df.apply(lambda x: x.str.replace("$", ""))
    df=df.apply(lambda x: x.str.replace("_", " "))
    df=df.apply(lambda x: x.str.replace("-", " "))
    df=df.apply(lambda x: x.str.lower())
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst = True, format='mixed')
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    df = df.drop_duplicates()

    return df