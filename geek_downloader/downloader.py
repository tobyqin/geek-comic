import json
import os
from os.path import dirname, join, exists, abspath

import requests

site_name = 'turnoffus'
project_dir = abspath(dirname(dirname(__file__)))
download_dir = join(project_dir, '@download', site_name)
data_file = join(dirname(__file__), '{}.json'.format(site_name))

if not exists(download_dir):
    os.mkdir(download_dir)


def read_data():
    with open(data_file) as f:
        return json.loads(f.read())


def download_data(data):
    for file in data:
        local_file = join(download_dir, file['name'])
        if not exists(local_file):
            print('Download: {}\n=> {}'.format(file['src'], local_file))
            download_image(file['src'], local_file)
        else:
            print('Skip: {}'.format(file['src']))


def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)


data = read_data()
download_data(data)
