import xml.etree.ElementTree as et
# tree=et.parse("stu.xml")
# root=tree.getroot()

# for student in root.findall("student"):
#     id=student.find("id").text
#     name=student.find("name").text
#     marks= student.find("marks").text
#     print(id,name,marks)

import xml.etree.ElementTree as et

# create root FIRST
root = et.Element("friends")

# friend 1
frnd1 = et.SubElement(root, "friend")
et.SubElement(frnd1, "name").text = "gowtham"
et.SubElement(frnd1, "phone").text = "7095602721"

# friend 2
frnd2 = et.SubElement(root, "friend")
et.SubElement(frnd2, "name").text = "varsha"
et.SubElement(frnd2, "phone").text = "6380339470"

# write to file
tree = et.ElementTree(root)
tree.write("frnds.xml", encoding="utf-8", xml_declaration=True)


tree = et.parse("frnds.xml")
root = tree.getroot()

for friend in root.findall("friend"):
    name = friend.find("name").text
    phone = friend.find("phone").text
    print(name, phone)