import PyPDF2
import re
import requests

def ler_pdf(caminho_pdf):
    with open(caminho_pdf, "rb") as f:
        leitor = PyPDF2.PdfReader(f)
        texto = ""
        for pagina in leitor.pages:
            texto += pagina.extract_text()
    return texto

def extrair_datas(texto):
    return re.findall(r"\d{4}-\d{2}-\d{2}", texto)

def verificar_feriados(datas):
    url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"
    resposta = requests.get(url)
    feriados = [f["date"] for f in resposta.json()]
    for data in datas:
        if data in feriados:
            print(f"{data} é feriado")
        else:
            print(f"{data} não é feriado")

if __name__ == "__main__":
    caminho = "Lista_de_datas.pdf"  # Exemplo
    texto = ler_pdf(caminho)
    datas = extrair_datas(texto)
    verificar_feriados(datas)
