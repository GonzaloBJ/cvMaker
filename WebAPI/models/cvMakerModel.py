class CVTemplate:
    name: str
    rootPath:str
    htmlPath: str
    stylePath: str
    colorSchemePath: str
    description: str

    def __init__(self, name: str, rootPath:str, htmlPath: str, stylePath: str, colorSchemePath: str, description: str) -> None:
        self.name = name
        self.rootPath = rootPath
        self.htmlPath = htmlPath
        self.stylePath = stylePath
        self.colorSchemePath = colorSchemePath
        self.description = description
