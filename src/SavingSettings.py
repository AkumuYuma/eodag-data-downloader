from src.YamlUtilities import YamlUtilities

class SavingSettings():
    """An encapsulation for saving options. 
    
    :param settings: A dictionary containing saving settings. It must be made like this: 
    {
        "base-path": this is the path where to save downloaded data. It must be relative to the project folder. 
        Default: <project_dir>/data
         
        "ext": The extension of the downloaded images (usually should be leave to png)
        Default: png 
        
        "config-path": this is the path where to save configurations data. It must be relative to the project folder 
        Default: <project_dir>/eodag-config
    }
    :type settings: dict
    """
    def __init__(self, settings: dict) -> None:
        present_file_path = YamlUtilities.get_present_file_path()
        
        config_base_path = settings.get('base-path', "")
        if config_base_path == "":
            config_base_path = "./data"
        self._base_path = f"{present_file_path}/../{config_base_path}"

        config_file_ext = settings.get('ext', "")
        if config_file_ext == "":
            config_file_ext = "png"
        self._ext = config_file_ext

        config_config_path = settings.get('config-path', "")
        if config_config_path == "":
            config_config_path = "./eodag-config"
        self._config_path = f"{present_file_path}/../{config_config_path}"
    
    @property
    def base_path(self) -> str: 
        return self._base_path
    @property 
    def ext(self) -> str:
        return self._ext
    @property
    def config_path(self) -> str: 
        return self._config_path
