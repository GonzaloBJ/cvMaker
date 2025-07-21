class Template:
    name: str
    html_path: str
    style_path: str

    def __init__(self, name: str, html_path: str, style_path: str) -> None:
        self.name = name
        self.html_path = html_path
        self.style_path = style_path
