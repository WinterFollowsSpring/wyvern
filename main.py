from config import load_config, config
from lang import load_lang, lang
from unit import Feet

if __name__ == '__main__':
    load_config()
    load_lang(config('lang'))

    # TODO the rest of the program