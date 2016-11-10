"""Fetch images from MDCS.
"""

import shutil

import json
import requests
import xmltodict
from toolz.curried import first, pipe, map, filter  # pylint: disable=no-member, no-name-in-module, redefined-builtin



def download_file(url, filename):
    """Download a file.

    Args:
      url: where to get the file from
      filename: where to write the file
    """
    request = requests.get(url, stream=True)
    with open(filename, 'wb') as fstream:
        shutil.copyfileobj(request.raw, fstream)
    return filename

def download_images():
    """Download images from the MDCS.
    """
    mdcs_url = "http://129.6.153.123:8000"
    auth = ("dwheeler", "12345")

    parsexml = lambda data: xmltodict.parse(data['content'])['semImage']['imageFile']

    make_dict = lambda data: dict(filename=data['title'] + '.tif', url=parsexml(data))

    funcs = (
        json.loads,
        filter(lambda schema: schema['title'] == "SemImage"),
        first,
        lambda data: json.dumps({"schema" : data['id']}),
        lambda data: requests.post(mdcs_url + "/rest/explore/query-by-example",
                                   {"query" : data},
                                   auth=auth).text,
        json.loads,
        map(make_dict),
        map(lambda data: download_file(data['url'], data['filename'])),
        list
    )

    data = requests.get(mdcs_url + "/rest/templates/select/all", auth=auth).text

    return pipe(data, *funcs)

if __name__ == '__main__':
    print(download_images())
