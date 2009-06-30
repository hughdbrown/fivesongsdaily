from fivesongsdaily.settings import LICENSE_KEY, ASSOICATE

def format_param(params):
    args = ["%s=%s" % (key, ",".join(v for v in value)) for key, value in params.items() if type(value) is list ] + \
        ["%s=%s" % (key, value.replace(" ", "+")) for key, value in params.items() if not (type(value) is list) ]
    return "&".join(arg for arg in args)

def AWSUrl(title):
    params = { 'Service': 'AWSECommerceService', 'AWSAccessKeyId': LICENSE_KEY, 'AssociateTag': ASSOCIATE, 'ResponseGroup': ['Images','ItemAttributes'], 'Operation': 'ItemSearch', 'ItemSearch.Shared.SearchIndex': 'Music', 'Title': title}
    url = "http://ecs.amazonaws.com/onca/xml?" + format_param(params)
    print url
    return url

def getXML(url):
    import urllib2
    return urllib2.urlopen(url).read()

def getAsinAndUrlFromXML(xml):
    from xml.dom import minidom
    xmldoc = minidom.parseString(xml)

    result = []    
    e = xmldoc.getElementsByTagName("ItemSearchResponse")[0]
    items = e.getElementsByTagName("Items")[0]
    for item in items.getElementsByTagName("Item") :
        medium_image = item.getElementsByTagName("MediumImage")[0]
        attributes = item.getElementsByTagName("ItemAttributes")[0];
        url = medium_image.getElementsByTagName("URL");
        artist = attributes.getElementsByTagName("Artist");
        title = attributes.getElementsByTagName("Title");
        asin = item.getElementsByTagName("ASIN");
        r  = [(x[0].childNodes[0].nodeValue if x else "") for x in (asin, url, artist, title)]
        result.append(r)
    return result

def getCoverArt(title) :
    try :
        url = AWSUrl(title)
        xml = getXML(url)
        return getAsinAndUrlFromXML(xml)
    except Exception, err:
        print err
        return []

if __name__ == "__main__" :
    import sys
    from pprint import pprint
    for title in sys.argv[1:]:
        print title
        for c in getCoverArt(title):
            print "\t", c

    
    