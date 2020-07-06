class Component:
    def html(self):
        raise NotImplementedError

    def __str__(self):
        return self.html()