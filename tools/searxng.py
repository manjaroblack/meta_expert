import os
import json
import requests
from langchain_community.utilities import SearxSearchWrapper
from config.load_configs import load_config

def format_results(organic_results: str) -> str:
    result_strings = []
    for result in organic_results:
        title = result.get('title', 'No Title')
        link = result.get('link', '#')
        snippet = result.get('snippet', 'No snippet available.')
        result_strings.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
    
    return '\n'.join(result_strings)

def searxng_search(query: str) -> str:
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    load_config(config_path)
    searxng_search = SearxSearchWrapper(searx_host=os.environ['SEARXNG_URL'])
    
    results = searxng_search.results(query=query, num_results=20)
    
    return format_results(results)

# Example usage
if __name__ == "__main__":
    search_query = "Python programming"
    results = searxng_search(search_query)
    print(results)