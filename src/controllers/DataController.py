from controllers.BaseController import BaseController
from helpers.config import Settings, get_settings

class DataController(BaseController):
    def __init__(self, settings:Settings = get_settings()):
        super().__init__(settings)