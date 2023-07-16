#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method of a rectangle
        args:
        width: width of a rectangle
        height: height of a rectangle
        x: x coordinate of a rectangle
        y: y coordinate of a rectangle
        Raises:
        TypeError: if either width, height, x or y isn't an integer
        ValueError:if either width, height, x or y isn't  > 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width to value entered"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height to value entered"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x to value entered"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y to value entered"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area value of the Rectangle instance"""
        area = self.__height * self.__width
        return area

    def display(self):
        """print rectangle with #"""
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for o in range(self.x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle"""
        return {'x': self.x,
                'y': self.y, 
                'id': self.id,
                'height': self.height,
                'width': self.width}
