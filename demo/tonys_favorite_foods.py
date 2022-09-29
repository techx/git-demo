

class Foods:
    def __init__(self,foods) -> None:
        self.foods = foods

    def request(self,i):
        return self.foods[i] if i < len(self.foods) else None

    def __repr__(self) -> str:
        return "you <3"
favorites = ['bbb','peaches','strawberries','dimsum']

if __name__ == '__main__':
    #code change here also
    #here is another code change!
    tonys_foods = Foods(favorites)
    print(tonys_foods.request(0))