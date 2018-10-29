"""Craete `reject` method and handle attempts of erroneous state changes"""

class Draft:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        self.doc.state = self.doc.moderation

    def reject(self):
        print("Can't reject draft")

class Moderation:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        self.doc.state = self.doc.published

    def reject(self):
        self.doc.state = self.doc.draft

class Published:
    def __init__(self, doc):
        self.doc = doc

    def publish(self):
        print("Already published")

    def reject(self):
        print("Can't reject published")

class Document:
    """Object to hold a state (Context)"""

    def __init__(self):
        self.draft = Draft(self)
        self.moderation = Moderation(self)
        self.published = Published(self)
        self.state = self.draft

    def publish(self):
        self.state.publish()

    def reject(self):
        self.state.reject()


if __name__ == '__main__':
    doc = Document()  # doc.state -- <__main__.Draft ...>
    doc.publish()     # doc.state -- <__main__.Moderation ...>
    doc.reject()      # doc.state -- <__main__.Draft ...>
    doc.reject()      # >> Can't reject draft
