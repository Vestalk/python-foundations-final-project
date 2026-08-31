class Note:
    def __init__(self, text: str, tags: list[str]) -> None:
        self.text = text
        self.tags = {
            normalized_tag
            for tag in tags
            if (normalized_tag := tag.strip(" ,").lower())
        }

    def __str__(self) -> str:
        tags = ", ".join(sorted(self.tags))
        return f"{self.text} [{tags}]"
