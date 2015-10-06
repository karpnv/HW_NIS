__author__ = 'admin'
from lxml import etree
tree = etree.parse('Zoteeva.xml')
root1 = tree.getroot()

for element in root1.iter('brend'):
    attrib_val = element.get('brendname')
    attribute_list = attrib_val.split(',')

    for attrib in attribute_list:
        sub_elem = etree.SubElement(element, 'availability')
        sub_elem.text = attrib
        print('availability = '+attrib)

txt = etree.tostring(root1, pretty_print=True, encoding='UTF-8')
f = open('Zoteeva_2.xml','w')
f.write(txt)
f.close()
