from src.Settings import Settings
from src.EodagPlugin import EodagPlugin
import sys 


usage_string = """This is a script to download satellite image data from different providers. 
Usage: $ python downloader.py <query>. 
The query can be passed both from a json file passing the path of the file and directly as through the command line like this '{}'.
To get an example of how the query should be structured give a look to the sample-query.json file in this folder. 
Bye
"""

if __name__=="__main__":
    if len(sys.argv) != 2: 
        print(usage_string)
        exit(1)
    
    eodagPlugin = EodagPlugin(Settings(sys.argv[1])) 
    search_results = eodagPlugin.search_with_current_settings()
    for product in search_results: 
        eodagPlugin.download_product(product)