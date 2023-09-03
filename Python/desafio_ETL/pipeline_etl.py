import pandas as pd
df = pd.read_excel('SD2023.xlsx')
print(df)

df.loc[df["Clientes"]=="negativo", "Total Debito"]
df["Total Debito"] = df["Valor Compra"] - df["Valor Pago"]
print(df)

df.to_excel("SD2023_Resultado.xlsx, index=False")