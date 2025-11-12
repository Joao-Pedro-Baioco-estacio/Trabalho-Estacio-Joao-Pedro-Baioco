# Verificador de Feriados (Python + Tkinter)

## Objetivo
Criar uma aplicação que:
1. Permite ao usuário escolher um arquivo PDF com datas.
2. Lê as datas do arquivo.
3. Verifica na API pública se cada data é feriado nacional no Brasil.
4. Mostra o resultado na interface gráfica.

---

## Etapas e Commits

### 🟢 Primeiro Commit
- Criação da interface (`tkinter`) com botão para selecionar PDF.

### 🟡 Segundo Commit
- Leitura do PDF (`PyPDF2`) e chamada à API:
  - `https://date.nager.at/api/v3/PublicHolidays/2025/BR`

### 🔵 Terceiro Commit
- Exibição das datas e se são feriados na interface.

---

## Dependências

```bash
pip install PyPDF2 requests
```

---

## Execução
```bash
python 3_interface_final.py
```

Selecione o PDF com datas (exemplo: `Lista_de_datas.pdf`).

---

## Exemplo de Saída

```
2025-04-21: ✅ Feriado
2025-05-24: ❌ Dia comum
2025-09-07: ✅ Feriado
```

---

## Autor
Projeto desenvolvido conforme o enunciado do trabalho.
