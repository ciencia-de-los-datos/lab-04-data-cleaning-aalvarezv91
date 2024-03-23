"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df.dropna(inplace=True)
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df = df.apply(lambda x: x.str.replace('_', '-') if x.dtype == "object" else x)
    df = df.apply(lambda x: x.str.replace('-', ' ') if x.dtype == "object" else x)

    def convert_date(date):
        try:
            return pd.to_datetime(date, format='%d/%m/%Y')
        except ValueError:
            return pd.to_datetime(date, errors='coerce')
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convert_date)

    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '').str.replace('$', '').str.extract('(\d+)').astype(float)
    
    df.drop_duplicates(inplace=True)
    
    return df