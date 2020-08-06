#!/usr/bin/env python
# A script to query hashes.org.... When it comes back online 
# You should send them $$ at https://www.patreon.com/posts/40082183

import requests
import sys
import json
from pygments import highlight, lexers, formatters

banner='''
###    ###          ##         #####
###    ###         ## #        #####
###    ###        ##  ##        ###
###    ###       ##    ##       ###
######          #####            #
###    ###     ######### #       
###    ###    ##         ##      #
###    ###   ###         ###    ###
###    ###  #####       #####    #
'''

print(banner)
print("A Query For The Hashes.org API")

api_key = '[REPLACE THIS SHOUTING WITH YOUR API KEY]'
hash_2check = sys.argv[1]
url = 'https://hashes.org/api.php?key=' + api_key + '&query=' + hash_2check

res = requests.get(url)
print('Response Status:',res.status_code)

color_json_bytes = highlight(str(res.content, 'utf-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
raw_text_out = res.text
data_2_dict = json.loads(raw_text_out)

print("hashes.org data:")
print(color_json_bytes)
