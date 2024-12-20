class Square:
    def __init__(self, a):
        self.a = a  # Initialize side length

    def area(self):
        return self.a * self.a  # Calculate area

    def perimeter(self):
        return self.a * 4  # Calculate perimeter

def main():
    # Create two square objects
    square1 = Square(4)
    square2 = Square(6)

    # Print details for square1
    print('Square with side 4:')
    print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')

    # Print details for square2
    print('Square with side 6:')
    print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')

# Call the main function to run the program
if __name__ == "__main__":
    main()
