from lxml import etree

tree = etree.parse('Shabalina_1.xml')
root = tree.getroot()

for element in tree.iter('patient'):
    element.text =u'Bolnoy'

for element in root.iter('hospital'):
    newattr = element.attrib
    if newattr:
        newattr["number"] = "03"

output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('Shabalina_2.xml', 'w')
f1.write(output)
print(output)
f1.close()
