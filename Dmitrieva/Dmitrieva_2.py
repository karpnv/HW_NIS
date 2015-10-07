import lxml
from lxml import etree

tree = etree.parse('Kozlova_1.xml')
etree.strip_elements(tree, 'eval', with_tail=False) #удаляем элемент с оценкой фильма и его содержимое
r = etree.tostring(tree, encoding='utf-8')
f = open('Kozlova_2.xml', 'w')
f.write(r.decode())
f.close()
