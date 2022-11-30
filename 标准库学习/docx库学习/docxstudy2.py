from docx import Document
from mytest.printing import printing
doc = Document()

name = [i for i in range(100)]
p1 = doc.add_paragraph('this is the first added paragraph' + str(name).strip('[').strip(']'))
p0 = p1.insert_paragraph_before('this is the later inserted paragraph')
doc.save('学习docx.docx')