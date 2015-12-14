#! /usr/bin/env python

class PartyAnimal:
    """ static class instance variable """
    x = 0


    def __init__(self, nam):
        """ instance vairable, nam in constructor """
        self.name = nam
        print "I am constructor as ", self.name
    

    def party(self):
        """ call static class instance variable """
        self.x = self.x + 1
        print "so far ", self.x


    def __del__(self):
        """" last call from destructor """
        print "I am destructor"


if __name__ == "__main__":
    """ testing class inheritance """
    sally = PartyAnimal('Sally')
    sally.party()
    sally.party()

    jim   = PartyAnimal('Jim')
    jim.party()
