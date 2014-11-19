from bs4 import BeautifulSoup
import urllib.request
import json
import re

def get_html(url):
    f = urllib.request.urlopen(url)
    return f.read()

def parse_properties(soup):
    properties = []
    rows = soup.find_all('tr')
    for row in rows:
        column1 = row.contents[0]
        for child in column1.children:
            value = child.string
            if re.search('[a-z]', value[0], re.IGNORECASE) and value != "Property":
                properties.append(child.string)
    return properties

def write_file(save_obj):
    with open("./properties_all.json", "w") as f:
        json.dump(save_obj, f, ensure_ascii=False, indent=4)

def main():
    save_obj = {}
    save_list = []
    sep_list = 0

    sites = json.loads(open("./describe_urls.json", "r").read())
    for prop in sites['properties']:
        html_doc = get_html(prop['property']['href'])
        properties = parse_properties(BeautifulSoup(html_doc))
        if sep_list:
            save_list.append(properties)
        else:
            save_list.extend(properties)

            save_obj['properties'] = save_list
            write_file(save_obj)

if __name__ == '__main__':
    main()
    print("done")
