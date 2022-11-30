n1 = 43432
n2 = 234.24234
s1 = 'I love you forever'
s2 = '月上柳梢头，，人约黄昏后，，不见去年人，，泪湿沾春袖'
formater = 'z'
con = '^'
print('{0:{1}{2}100.30}'.format(s2, formater, con))
print(f'{s2:{formater}{con}100.30}')

print(f'{n2:-^100,.12%}')
print(f'{n1:-^100o}')
print(f'{n1:-^100b}')

