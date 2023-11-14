#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes by calling the super class."""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size.
        The setter assigns the width and the height with the
        same value and validates values based on the logic in
        the Rectangle class."""

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Displays a human-readable representation of the Rectangle.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """Assigns args and kwargs to the attributes."""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary of the attributes of the Square."""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
