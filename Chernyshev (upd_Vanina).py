__author__ = 'chernyshev'

from lxml import etree
tree = etree.parse('Vanina.xml')
root1 = tree.getroot()

for element in tree.iter('release_date'):
	element.text="Date and platform"

for element in tree.iter('score'):
	score = "please estimate it on our website"
	element.text = score

output=etree.tostring(root1, pretty_print=True)
print(output.decode().encode())
f = open('upd_Vanina.xml', 'w')
f.write(output.decode())
f.close()
