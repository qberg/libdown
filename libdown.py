import argparse
import requests
from bs4 import BeautifulSoup

URL = f"https://libgen.is/search.php"

def search(query,session,url=URL):
    '''
    A method that returns the search results of a query on a given url.
    '''
    payload = {'req':query, 'open':0, 'res':100, 'view':"simple", 'phrase':1, 'column':"def", 'page': 1}
    page = session.get(url, params = payload)  
    print(page.url)



if __name__ == '__main__':
    # Defining the command line arguments.
    parser = argparse.ArgumentParser(description="Download all books from libgen matching a seacrh topic given.")
    parser.add_argument("--query",type=str,required=True,help="Space seperated keywords for topics of search.")

    args = parser.parse_args()
    query = args.query

    # Performing the search on the given query in libgen.
    session = requests.Session()
    search(query,session)


