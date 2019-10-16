"""
this module get original informations from api.steampowered.com and store them in json format.
"""


import urllib.request
import json


class dota2API():

    """docstring for dota2API"""

    GetMatchHistory = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/"
    GetMatchDetails = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/"
    GetHeroes = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/"
    GetPlayerSummaries = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    EconomySchema = "https://api.steampowered.com/IEconItems_570/GetSchema/v0001/"
    GetLeagueListing = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/"
    GetLiveLeagueGames = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/"
    GetMatchHistoryBySequenceNum = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/"
    GetTeamInfoByTeamID = "https://api.steampowered.com/IDOTA2Match_570/GetTeamInfoByTeamID/v001/"
    steamid64_32 = 76561198080336175
    key = 'D3565EEA9151352BFDEE2C6657CD31BB'

    def __init__(self):
        super(dota2API, self).__init__()

    def getTeamInfo(self):
        data = '?key=' + self.key
        res = urllib.request.urlopen(self.GetTeamInfoByTeamID + data)
        # print(res.status, res.reason)
        # print(res.getheaders())
        teaminfo_str = res.read().decode('utf-8')
        teaminfo_file = open("teaminfo_original.json", "w")
        teaminfo_file.write(teaminfo_str)
        teaminfo_file.close()

    def getLeagueList(self):
        data = '?key=' + self.key
        res = urllib.request.urlopen(self.GetLeagueListing + data)
        leaguelist_str = res.read().decode('utf-8')
        leaguelist_file = open("leaguelist_original.json", "w")
        leaguelist_file.write(leaguelist_str)
        leaguelist_file.close()

    def createLeaguePool(self):
        leaguelist_file = open("leaguelist_original.json", "r")
        leaguelist_str = leaguelist_file.read()
        leaguelist = json.loads(leaguelist_str)
        leaguepool = leaguelist["result"]["leagues"]
        leaguepool_str = json.dumps(leaguepool)
        leaguepool_file = open("leaguepool.json", "w")
        leaguepool_file.write(leaguepool_str)
        leaguepool_file.close()

    def convertTeamInfo(self):
        teaminfo_file = open("teaminfo_original.json", "r")
        teaminfo_str = teaminfo_file.read()
        teaminfo_file.close()
        # print(teaminfo_str)
        teaminfo = json.loads(teaminfo_str)
        # teaminfo_str = json.dumps(teaminfo)
        # teaminfo_file.write(teaminfo_str)

        # print(teaminfo)
        # print("\n\n\n")
        print(teaminfo["result"]["teams"][0])
        self.createPlayerPool(teaminfo["result"]["teams"])

    def createPlayerPool(self, teams):
        playerpool = {}
        for team in teams:
            print(team["name"])
            i = 0
            while True:
                if "player_" + str(i) + "_account_id" in team:
                    playerid_32 = team["player_" + str(i) + "_account_id"]
                    playerid_64 = playerid_32 + self.steamid64_32
                    data = '?key=' + self.key + '&steamids=' + str(playerid_64)
                    res = urllib.request.urlopen(
                        self.GetPlayerSummaries + data)
                    playerinfo_str = res.read().decode('utf-8')
                    playerinfo = json.loads(playerinfo_str)
                    # playerinfo = {
                    #     playerid_32: playerinfo["response"]["players"]}
                    playerpool[playerid_32] = playerinfo[
                        "response"]["players"][0]
                    print(playerid_32)
                    i += 1
                else:
                    break
        playerpool_str = json.dumps(playerpool)
        playerpool_file = open("playerpool.json", "w")
        playerpool_file.write(playerpool_str)
        playerpool_file.close()


dota2_api = dota2API()
# dota2_api.getTeamInfo()
# dota2_api.convertTeamInfo()
dota2_api.getLeagueList()
dota2_api.createLeaguePool()
print("done")
# input()