#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class implementation"""
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ Function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square Class Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Square Class Setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return Class String"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Update Function"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        elif len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.width = v
                    self.height = v                    
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """to dict function"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}