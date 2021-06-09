
from identified_object import IdentifiedObject


class League(IdentifiedObject):

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self.competitions_in_league = []

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self.competitions_in_league

    def add_team(self, prop):
        self._teams.append(prop)

    def add_competition(self, prop):
        self.competitions.append(prop)

    def teams_for_member(self, member):
        return [team for team in self._teams if member in team.members]

    def competitions_for_team(self, team):
        return [competition for competition in self.competitions_in_league if team in competition.teams_competing]

    def competitions_for_member(self, member):
        member_teams = [team for team in self._teams if member in team.members]
        return [competition for competition in self.competitions_in_league if any(x in member_teams for x in competition.teams_competing)]

    # __str__() -- return a string like the following: "League Name: N teams, M competitions"
    def __str__(self):
        return str(self.name + ": " + len(self.teams) + ", " + len(self.competitions_in_league))
