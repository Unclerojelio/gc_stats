# python save.py

import xml.etree.ElementTree as ET
tree = ET.parse('../data/Adelaide.gpx')
root = tree.getroot()

ns = {'gpx': 'http://www.topografix.com/GPX/1/0',
      'gs': 'http://www.groundspeak.com/cache/1/0'}

def num_caches():
    caches = []
    for wpt in root.findall('gpx:wpt', ns):
        cache = wpt.find('gpx:type', ns).text
        caches.append(cache)
    return len(caches)

def print_types():

    traditional_caches = []
    multi_caches = []
    event_caches = []
    letterbox_caches = []
    earth_caches = []
    event_caches = []
    virtual_caches = []
    wherigo_caches = []
    webcam_caches = []
    cito_caches = []
    other_caches = []
    
    for wpt in root.findall('gpx:wpt', ns):
        name = wpt.find('gpx:name', ns).text
        type = wpt.find('gpx:type', ns).text
        if type == 'Geocache|Traditional Cache':
            traditional_caches.append(name)
        elif type == 'Geocache|Letterbox Hybrid':
            letterbox_caches.append(name)
        elif type == 'Geocache|Multi-cache':
            multi_caches.append(name)
        elif type == 'Geocache|Earthcache':
            earth_caches.append(name)
        elif type == 'Geocache|Event Cache':
            event_caches.append(name)
        elif type == 'Geocache|Virtual Cache':
            virtual_caches.append(name)
        elif type == 'Geocache|Wherigo Cache':
            wherigo_caches.append(name)
        elif type == 'Geocache|Webcam Cache':
            webcam_caches.append(name)
        elif type == 'Geocache|Cache In Trash Out Event':
            cito_caches.append(name)
        else:
            other_caches.append(name)
    
    print 'Traditional Caches: ' + str(len(traditional_caches))
    print 'Letterbox Caches: ' + str(len(letterbox_caches))
    print 'Multi Caches: ' + str(len(multi_caches))
    print 'Earth Caches: ' + str(len(earth_caches))
    print 'Event Caches: ' + str(len(event_caches))
    print 'Virtual Caches: ' + str(len(virtual_caches))
    print 'Whereigo Caches: ' + str(len(wherigo_caches))
    print 'Webcam Caches: ' + str(len(webcam_caches))
    print 'CITO Caches: ' + str(len(cito_caches))
    print 'Other Caches: ' + str(len(other_caches))

    print other_caches


def print_list():
    size = ''
    for wpt in root.findall('gpx:wpt', ns):
        number = wpt.find('gpx:name', ns).text
        type = wpt.find('gpx:type', ns).text
        name = wpt.find('gpx:urlname', ns).text
        cache = wpt.find('gs:cache', ns)
        size = cache.find('gs:container', ns).text
        

        print number + '\t' + name + '\t' + type.split('|')[1] + '\t' + size
        

#print num_caches()
print_types()
#print_list()
