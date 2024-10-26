import unittest
from Analyzers.AEvents.Event import Event


class TestEvent(unittest.TestCase):
    def test_event_creation(self):
        event = Event(name="click", description="Click event", event_type="click")
        self.assertEqual(event.name, "click")
        self.assertEqual(event.description, "Click event")
        self.assertEqual(event.event_type, "click")


if __name__ == '__main__':
    unittest.main()
