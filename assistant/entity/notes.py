

class Note:
    def __init__(self, text: str, tags: list[str]):
        self.text = text
        self.tags = set(tag.lower() for tag in tags)

    def __str__(self):
        tags = " ,".join(self.tags)
        return f"{self.text} [{tags}]"
