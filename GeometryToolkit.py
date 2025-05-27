class ShapeCalculator:

    def area(self, *args):
        if len(args) == 1:
            r = args[0]
            print("Area of circle:", 3.14 * r * r)
        elif len(args) == 2:
            l, b = args
            print("Area of rectangle:", l * b)
        else:
            print("Invalid number of arguments")

a = ShapeCalculator()
a.area(5)
a.area(5, 10)   