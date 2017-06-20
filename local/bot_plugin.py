class Plugin:
    def __init__(self, name):
        self.__name = name

    def load_plugin(self):
        print("Plugin Loaded")

    def unload_plugin(self):
        print("Plugin Unloaded")
        return
