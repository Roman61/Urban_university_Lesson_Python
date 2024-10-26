import unittest
from Analyzers.ADataRequirements.Descriptions import DataRequirement


class TestDataRequirements(unittest.TestCase):
    def test_data_requirement_creation(self):
        req = DataRequirement(name="UserName", description="The name of the user", type="string")
        self.assertEqual(req.name, "UserName")
        self.assertEqual(req.description, "The name of the user")
        self.assertEqual(req.type, "string")


if __name__ == '__main__':
    unittest.main()
