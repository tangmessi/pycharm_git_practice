import docx as d
from docx import Document
import re
a = Document(r'C:\Users\Administrator\Desktop\1.docx')
for b in a.paragraphs:
    for run in b.runs:
        if "WHAT" in run.text:
            run.text = run.text.replace('WHAT', '唐国毅')
    print (b.text)
    a.save(r'C:\Users\Administrator\Desktop\1.docx')

#with open(r'C:\Users\Administrator\Desktop\1.docx',mode='r',encoding='Unicode') as word:
'''    word = word.read()
    print (word)
    print(word.read())
def read_document():
    document=Document('2.docx')
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            if "唐诗" in run.text:
                run.text=run.text.replace('唐诗','宋词')
    document.save('3.docx')'''