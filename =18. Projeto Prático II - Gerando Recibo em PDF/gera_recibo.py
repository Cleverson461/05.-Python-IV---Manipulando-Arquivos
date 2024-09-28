# pip install fpdf
# pip install num2words 
from fpdf import FPDF
from num2words import num2words
from datetime import date


# 1 - Utilização de Variáveis
cliente = input("Informe o nome do cliente\n")
consulta = input("Informe o tipo da consulta\n")
vlr = input("Informe o valor da consulta\n")
vlr_msg = f"{vlr} reais"
vlr_extenso = num2words(float(vlr), lang='pt-br')
vlr_extenso_msg = f"{vlr_extenso} reais"
data = date.today()
#formata_data = data.strftime('%d/%m/%Y')
#print(formata_data)
dia = data.day
mes = data.month
ano = data.year

# 2 - Recibo
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', "", 20)
pdf.image("dados/rec.jpg", x=0, y=0)
pdf.text(162, 45, vlr_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, vlr_extenso_msg)
pdf.text(80, 135, consulta)
pdf.set_text_color(255,255,255)   
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))

name_archive = f"{cliente.strip()}_{dia}_{mes}_{ano}"
pdf.output(f'{name_archive}.pdf')

print("Recibo gerado com sucesso!")