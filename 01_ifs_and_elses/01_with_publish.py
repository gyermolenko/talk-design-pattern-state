"""
It is already perfect!
    OR
Why even bother?
"""

class Document:

    def __init__(self):
        self.state = "draft"

    def publish(self):
        if self.state == "draft":
            self.state = "moderation"
        elif self.state == "moderation":
            self.state = "published"
        elif self.state == "published":
            print("Already published")


if __name__ == '__main__':
    doc = Document() # doc.state -- "draft"
    doc.publish()    # doc.state -- "moderation"
    doc.publish()    # doc.state -- "published"
    doc.publish()    # >> Already published
