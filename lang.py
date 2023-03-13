import re, os, json

_language_dictionary : dict[str, str] = {}

def normalize(lang_dict : dict) -> dict[str, str]:
    output_dict = {}

    def normalize_item(item : dict | str, lang_code : str = ''):
        if type(item) is dict:
            for key in item:
                normalize_item(item[key], f'{lang_code}{key}.')
        else:
            output_dict[lang_code[:-1]] = item
    
    normalize_item(lang_dict)
    return output_dict

def load_lang(lang : str):
    global _language_dictionary
    if f'{lang}.json' in os.listdir('./res/lang'):
        with open(f'./res/lang/{lang}.json', 'r', encoding='UTF-8') as json_file:
            _language_dictionary = normalize(json.load(json_file))
    else:
        raise ValueError(f'Language "{lang}" does not have lang file and cannot be loaded')

def lang(text : str):
    lang_codes = (word for word in re.findall(re.escape('{') + r'(.*?)' + re.escape('}'), text) if word in _language_dictionary)
    output = text
    for word in lang_codes:
        output = output.replace(f'{{{word}}}', _language_dictionary[word], 1)
    return output