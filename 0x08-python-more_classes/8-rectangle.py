#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """ class defines rectangle"""
    number_of_instances = 0
    """ number of instances"""
    print_symbol = "#"
    """Used as symbol for string representation"""

    def __init__(self, width=0, height=0):
        """
        init method define square
        width:private instance define width
        height:private instance define height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ method to define area of rectangle"""
        rec_area = self.__width * self.__height
        return rec_area

    def perimeter(self):
        """ method to define peimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            rec_perimeter = 0
        else:
            rec_perimeter = (2 * self.__width) + (2 * self.__height)
        return rec_perimeter

    def __str__(self):
        """
        return well read string retprestantion of rectangle
        formed of #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rec_str = ""
            for i in range(self.height):
                rec_str += str(self.print_symbol) * self.__width + "\n"
            return rec_str[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 > area_2:
                return rect_1
            elif area_1 < area_2:
                return rect_2
            elif area_1 == area_2:
                return rect_1
