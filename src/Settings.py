import json
from src.SearchSettings import SearchSettings
from src.SavingSettings import SavingSettings
from src.Providers import ProviderList, Provider
from src.YamlUtilities import YamlUtilities
import os


class Settings():     
    """Class representing Settings for a eodag search. 

    :param settings: If it is a dict, must contain a SearchSettings section, a SavingSattings section and a provider collection. 
    For more info check SavingSettings, SearchSettings and Providers documentation. 
    
    If it a string, it is supposed to be the path to a json of the same structure. 
    """

    # Dict with the current dynamic configuration of the providers
    present_provider_config = None
    # With respect to this source file 
    relative_path_to_default_config_file = "../res/eodag-default.yml"

    def __init__(self, settings) -> None: 
        if type(settings) == str:
            if settings.startswith("{") and settings.endswith("}"): # Settings passed directy in command line
                dict_settings = json.loads(settings)
            else: # Settings passed as json path, try to open the path 
                dict_settings = self.load_settings_from_file(settings)
        elif type(settings) == dict: # Settings passed as dict, just laod in memory  
            dict_settings = settings
        else: 
            raise TypeError("Settings type must be string or dict")

        self.searchSettings = SearchSettings(dict_settings["search-settings"])
        self.savingSettings = SavingSettings(dict_settings["saving-settings"])
        self.providers = ProviderList(dict_settings["providers"])
        self.config_file_path = f"{self.savingSettings.config_path}/eodag.yml"

        # Initializing config 
        # Creating config directory if it doesn't exist
        self.create_config_directory() 
        # Initializing the current provider config with the default settings  
        if Settings.present_provider_config is None: 
            self.initialize_providers_config() 

        # Update providers settings with customized settings from the self.providers infos 
        self.update_providers_info()
    
    @staticmethod
    def get_default_config_dict() -> dict: 
        """Loads the resource with the default providers config and returns it as dict

        Returns:
            dict: default providers config
        """
        dir_path = YamlUtilities.get_present_file_path()
        return YamlUtilities.load_yaml_file(f"{dir_path}/{Settings.relative_path_to_default_config_file}") 

    def load_settings_from_file(self, file_path: str) -> dict: 
        with open(file_path, "r") as settings_file: 
            settings_string = settings_file.read()
            return json.loads(settings_string)
        

    def initialize_providers_config(self) -> None: 
        """Initializes the static variable present_provider_config with the default providers settings """
        Settings.present_provider_config = Settings.get_default_config_dict()
        self.update_config_file_with_present_providers_settings()
    
    def update_config_file_with_present_providers_settings(self) -> None: 
        """Updates the config file with the current info of the providers"""
        YamlUtilities.dump_dict_into_yaml(Settings.present_provider_config, self.config_file_path)
        
    def create_config_directory(self) -> None: 
        """Creates the config directory if it doesn't exist """
        os.system(f"mkdir -p {self.savingSettings.config_path}") # Se non esiste la cartella del config file la creo 

    def update_providers_info(self) -> None: 
        """Updates the current provider configuration (and the config file) with the info in the provider list"""
        for provider in self.providers.provider_list: 
            self.update_provider_info(provider)
    
    def update_provider_info(self, provider: Provider): 
        """Updates the current provider dynamic configuration (and the config file) with the info of the provider

        Args:
            provider (Provider): The provider to get info from 
        """
        for field,value in provider.provider_info.items():
            Settings.present_provider_config[provider.name][field] = value 
        self.update_config_file_with_present_providers_settings()
        


if __name__=="__main__": 
    print(Settings.load_default_config())