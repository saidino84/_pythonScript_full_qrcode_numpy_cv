import os
os.system("clear")
os.chdir(os.path.dirname(__file__))
import PyPDF2 as pdfer

reader =pdfer.PdfFileReader('carta.pdf')


print(reader.documentInfo)
print(reader.getPage(0).extractText())

writer=pdfer.PdfFileWriter()

my_page=reader.getPage(0)
writer.addPage(my_page)

output_file="files_we_want.pdf"
with open(output_file,'wb') as out:
    writer.write(out)
