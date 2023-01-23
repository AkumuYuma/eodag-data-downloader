
# search_results, total_count = dag.search(
#     productType="S2_MSI_L2A_MAJA", # disponibile su theia
#     start="2021-03-01",
#     end="2021-03-31",
#     geom={"lonmin": 1, "latmin": 43, "lonmax": 2, "latmax": 44}
# )

# search_results, _ = dag.search(
#     productType="S2_MSI_L1C", # Disponibile su copernicus
#     start="2021-03-01",
#     end="2021-03-31",
#     geom={"lonmin": 1, "latmin": 43, "lonmax": 2, "latmax": 44}
# )

from Settings import Settings
from EodagPlugin import EodagPlugin

SAMPLE_INPUT = {
    "search-settings": {
        "product-name": "S2_MSI_L2A_MAJA", 
        "init-time": "2021-03-01", 
        "end-time": "2021-03-31", 
        "geometry": {
            "lonmin": 1, "latmin": 43, 
            "lonmax": 2, "latmax": 44
            }
    }, 
    "saving-settings": {
        "base-path": "./data", # Path relativo alla cartella in cui c'è la cartella di progetto (downloader)
        "ext": "png", 
        "config-path": "./eodag-config" # Path relativo alla cartella in cui c'è la cartella di progetto (downloader)
    }, 
    "providers": {
        "theia": {
            "priority": 2, 
            "auth": {
                "credentials": 
                    {
                        "ident": "change-me", 
                        "pass": "change-me"
                    }
            }
        }, 
        "peps": {
            "priority": 0, 
            "auth": {
                "credentials": {
                    "username": "change-me",
                    "password": "change-me"
                }
            }
        }
    }
}

if __name__=="__main__": 
    # if len(sys.argv) != 7: 
    #     print(usage_string)
    #     sys.exit(1)

    # settings = Settings(sys.argv[1])
    settings = Settings(SAMPLE_INPUT)
    eodagPlugin = EodagPlugin(settings)
    search_results = eodagPlugin.search_with_current_settings()

    # search_result è una tupla in cui il primo valore è un vettore di prodotti, il secondo è un intero che non so che cazzo mi significa
    for product in search_results: 
        pass 

    eodagPlugin.download_product(search_results[3])


    # dag = EODataAccessGateway() 
    # search_results, total_count = dag.search(
    #     productType="S2_MSI_L2A_MAJA", # disponibile su theia
    #     start="2021-03-01",
    #     end="2021-03-31",
    #     geom={"lonmin": 1, "latmin": 43, "lonmax": 2, "latmax": 44}
    # )
    # print(search_results)

    # search_results[0].get_quicklook("stocazzo.jpg")
    