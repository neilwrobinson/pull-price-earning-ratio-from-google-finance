#!/usr/bin/python
#grab_pe_ratio.py
#Use freely in any manner you like; I assume no liable for any damages that you may cause. :)
#Written 2015 by Neil Robinson



from lxml import html
import requests

#page = requests.get('http://www.google.com/finance?q=TSE%3AREI.UN')
page = requests.get('http://www.google.com/finance?q=RY')
tree = html.fromstring(page.content)

pe_ratio_d = tree.xpath('//td[@class="key"]/text()')
pe_ratio = tree.xpath('//td[@class="val"]/text()')

print 'PE Ratio: ', pe_ratio_d[5]
print 'PE Ratio: ', pe_ratio[5]

print 'V*: ', float(pe_ratio[5])*((8.5+2*.1))

#This is the HTML from Google's website that is used to "grab" the PE ratio.
#<td class="key"
#          data-snapfield="pe_ratio">P/E
#</td>
#<td class="val">15.89
