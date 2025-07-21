class CVTemplate:
    name: str
    htmlPath: str
    stylePath: str
    description: str

    def __init__(self, name: str, htmlPath: str, stylePath: str, description: str) -> None:
        self.name = name
        self.htmlPath = htmlPath
        self.stylePath = stylePath
        self.description = description
