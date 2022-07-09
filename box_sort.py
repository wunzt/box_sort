# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/08/2022
# Description: Calculates the volumes of boxes and sorts a list of box objects from greatest to least volume.

class Box:
    """Represents a box with a length, width, and height and calculates its volume."""

    def __init__(self, length, width, height):
        """Initializes a box with a length, width, and height."""
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Returns the length of the box."""
        return self._length

    def get_width(self):
        """Returns the width of the box."""
        return self._width

    def get_height(self):
        """Returns the height of the box."""
        return self._height

    def volume(self):
        """Calculates the volume of the box."""
        box_volume = self.get_length() * self.get_width() * self.get_height()
        return box_volume

def box_sort(box_list):
    """Uses insertion sort to sort the boxes from greatest to least volume."""
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1

        while pos >= 0 and box_list[pos].volume() < value.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1

        box_list[pos + 1] = value

    return box_list