
from mytest.printing import printing


import jieba

import docx

doc = docx.Document()
doc.add_paragraph('come on')
doc.save('learning.docx')
print(globals())