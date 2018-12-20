import configparser
import crawler
from pathlib import Path

class Config():
    config = configparser.ConfigParser()
    config_file = '/config/config.ini'
    config_path = Path(crawler.FilePath + config_file)

    def __init__(self):
        self.config.read(self.config_path)

    def get_domain(self):
        return self.config['current']['domain']
    def get_media(self):
        return self.config['current']['media']
    def get_is_jp_pre(self):
        return self.config['current']['is_jp_pre']
    def get_header(self):
        return self.config['config']['header']

    def set_domain(self,val):
        self.config['current']['domain'] = val
        self._save()
    def set_media(self,val):
        self.config['current']['media'] = val
        self._save()
    def set_is_jp_pre(self, val):
        self.config['current']['is_jp_pre'] = val
        self._save()
    def set_header(self, val):
        self.config['config']['header'] = val
        self._save()

    def _save(self):
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)


def main():
    pass
    # print(Path('no_index/text')/"result.txt")
    # a = Config()
    # print(a.get_current())

if __name__ == "__main__":
    main()