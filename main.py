class Burger:
    def __init__(self):
        self.lettuce: bool = False
        self.tomatoes: bool = False
        self.pickles: bool = False
        self.cheese: bool = False

    def put_lettuce(self):
        self.lettuce = True
        return self

    def put_tomatoes(self):
        self.tomatoes = True
        return self

    def put_pickles(self):
        self.pickles = True
        return self

    def put_cheese(self):
        self.cheese = True
        return self

    @staticmethod
    def map_boolean(ingredient) -> str:
        if ingredient:
            return 'Yes'
        return 'No'

    def __str__(self):
        return f"Pickles: [{self.map_boolean(self.pickles)}]\n" \
               f"Tomatoes: [{self.map_boolean(self.tomatoes)}]\n" \
               f"Lettuce: [{self.map_boolean(self.lettuce)}]\n" \
               f"Cheese: [{self.map_boolean(self.cheese)}]\n"

burger = print(Burger().put_cheese().put_pickles().put_tomatoes())