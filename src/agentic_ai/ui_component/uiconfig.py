from configparser import ConfigParser

class Config:
    def __init__(self, config_file='./src/agentic_ai/ui_component/uiconfigfile.ini'):
        self.uiconfig = ConfigParser()
        self.uiconfig.read(config_file)
    def get_pagetitle(self):
        return self.uiconfig["DEFAULT"].get("PAGE_TITLE")
    def get_platform_options(self):
        return self.uiconfig["DEFAULT"].get("PLATFORM_OPTIONS").split(", ")
    def get_usecase_options(self):
        return self.uiconfig["DEFAULT"].get("USE_CASE_OPTIONS").split(", ")
    def get_groq_model_options(self):
        return self.uiconfig["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")