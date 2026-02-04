import os
import pandas as pd
import zipfile


BASE_PATH = r"E:\Teste para estagio\Intuitive Care\teste 1\Teste1\Teste_1_\arquivos"

def processar_arquivo(filepath, ano, trimestre):
    ext = os.path.splitext(filepath)[1].lower()
    df = None

    try:
        if ext == ".csv" or ext == ".txt":
            df = pd.read_csv(filepath, sep=";", encoding="latin1")
        elif ext == ".xlsx":
            df = pd.read_excel(filepath)
        else:
            return None
    except Exception as e:
        print(f"Erro ao ler {filepath}: {e}")
        return None


    colunas = [c for c in df.columns if "Despesa" in c or "Sinistro" in c]
    if not colunas:
        return None


    cnpj = df["CNPJ"] if "CNPJ" in df.columns else "SUSPEITO"
    razao = df["RazaoSocial"] if "RazaoSocial" in df.columns else "SUSPEITO"

    df_norm = pd.DataFrame({
        "CNPJ": cnpj,
        "RazaoSocial": razao,
        "Ano": ano,
        "Trimestre": trimestre,
        "ValorDespesas": df[colunas[0]] if colunas else 0
    })
    return df_norm

def main():
    dados_final = pd.DataFrame()


    for f in os.listdir(BASE_PATH):
        filepath = os.path.join(BASE_PATH, f)
        if os.path.isfile(filepath):

            nome = os.path.splitext(f)[0]
            if "T" in nome:
                trimestre, ano = nome.split("T")
                ano = ano.strip()
                trimestre = trimestre.strip()
            else:
                ano, trimestre = "2025", "?"

            df = processar_arquivo(filepath, ano, trimestre)
            if df is not None:
                dados_final = pd.concat([dados_final, df], ignore_index=True)

   
    if "CNPJ" in dados_final.columns and "RazaoSocial" in dados_final.columns:
        duplicados = dados_final.groupby("CNPJ")["RazaoSocial"].nunique()
        suspeitos = duplicados[duplicados > 1].index
        dados_final.loc[dados_final["CNPJ"].isin(suspeitos), "RazaoSocial"] = "SUSPEITO"

  
    if "ValorDespesas" in dados_final.columns:
        dados_final = dados_final[dados_final["ValorDespesas"].astype(float) > 0]

   
    if "Trimestre" in dados_final.columns:
        dados_final["Trimestre"] = dados_final["Trimestre"].apply(lambda x: f"Q{x}")

  
    dados_final.to_csv("consolidado_despesas.csv", index=False, sep=";")

   
    with zipfile.ZipFile("consolidado_despesas.zip", "w") as z:
        z.write("consolidado_despesas.csv")

    print("Processo concluído! Arquivo consolidado_despesas.zip gerado.")

if __name__ == "__main__":
    main()