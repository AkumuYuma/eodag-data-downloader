from ruamel import yaml
import os

class YamlUtilities():
    """Class utilities static methods to interact with yaml.
    """
    
    @staticmethod
    def load_yaml_file(file_path: str) -> dict: 
        """Parses a yaml file and returns it into a dictorary. 
        If it fails to open the file, it will return None

        Args:
            file_path (str): The path of the yaml file

        Returns:
            dict: The parsed yaml file or None if an error occurred in opening the file
        """
        try: 
            with open(file_path, "r") as f: 
                yaml = YamlUtilities.init_custom_yaml_with_null_representer()
                return yaml.load(f.read())
        except Exception: 
            return None 
    
    @staticmethod
    def dump_dict_into_yaml(yaml_dict: dict, file_path: str) -> None: 
        """Writes the yaml file from the dict.

        Args:
            yaml_dict (dict): The dict to convert in yaml 
            file_path (str): The yaml file path 
        """
        yaml = YamlUtilities.init_custom_yaml_with_null_representer()
        with open(file_path, "w") as config_file_stream: 
            yaml.dump(yaml_dict, config_file_stream)
            
    
    @staticmethod
    def init_custom_yaml_with_null_representer() -> yaml.YAML: 
        """Creates and returns an instance of YAML interface with the custom null representer 
        The chosen null representer represents the empty yaml fields with the empty string rather than "null". 

        Returns:
            yaml.YAML: The initialized yaml interface
        """
        my_represent_none = NullRepresenter()
        _custom_yaml = yaml.YAML() 
        _custom_yaml.representer.add_representer(type(None), my_represent_none)
        return _custom_yaml
    
    @staticmethod
    def get_present_file_path() -> str: 
        """Returns the path of the present file

        Returns:
            str: the path of the present file
        """
        return os.path.dirname(os.path.realpath(__file__))
    

class NullRepresenter:
    """Class to represent the empty string when parsing empty yaml fields. 
    If you don't use this, the empty fields will be filled with "null" and I don't like it :-D 
    """
    def __init__(self):
        self.count = 0
    def __call__(self, repr, data):
        ret_val = repr.represent_scalar(u'tag:yaml.org,2002:null', 
                u'null' if self.count == 0 else u'')
        self.count += 1
        return ret_val



if __name__=="__main__":
    print(YamlUtilities.load_yaml_file("./eodag-config/eodag.yml"))