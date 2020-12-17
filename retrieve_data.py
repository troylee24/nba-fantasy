import requests

def retrieve_xml(file, url):
    response = requests.get(url)
    with open(file, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    retrieve_xml(file='data/rankings.xml', url='https://www.fantasybasketballnerd.com/service/draft-rankings')
    retrieve_xml(file='data/projections.xml', url='https://www.fantasybasketballnerd.com/service/draft-projections')