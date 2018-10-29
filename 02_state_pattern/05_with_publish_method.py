"""Create `publish` method in Document, calling corresponding state methods"""

class Draft:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        self.doc.state = self.doc.moderation

class Moderation:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        self.doc.state = self.doc.published

class Published:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        print("Already published")


class Document:
    """Object to hold a state (Context)"""

    def __init__(self):
        self.draft = Draft(self)
        self.moderation = Moderation(self)
        self.published = Published(self)
        self.state = self.draft

    def publish(self):
        self.state.publish()


if __name__ == '__main__':
    doc = Document()  # doc.state -- <__main__.Draft ...>
    doc.publish()     # doc.state -- <__main__.Moderation ...>
    doc.publish()     # doc.state -- <__main__.Published ...>
    doc.publish()     # >> Already published
