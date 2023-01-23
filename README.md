# eodag-data-downloader

This is a repository for a command line tool to download data using eodag library. The tool take one single json file containing all the needed info and settings. In a single place you will write the searching filters (such as Product name, starting and ending sensing date and geometry) as well as providers configurations. 
The downloader will save all the product quicklooks matching the searching criteria from all of the configured providers. The destination folder can be configured from the json too. 

The idea beyond this project is to build an interface for downloading satellite data fitting the needings of cloud authomation. In fact, the input json will be passed through a TOSCA template. 

## Dependencies 
This tool uses ruamel.yaml to access and manage yaml files and (obv) eodag library. 
```bash
$ pip install ruamel.yaml 
$ pip install eodag
```
If you don't want to install dependencies from yourself you can you the [requirements.txt](./requirements.txt) file with 
```bash 
$ pip install -r requirements.txt
```


## Installation 
No need for any installation, just type
```bash
$ python donwloader.py <arguments>
```

## Usage
The goal of this tool is to provide a single json interface to configure, search and download satellite data. The tool takes one command line argument representing the json file. It can be the path of the file, as well a string in json format (surrounded by '' characters). 

The following is an example of query 
 ```json
 {
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
        "base-path": "./data", 
        "ext": "png", 
        "config-path": "./eodag-config" 
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
 ```
 
 The query is diveded into three major parts: "search-settings", "saving-settings" and "providers". 
 * search-settings
 This section contains the actual query, i.e. the name of the product you want do download, the init and end time (This dates are referred to the sensing time of the satellite!) and the geometry to look into. 
 The format of the datetime is YYYY-MM-DDThh-mm-ss+hh:mm, where the last hh:mm is the time offset. If the offset is not set it is supposed to be in UTC. To leave time offset unset you should write Z (eg.: “1990-11-26”, “1990-11-26T14:30:10.153Z”, “1990-11-26T14:30:10+02:00”). 
 The geometry represents a rectangle of latitude and longitude to look into. 
 
 * saving-settings 
 In this section it is possible to choose preferencies on saving pattern of the script. The "base-path" is the location of the downloaded data. This path is intended to be relative to the project directory. The images will be saved in `<project-dir>/<base-path>/<provider-name>/`. The "ext" field is the extension of the downloaded images. The "config-path" is the location of the generated configuration file of eodag. 
 
 * providers
 In this sections you must provide a collection of providers. The structure of the inner object must be the same as the yaml configuration of eodag. THis means that you can modify not only the "priority" and "auth" fields, but any field available in the eodag configuration. Anyway, the images will be downloaded starting from the provider with higher priority value. If a provider has 0 as priority value, it will be skipped.  

 
  ### About the generated eodag configuration file
  [Here](./res/eodag-default.yml) you can find the default configuration file provided by eodag (if you ever used eodag on your machine you will have a copy of this in ~/.config/eodag/). This tool will load the default configuration file and update it with customized providers settings provided in the json input and will force eodag to use the new configuration file (saved in `<confing-path>/eodag.yml`). In this way, after the first use of the script, the config file will be generated and will contain your credentials. Be careful!
