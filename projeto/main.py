"""Ler as notas técnicas dos projetos dos alunos de cada curso e de cada série, 
digitadas pelos professores em planilha excel e exibir como foram geradas 
as médias de AT bimestrais em páginas web (arquivo .HTML apenas) para cada aluno.
PODENDO VARIAR QUANTIDADES DE DISCIPLINAS E NOMES DAS MESMAS. 
Logicamente a quantidade de alunos varia
de turma para turma.

Cada planilha de notas está criada a partir da primeira célula de um arquivo (pasta) excel. Vale dizer
que as os nomes de alunos de cada turma de uma determinada série de um curso podem estar
misturados dentro de uma mesma planilha. (Ex: 1°K e 1°B pro curso de ADM)
Seu programa deve ler todos os dados de CADA ALUNO e criar uma página web individual com os dados
de AT deste aluno. O nome de cada arquivo html para cada aluno deve ser o número da sua matrícula.
O aluno deve visualizar todos os dados referentes as notas de cada disciplina e a média técnica gerada.
Destaque as notas abaixo de 6,0 em vermelhas e a partir de 6,0 em azuis. Use vermelho e azul para
destacar a média AT FINAL. ATENÇÃO PODE ACONTECER DE ALGUM PROFESSOR NÃO TER
INFORMADO NOTA, OU ALUNO NÃO TER APRESENTADO PROJETO DE UMA OU MAIS DISCIPLINAS;
PARA ESTE CASO, APRESENTE “NÃO INFORMADA” COMO NOTA.

MOSTRE NA TELA PARA O USUÁRIO, EM FORMATO DE TABELA (PRETTYTABLE), individualizadas para
cada aluno os dados de suas notas e média AT, OBEDECENDO O FORMATO MOSTRADO NA FIGURA 1.
Esta exibição deve ser feita de acordo com a ordem de digitação dos dados na planilha excel. Mostre
antes de cada tabela exibida o número da linha em que o aluno que se encontra na planilha excel.
Ao exibir as notas na página web, o aluno poderá clicar num botão para gerar um arquivo pdf com os
dados visualizados na página. A geração do arquivo pdf deve ser parte do programa python que for
criado.
A criatividade, capricho e conhecimento da programação deste projeto será avaliada criteriosamente,
de forma que os melhores resultados terão notas melhores. """

# main.py
# Projeto POOI - 4º Bimestre
# Leitura de planilha Excel e geração de HTML + PDF por aluno

import os
import pandas as pd
from prettytable import PrettyTable
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# registra a fonte Arial para o reportlab
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

# função para gerar o PDF de um aluno específico
def gerar_pdf(dados_aluno, materias, caminho_pdf):
    pdf = canvas.Canvas(caminho_pdf)
    pdf.setTitle("Relatório de Notas do Aluno")
    pdf.setFont("Arial", 14)
    pdf.drawString(50, 800, "Relatório de Notas do Aluno")
    pdf.setFont("Arial", 12)

    y = 770
    for chave, valor in dados_aluno.items():
        texto = str(chave) + ": " + str(valor)
        pdf.drawString(50, y, texto)
        y -= 20

    pdf.drawString(50, y - 10, "Notas:")
    y -= 30
    for mat in materias:
        valor = dados_aluno.get(mat, "NÃO INFORMADA")
        texto = str(mat) + ": " + str(valor)
        pdf.drawString(70, y, texto)
        y -= 20

    pdf.save()

# função principal
def main():
    # procura automaticamente o arquivo .xlsx na pasta atual
    arquivo_excel = ""
    for arq in os.listdir("."):
        if arq.endswith(".xlsx"):
            arquivo_excel = arq
            break

    if arquivo_excel == "":
        print("Nenhum arquivo .xlsx encontrado na pasta do projeto.")
        return

    # lê o arquivo Excel com pandas
    planilha = pd.read_excel(arquivo_excel)

    # garante que a planilha tenha dados
    if len(planilha) == 0:
        print("A planilha está vazia.")
        return

    # identifica colunas fixas e dinâmicas
    colunas = list(planilha.columns)
    codigo_col = colunas[0]
    aluno_col = colunas[1]
    turma_col = colunas[2]
    materias = colunas[3:-1]
    media_col = colunas[-1]

    # exibe cada aluno no terminal com prettytable
    linha_planilha = 2
    for i in range(len(planilha)):
        print("Linha da planilha:", linha_planilha)
        linha_planilha += 1

        aluno = planilha.iloc[i]
        tabela = PrettyTable()
        tabela.field_names = colunas
        dados_linha = []
        for c in colunas:
            valor = aluno[c]
            if str(valor) == "nan":
                valor = "NÃO INFORMADA"
            dados_linha.append(valor)
        tabela.add_row(dados_linha)
        print(tabela)
        print()

        # gera HTML de cada aluno
        matricula = str(aluno[codigo_col])
        nome_aluno = str(aluno[aluno_col])
        turma = str(aluno[turma_col])
        media_final = str(aluno[media_col])

        caminho_html = os.path.join("arquivos", matricula + ".html")
        html = open(caminho_html, "w", encoding="utf-8")

        html.write("<html><head><meta charset='utf-8'><title>Notas do Aluno</title></head><body>")
        html.write("<h2>Aluno: " + nome_aluno + "</h2>")
        html.write("<p><b>Matrícula:</b> " + matricula + "</p>")
        html.write("<p><b>Turma:</b> " + turma + "</p>")
        html.write("<table border='1' cellpadding='5' cellspacing='0'>")
        html.write("<tr><th>Disciplina</th><th>Nota</th></tr>")

        for mat in materias:
            nota = aluno[mat]
            if str(nota) == "nan":
                nota = "NÃO INFORMADA"
                cor = "black"
            else:
                try:
                    n = float(nota)
                    if n < 6.0:
                        cor = "red"
                    else:
                        cor = "blue"
                except:
                    cor = "black"
            html.write("<tr><td>" + mat + "</td><td style='color:" + cor + "'>" + str(nota) + "</td></tr>")

        # média final
        cor_media = "blue"
        try:
            if float(media_final) < 6.0:
                cor_media = "red"
        except:
            cor_media = "black"

        html.write("<tr><td><b>Média AT3</b></td><td style='color:" + cor_media + "'><b>" + str(media_final) + "</b></td></tr>")
        html.write("</table>")

        # botão gerar PDF
        caminho_pdf = os.path.join("pdfs", matricula + ".html.pdf")
        comando_pdf = "python main.py " + matricula
        html.write("<br><br><form action='../pdfs/" + matricula + ".html.pdf'>")
        html.write("<button type='submit'>Baixar PDF</button>")
        html.write("</form>")

        html.write("</body></html>")
        html.close()

        # gera PDF automático para a pasta pdfs/
        dados_pdf = {codigo_col: matricula, "Aluno": nome_aluno, "Turma": turma}
        for mat in materias:
            valor = aluno[mat]
            if str(valor) == "nan":
                valor = "NÃO INFORMADA"
            dados_pdf[mat] = valor
        dados_pdf["Média AT3"] = media_final
        gerar_pdf(dados_pdf, materias, caminho_pdf)

    print("Arquivos HTML e PDFs gerados com sucesso!")

# executa
if __name__ == "__main__":
    main()
