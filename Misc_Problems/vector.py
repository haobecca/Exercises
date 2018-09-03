# Creating Vector Class
# Rebecca Haskins

import math

class Vector:

    def __init__(self, length, direction):
        self.length = length
        self.direction = direction
    
    def get_length(self):
        """ Return length of vector object """
        return self.length


    def get_direction(self):
        """ Return direction of vector object """
        return self.direction

    def get_x(self):
        """ Return x value of vector object """
        rad = math.radians(self.direction)
        return self.length * (math.cos(rad))

    def get_y(self):
        """ Return y value of vector object """
        rad = math.radians(self.direction)
        return self.length * (math.sin(rad))

    def get_dot_product(self, another_vector):
        """ Return dot product of self_vector and another_vector """
        self_x = self.get_x()
        self_y = self.get_y()
        another_x = another_vector.get_x()
        another_y = another_vector.get_y()
        return (self_x * another_x) + (another_y * self_y)

    def get_dot_angle(self, another_vector):
        """ Return angle between two vector objects """
        dot_product = self.get_dot_product(another_vector)
        square_root_self = self.get_length()
        square_root_another_vector = another_vector.get_length()
        inside_acos = ((dot_product) / (square_root_self * square_root_another_vector))
        print(dot_product)
        print(square_root_self)
        print(square_root_another_vector)
        print(inside_acos)
        return (math.degrees(math.acos(inside_acos)))



v1 = Vector(5, 45)
v2 = Vector(8, 60)
print(type(v1))
print(v1.get_length())
print(v1.get_x())
print(v1.get_y())
print(v1.get_dot_product(v2))
print(v1.get_dot_angle(v2))
## Testing Git