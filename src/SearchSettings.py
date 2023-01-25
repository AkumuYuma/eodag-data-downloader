class SearchSettings():
    """An encapsulation for the search settings. 

    :param settings: A dictionary containig search settings, it must be made like this: 
    {
    "product_name": <name of the product>: str, 
    "init_time": <starting date (of data ingestion)>. The format is YYYY-MM-DDThh-mm-ss+hh:mm, where the last hh:mm is the time offset. 
    If the offset is not set it is supposed to be in UTC. To leave time offset unset you should write Z 
    (eg.: “1990-11-26”, “1990-11-26T14:30:10.153Z”, “1990-11-26T14:30:10+02:00”): str
    "end_time": <end time (of data ingestion)> the same as init-time
    "geometry": {
        "lonmin": value, "latmin": value
        "lonmax": value, "latmax": value
        } The geometry to search in. 
    }
    :type settings: dict
    """

    def __init__(self, settings: dict): 
        self._product_name = settings["product_name"]
        self._init_time = settings["init_time"]
        self._end_time = settings["end_time"]
        self._geometry = settings["geometry"]
    
    @property
    def product_name(self) -> str:
        return self._product_name
    
    @property 
    def init_time(self) -> str:
        return self._init_time
    
    @property
    def end_time(self) -> str:
        return self._end_time
    
    @property 
    def geometry(self) -> dict: 
        return self._geometry
    
    