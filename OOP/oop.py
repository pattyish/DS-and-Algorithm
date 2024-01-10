class StarCookie:
    # Shareable with objects
    milk = 0.1
    # You can set up default value in initializer or constructors

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


star_cookie1 = StarCookie("Red", 17)
# __dict__ get all attributes of objects as dictionary
print(star_cookie1.__dict__)
star_cookie2 = StarCookie("Blue", 17)
print(star_cookie2.__dict__)
