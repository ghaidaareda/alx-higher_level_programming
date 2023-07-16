#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square that inhereit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method of square:
        args:
        from super class are :id, x, y, width and height
        width and height are assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width
    
    @size.setter
    def size(self, value):
        """ size gettet & validtion"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
        
    def __str__(self):
        """ string represenation of square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
