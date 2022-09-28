

class ShortPeopleIdentifier:
    short_people = set(["joyce","hannak","hannaz"])

    def check(name):
        return True if name in ShortPeopleIdentifier.short_people else False

if __name__ == '__main__':
    name = 'joyce'
    #code change
    print(ShortPeopleIdentifier.check('joyce'))