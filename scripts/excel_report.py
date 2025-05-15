# scripts/excel_report.py
import pandas as pd
df = pd.read_csv("ventes.csv")
summary = df.groupby("region")["ventes"].sum().reset_index()
summary.to_excel("rapport_ventes.xlsx")
print("Rapport généré !")