import xml.etree.ElementTree as ET

ns = 'http://www.topografix.com/GPX/1/0'

tree = ET.parse('../data/Adelaide.gpx')
root = tree.getroot()
for wpt in root.iter('{http://www.topografix.com/GPX/1/0}wpt'):
    name = wpt.find('{http://www.topografix.com/GPX/1/0}name').text
    type = wpt.find('{http://www.topografix.com/GPX/1/0}type').text
    print name, type
