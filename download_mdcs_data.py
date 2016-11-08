"""Fetch images from MDCS.
"""

import json
import requests
import xmltodict


def download_mdcs_data():
    user = "dwheeler"
    password = "12345"
    mdcs_url = "http://129.6.153.123:8000"
    schema_title = 'SemImage'
    url = mdcs_url + "/rest/templates/select/all"

    allSchemas = json.loads(requests.get(url, auth=(user, password)).text)
    schemaIDs = [schema['id'] for schema in allSchemas if schema['title'] == schema_title]

    url = mdcs_url + "/rest/explore/query-by-example"
    query = {"schema" : schemaIDs[0]}
    req_data = {"query" : json.dumps(query)}
    qres = json.loads(requests.post(url, req_data, auth=(user, password)).text)

    imgfile = [data['title'] for data in qres]
    img_urls = [xmltodict.parse(data['content'])['semImage']['imageFile'] for data in qres]

    # for i in range(len(qres)):
    #     imgfile.append(qres[i]['title'])
    #     content = qres[i]['content']
    #     # qdata = DMD.DataModelDict(content)
    #     content_dict = xmltodict.parse(content)
    #     # img_urls.append(qdata.find('imageFile'))
    #     img_urls.append(content_dict['semImage']['imageFile'])


    print("no_images: ",len(img_urls))
    print()
    print(imgfile)
    print()
    print(img_urls)

if __name__ == '__main__':
    download_mdcs_data()
