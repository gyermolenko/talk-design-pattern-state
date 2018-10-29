"""Add all states as document attrs"""

class Draft:
    def __init__(self, doc):
        self.doc = doc

class Moderation:
    def __init__(self, doc):
        self.doc = doc

class Published:
    def __init__(self, doc):
        self.doc = doc


class Document:
    """Object to hold a state (Context)"""

    def __init__(self):
        self.draft = Draft(self)
        self.moderation = Moderation(self)
        self.published = Published(self)
        self.state = self.draft
