#!/usr/bin/python3
"""Creates a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes for the Square.

        Attributes:
            size (int): The length of the size of the Square.
            x (int): The x coordinate inherited from Rectangle.
            y (int): The y coordinate inherited from Rectangle.
            id (int): id inherited from Rectangle.
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size.
        Checks if size is a non-zero positive integer."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Adds args and kwargs.

        Args:
            *args (int): Order of arguments.
            - id represents id
            - size represents the sides of the Square
            - x represents x-coordinate of the Square
            - y represents y-coordinate of the Square

            **kwargs (int): a dictionary.
            - keys represent attribute of Square.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            elif len(args) >= 2:
                self.size = argss[1]
            elif len(args) >= 3:
                self.x = args[2]
            elif len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def validate_x(self, value):
        """Calls inherited x getter and setter."""
        self.__x = x

    def validate_y(self, value):
        """Calls inherited x getter and setter."""
        self.__y = y

    def __str__(self):
        """Returns a string rep of the Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        size = self.height
        return f"[Square] ({id}) {x}/{y} - {size}"
