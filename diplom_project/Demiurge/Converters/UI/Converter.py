class UIConverter:
    def __init__(self, ux_design):
        self.ux_design = ux_design
        self.ui_components = []

    def convert_to_ui(self):
        # Преобразование каждого UX элемента в UI компонент
        for ux in self.ux_design:
            ui_component = UIComponent(
                properties={"description": ux.properties["description"]})  # Можно добавить другие свойства
            self.ui_components.append(ui_component)
        return self.ui_components


class UIComponent:
    def __init__(self, properties):
        self.properties = properties

    def __repr__(self):
        return f"UIComponent(properties={self.properties})"