"""Set initial doc state and backref from state objects to doc"""

class Draft:
    def __init__(self, doc):
        self.doc = doc  # ref. to object holding context

class Moderation:
    def __init__(self, doc):
        self.doc = doc

class Published:
    def __init__(self, doc):
        self.doc = doc


class Document:
    """Object to hold a state (Context)"""

    def __init__(self):
        self.state = Draft(self)  # concrete initial state
