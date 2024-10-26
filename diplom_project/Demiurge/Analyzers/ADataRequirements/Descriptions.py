class DataRequirement:
    def __init__(self, name, description, req_type):
        self.name = name
        self.description = description
        self.type = req_type
        self.validate()

    def validate(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string.")
        if self.type not in ['string', 'integer', 'float']:
            raise ValueError("Type must be one of: ['string', 'integer', 'float']")

    def __repr__(self):
        return f"DataRequirement(name={self.name}, description={self.description}, type={self.type})"
