#! /usr/bin/env python

from partyanimal import PartyAnimal

class FootballFan(PartyAnimal):
    """ child class static instance variable """
    points = 0
   
    
    def touchdown(self):
        """ manipulation of static instance variable """
        self.points = self.points + 7
        self.party()
        print self.name, " points ", self.points


jimmy = FootballFan('Jim')
jimmy.party()
jimmy.touchdown()
