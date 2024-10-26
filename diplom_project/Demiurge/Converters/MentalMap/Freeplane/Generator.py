def __init__(self, app_description):
    self.app_description = app_description
    self.screens = []


def generate_map(self):
    # Логика для разбивки описания на экраны
    descriptions = self.app_description.split('\n')
    for desc in descriptions:
        if desc.strip():
            screen = Screen(desc)
            self.screens.append(screen)
    return self.screens


class Screen:
    def __init__(self, description):
        self.description = description
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def __repr__(self):
        return f"Screen(description={self.description}, events={self.events})"