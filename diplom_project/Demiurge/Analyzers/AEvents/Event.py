class Event:
    def __init__(self, name, description, event_type):
        self.name = name
        self.description = description
        self.event_type = event_type  # Например, "click", "keypress"

    def trigger(self):
        print(f"Triggering event: {self.name}")

    def __repr__(self):
        return f"Event(name={self.name}, description={self.description}, type={self.event_type})"
