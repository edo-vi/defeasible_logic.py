class Atom:
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, __other: object) -> bool:
        if not isinstance(__other, Atom):
            return False
        return self.value == __other.value

    def __str__(self):
        if self.value is None:
            return "Atom()"
        return f"Atom({str(self.value)})"
