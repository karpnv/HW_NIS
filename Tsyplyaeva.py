from lxml import etree

tree = etree.parse('usenko.xml')
root = tree.getroot()

print root.tag

for el in root:
    for sub_el in el.iter('person'):
        sub_el.set('age', 'unknown')


shop = root.find('shopping_list')
shop.remove(shop.find('note'))
for el in shop.find('list'):
    for attribute in el.attrib.keys():
        if attribute=='unit':
            del el.attrib[attribute]


for el in root.iter('doctor_recipe'):
    for sub_el in el.iter('next_date'):
        sub_el.text = "NEVER COME AGAIN"


Test_El = etree.SubElement(root, "Just_a_test_element")
Test_SubElement = etree.SubElement(Test_El, "test_sub", property = "test_property")
Test_El.text = "TESTING LXML"
root.insert(0, Test_El)

    
        
txt = etree.tostring(root, pretty_print=True)
#print txt.decode()
f = open('usenko_update.xml', 'w')
f.write(txt.decode())
f.close()
