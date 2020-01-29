import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

import PyPDF2



NomeProva = input("Digite o nome ou caminho das resposta da prova:")

NomeGabarito = input("Digite o nome ou caminho do Gabarito:")

# Prova

prova_excel = pd.read_excel(NomeProva, sheet_name = 'Sheet1')
prova = {}
for i in prova_excel.index:
    prova[prova_excel['Questao'][i]]= prova_excel['Resposta'][i]

#Gabarito

pdfFileObj = open(NomeGabarito,'rb')
gabarito_pdf = PyPDF2.PdfFileReader(pdfFileObj)

pageGabarito = gabarito_pdf.getPage(0)
textGabarito = pageGabarito.extractText()
GabaritoBruto = textGabarito.split()
GabaritoLinhas = []

for i in range(12):
    if i%2 != 0:
        GabaritoLinhas.append(GabaritoBruto[i])

 
        
GabaritoLista= []

for i in range(len(GabaritoLinhas)):
    for c in GabaritoLinhas[i]:
        GabaritoLista.append(c)

Gabarito = {}
for i in range(len(GabaritoLista)):
    
    Gabarito[i+1] = GabaritoLista[i]


# Analise
    
QuestoesCorretas = prova.items() & Gabarito.items()
QuestoesErradas = prova.items() - Gabarito.items()

QuestoesCorretas = sorted(QuestoesCorretas)
QuestoesErradas = sorted(QuestoesErradas)

numItensCorretos = len(QuestoesCorretas)
numErros = len(prova.items() - Gabarito.items())
NotaLiquida = numItensCorretos - numErros


print("Numero de intens corretos:{}".format(numItensCorretos))
print("Numero de intens errados:{}".format(numErros))
print("Nota Liquida:{}".format(NotaLiquida))

NomeArquivo = NomeProva.split(".")[0] + "ItensErrados.txt" 

File = open(NomeArquivo, "w+")

File.write("\t\t\t\t\t\t\tItens Errados\n")
for item in QuestoesErradas:
    File.write(str(item)+"\n")

File.close()




        






