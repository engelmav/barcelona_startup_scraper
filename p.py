import json
from pprint import pprint

# pythonify
# curl 'http://w153.bcn.cat/api/es/map_resources' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'X-CSRF-TOKEN: uzHOXrxJo1VPII221yo88P+3wSQftCOiuDFb0PkxtjzzQ0TTHfY6qsY53ByIT8IMkC7qOf5OYNoV0zcVLfRU6Q==' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://w153.bcn.cat/' -H 'Cookie: NG_TRANSLATE_LANG_KEY=%22en%22; _gat=1; _bcn_startup_map_session=VXgxa29ack1ub0xZTzNuUFZ2SHJlMTR3S2V5QzNoMXhObm8vRXVFRyttd2R2RUFTWkNENEE3ODdaVWphSk92YkxmNjBjcVAzZkhDTEVMN3FvMVNxL2lMdERwRXR0SDl2eW9ycjNtOWM5RDVKRVZtN0tMSkNmVzZkY25kVW1pdWtQV2JCSVRRRFlzS3VMNGZMcjBzVFBlODUxTUxmb3MyUGQybzc4UEEvQmE4SFVtR0ljVno1Rm5OQlJCUm1oS1ZTLS1sWHBjdGc3bUFFY2lCS0pxQVJOWWRRPT0%3D--a2a950456cab3582ba747cf6cda5869992184b6a; _ga=GA1.2.2025112129.1449091375' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed

with open('/Users/vengelmann/bcn_startup_json.json') as jf:
        data = json.load(jf)

categories = data['categories']


def get_cat_from_id(id):
    for cat in categories:
        if cat['id'] == id:
            return cat['title']


for rec in data['map_resources']:
    desc = rec['description_preview'] or "No description"
    print ("%s [%s - %s]") % (rec['title'], rec['typology'], desc)
    for cat_id in rec['category_ids']:
        print "\t%s" % get_cat_from_id(int(cat_id))
