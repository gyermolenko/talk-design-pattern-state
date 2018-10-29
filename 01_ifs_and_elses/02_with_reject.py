"""
We need new method:
reject from `moderation` state back to `draft`
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

    def reject(self):
        if self.state == "draft":
            print("Can't reject draft")
        elif self.state == "moderation":
            self.state = "draft"
        elif self.state == "published":
            print("Can't reject published")


if __name__ == '__main__':
    doc = Document() # doc.state -- "draft"
    doc.reject()     # >> Can't reject draft
    doc.publish()    # doc.state -- "moderation"
    doc.publish()    # doc.state -- "published"
    doc.publish()    # >> Already published
