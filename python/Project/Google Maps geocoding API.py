from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML
api_url='http://maps.googleapis.com/maps/api/geocode/xml?'

address=input('Enter address:')
if len(address)<1:
	address='Warsaw,Polland'
#encoding to UTF-8 and adding to the API URL 
url=api_url+ENCODE({'address':address})

#getting the data
data=OPEN(url).read()
#digging into XML tree
tree=XML.findstring(data)
res=tree.findall('result')
#dig into the XML tree to find 'latitude'
lat=res[0].find('geometry').find('location').find('lat').text
#find longitude
lng=res[0].find('geometry').find('location').find('lng').text

lat=float(lat)
lng=float(lng)
lat_c='S' if lat<0 else 'N'
lng_c='W' if lng<0 else 'E'

#the actual object found by the API
location=res[0].find('formatted_address').text

#The result
print("==>",location,"<==")
print('Latitude:{0:.3f}{1}'.format(abs(lat),lat_c))
print('Longitude:{0:.3f}{1}'.format(abs(lng),lng_c))