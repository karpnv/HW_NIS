from lxml import etree
tree = etree.parse('nis1_roshchina.xml')
root1 = tree.getroot()

for element in root1.iter('part'):
    attributes = element.attrib
    if attributes:
        attributes["quality"] = "good"

newfile = etree.tostring(root1, pretty_print=True)
a = open('nis1_roshchina_upd.xml','w')
a.write(newfile.decode())
a.close()
