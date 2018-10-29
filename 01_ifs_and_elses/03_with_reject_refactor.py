DRAFT = "draft"
MODERATION = "moderation"
PUBLISHED = "published"

class Document:

    def __init__(self):
        self.state = DRAFT

    def publish(self):
        if self.state == DRAFT:
            self.state = MODERATION
        elif self.state == MODERATION:
            self.state = PUBLISHED
        elif self.state == PUBLISHED:
            print("Already published")

    def reject(self):
        if self.state == DRAFT:
            print("Can't reject draft")
        elif self.state == MODERATION:
            self.state = DRAFT
        elif self.state == PUBLISHED:
            print("Can't reject published")


if __name__ == '__main__':
    doc = Document() # doc.state -- "draft"
    doc.reject()     # >> Can't reject draft
    doc.publish()    # doc.state -- "moderation"
    doc.publish()    # doc.state -- "published"
    doc.publish()    # >> Already published
