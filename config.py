import json, os

_config : dict[str, str] = {}

def config(item : str):
    if item not in _config:
        raise ValueError(f'"{item}" not in config. Is config loaded?')
    
    return _config[item]

def load_config():
    if not os.path.exists('./config.json'):
        raise RuntimeError('config.json missing')
    
    with open('./config.json', 'r', encoding='UTF-8') as config_file:
        global _config
        _config = json.load(config_file)