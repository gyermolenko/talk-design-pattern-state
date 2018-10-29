from transitions import Machine

class Document:
    states = ["draft", "moderation", "published"]

    def __init__(self):
        self.machine = Machine(model=self, states=Document.states, initial="draft")
        self.machine.add_transition(trigger="publish", source="draft", dest="moderation")
        self.machine.add_transition(trigger="publish", source="moderation", dest="published")
        self.machine.add_transition(trigger="reject", source="moderation", dest="draft")


if __name__ == '__main__':
    doc = Document() # doc.state -- "draft"
    doc.reject()     # transitions.core.MachineError: "Can't trigger event reject from state draft!"
    doc.publish()    # doc.state -- "moderation"
    doc.publish()    # doc.state -- "published"
    doc.publish()    # transitions.core.MachineError: "Can't trigger event publish from state published!"
