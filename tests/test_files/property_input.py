class TestClass:
    @property
    def z_property(self):
        pass

    @z_property.setter
    def z_property(self, value):
        pass

    @property
    def a_property(self):
        pass

    @property
    def b_property(self):
        pass

    @b_property.deleter
    def b_property(self):
        pass

    @b_property.setter
    def b_property(self, value):
        pass

    @z_property.getter
    def z_property(self):
        pass

    @a_property.setter
    def a_property(self, value):
        pass
