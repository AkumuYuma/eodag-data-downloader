from src.Settings import Settings
from eodag import EODataAccessGateway, EOProduct
import os 

class EodagPlugin():
    """A class representing an interfact to communicate with eodag library.  
    :param settings: A settings object containing preferencies for eodag 
    :type settins: Settings
    """

    def __init__(self, settings: Settings) -> None:
        self.product_name = settings.searchSettings.product_name
        self.init_time = settings.searchSettings.init_time
        self.finish_time = settings.searchSettings.end_time
        self.geom = settings.searchSettings.geometry
        self.base_path = settings.savingSettings.base_path
        self.extension = settings.savingSettings.ext
        self.dag = EODataAccessGateway(settings.config_file_path)
        
    def search_with_current_settings(self): 
        """This triggers the research with current settings

        Returns:
            list(EOProduct): List of Products matching the search criteria 
        """
        return self.dag.search(
            productType=self.product_name, 
            start=self.init_time, 
            end=self.finish_time, 
            geom=self.geom 
        )[0]
    
    def download_product(self, product: EOProduct) -> str: 
        """Download the quicklook (the image) for the selected product. 
        For the data access and download, it uses the providers settings contained in the Settings object

        Args:
            product (EOProduct): The product to download 

        Returns:
            str: The path where the image was saved
        """
        full_path = f"{self.base_path}/{product.provider}"
        if not os.path.isdir(full_path): 
            os.system(f"mkdir {full_path} -p")

        product_id = product.properties["id"]
        file_name = f"{product_id}.{self.extension}"

        product.get_quicklook(file_name, full_path)