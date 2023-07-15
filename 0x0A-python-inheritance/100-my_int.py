#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """
    MyInt is a rebel
    MyInt has == and != operators inverted
    """

    def __eq__(self, parameter):
        return super().__ne__(parameter)

    def __ne__(self, parameter):
        return super().__eq__(parameter)
