"""Fetch images from MDCS.
"""

import json
import requests
import xmltodict
from toolz.curried import pipe, map, filter, first
import shutil


def download_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fstream:
        shutil.copyfileobj(r.raw, fstream)
    return filename

def download_images():
    mdcs_url = "http://129.6.153.123:8000"
    auth=("dwheeler", "12345")

    data = requests.get(mdcs_url + "/rest/templates/select/all", auth=auth).text

    parsexml = lambda data: xmltodict.parse(data['content'])['semImage']['imageFile']

    make_dict = lambda data: dict(filename=data['title'] + '.tif', url=parsexml(data))

    funcs = (
        json.loads,
        filter(lambda schema: schema['title'] == "SemImage"),
        first,
        lambda data: json.dumps({"schema" : data['id']}),
        lambda data: requests.post(mdcs_url + "/rest/explore/query-by-example", {"query" : data}, auth=auth).text,
        json.loads,
        map(make_dict),
        map(lambda data: download_file(data['url'], data['filename'])),
        list
    )

    return pipe(data, *funcs)

if __name__ == '__main__':
    print(download_images())
