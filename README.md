# Teste de Integração com API Pública - ANS

Este projeto foi desenvolvido em **Python** para consolidar os dados de **Despesas com Eventos/Sinistros** dos últimos 3 trimestres.  
O objetivo é ler arquivos CSV/TXT/XLSX, normalizar as colunas e gerar um único arquivo consolidado.

---

##  Estrutura do Projeto


---

##  Como Executar no VS Code

### 1. Pré-requisitos
- Python 3.10+ instalado
- VS Code com extensão Python
- Bibliotecas necessárias:
  - `pandas`
  - `openpyxl` (para arquivos Excel)

Instale com:
```bash
pip install pandas openpyxl

python arquivos/main.py

---

#### Como rodar o arquivo main.py no VS Code

No terminal do VS Code, dentro da pasta do projeto, rode:
python arquivos/main.py

O programa percorre a pasta arquivos e identifica os arquivos dos trimestres (1T2025.csv, 2T2025.csv, 3T2025.csv).
O programa lê arquivos nos formatos CSV, TXT e XLSX. Identifica automaticamente colunas relacionadas a Despesas com Eventos/Sinistros e normaliza os dados para manter consistência nas colunas.


