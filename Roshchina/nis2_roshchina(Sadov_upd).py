from lxml import etree

tree = etree.parse('Sadov_assignment_1.xml')
root1 = tree.getroot()

for element in tree.iter('horsepower'):
	element.text="Power"

for element in root1.iter('car'):
    newattr = element.attrib
    if newattr:
        newattr["num"] = "10"



newtree = etree.tostring(root1, encoding='utf-8')
f = open('nis2_roshchina(Sadov_upd).xml','w')
f.write(newtree.decode())
f.close()
