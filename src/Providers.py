class Provider(): 
    """An encapsulation for eodag provider. 
    :param provider_info: A dictionary containing provider info. It must be made like this: 

    <provider_name>: {
        "priority": <priority of the provider>. Higher value means higher priority. Default: 0, 
        "auth": {
            "credentials": 
                {
                    "ident": <your identity>, 
                    "pass": <your password> 
                }
        }
    
    You can find a list of providers here: https://eodag.readthedocs.io/en/stable/getting_started_guide/providers.html. 
    Also notice that the auth interface may change from provider to provider, it is recommended to always check it in the eodag-default.yml file 
    
    :type provider_info: dict
    """

    def __init__(self, name: str, provider_info: dict) -> None:
        self._name = name
        self._provider_info = provider_info
    
    @property 
    def name(self) -> str: 
        return self._name 
    @property
    def provider_info(self) -> dict: 
        return self._provider_info


class ProviderList():
    """This represents a list of providers. 
    :param providers: This is a collection of providers info. It will be converted into a list. You can access it through the property providerList
    :type providers: dict
    """

    def __init__(self, providers: dict) -> None:
        self._provider_list = []
        for provider_name, provider_info in providers.items():
            self._provider_list.append(Provider(provider_name, provider_info))
    
    @property 
    def provider_list(self) -> list: 
        return self._provider_list