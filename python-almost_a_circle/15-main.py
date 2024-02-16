#!/usr/bin/python3
""" 15-main """
from models.square import Square

if __name__ == "__main__":

    r1 = Square(10, 7, 2)
    r2 = Square(2, 4)
    Square.save_to_file([r1, r2])

