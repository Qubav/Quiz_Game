
class Question:
    """Class that is used to build objects that store question contents and answer as attributes."""

    def __init__(self, text: str, answer:str) -> None:
        self.text = text
        self.answer = answer