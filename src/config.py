import configparser, atexit

CONFIG_FILE = "wannago.conf"

class Config(configparser.ConfigParser):
    def __init__(self, config_file=CONFIG_FILE):
        super().__init__()
        self.read(config_file)
        self.config_file = config_file
        atexit.register(Config.writeConfig, self)

    def writeConfig(self):
        with open(self.config_file, 'w') as file:
            self.write(file)

    def setConfig(self, section, name, value, overwrite=True):
        if not section in self:
            self[section] = {}
        if not name in self[section] or overwrite:
            self[section][name] = value
        return value

    def getConfig(self, section, name, defaultValue=None, writeIfMissing=False):
        if not section in self or not name in self[section]:
            if writeIfMissing and defaultValue is not None:
                self.setConfig(section, name, defaultValue)
            return defaultValue
        return self[section][name]

    def setToken(self, token):
        self.setConfig('Navitia', 'Token', token)

    def getToken(self):
        return self.getConfig('Navitia', 'Token')

defaultConfig = Config()
