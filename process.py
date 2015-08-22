import requests, re, logging
from pprint import pprint
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.DEBUG)

#<tr>
#    <td><a href="/fishboat/fish/recreational/lakes/travis/">TRAVIS</a>
#    </td>
#<td> Water murky; 87&ndash;91 degrees; 11.86&#39; low. Black bass are fair on Rat&ndash;L&ndash;Traps and spinnerbaits. Striped bass are slow. White bass are fair on Li&#39;l Fishies. Crappie are good on minnows and pink tube jigs. Channel and blue catfish are fair on shrimp and liver. Yellow catfish are slow.</td>
#</tr>

county = "TRAVIS"
region = "HC"


response = requests.get("http://tpwd.texas.gov/fishboat/fish/action/reptmap.php?EcoRegion={}".format(region))
#p = re.compile('\<a\ href=\"\/fishboat\/fish\/recreational\/lakes\/{}\/\"\{}\<\/a\>\s*\s*\<\/td\>\s*<td\>(.*)\s*\<\/tr\>'.format(county, county), re.IGNORECASE)
#pprint(response.text)
#m = p.match(response.text)
#pprint(m)


soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all(href=re.compile(county))
pprint(links)
