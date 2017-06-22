class plugin_system:
    def __init__(self):
        self.__plugins = []
        self.__trigger = "!"

    def load_plugin(self, plugin):
        '''Loads a specific plugin'''
        self.__plugins.append(plugin)

    def unload_plugin(self, plugin):
        '''Unloads a specific plugin'''
        pass

    def clear_plugins(self):
        '''Clears the plugin list. DOES NOT
        PROPERLY UNLOAD PLUGINS'''
        self.__plugins = []

    def get_commands(self, plugin=None):
        '''Returns the command triggers
        for all the plugins if no arg is given.'''
        pass

    def get_meta(self, plugin=None):
        '''Returns the MetaData for all
        plugins if no arg is given.'''
        pass


class plugin:
    def __init__(self):
        '''Base Example for a plugin class'''
        self.__command = ["help"]
        self.__meta = {"name": "Help System", "version": "1.0.0", "description": "Lists all of the commands of the bot."}

    def load(self):
        '''Initializes the needed info for a plugin'''
        pass

    def unload(self):
        pass

    def run(self):
        pass
