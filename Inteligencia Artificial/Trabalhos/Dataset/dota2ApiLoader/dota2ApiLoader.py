import dota2api
# from dota2 import dota2API
from dota2api.src.exceptions import APIError, APITimeoutError
import csv
from multiprocessing import Pool
import time
import sys

# D3565EEA9151352BFDEE2C6657CD31BB
# Honeybadger
# 4429.660538434982 seconds

def getMatchInfo( api, matchId ):
    for retries in range(3):
        try:
            match = api.get_match_details(match_id=matchId)
            break
        except APIError as e:
            print(e.msg)
            raise APIError('Getting match ' + str(matchId) + ' Failed')
        except Exception as e:
            print(sys.exc_info())
            if retries == 2:
                raise APIError('Getting match ' + str(matchId) + ' Failed')
            else:
                time.sleep(120)

    if match['human_players'] != 10 or len(match['players']) != 10:
        raise APIError('Bad number of players')
    if 'radiant_win' not in match:
        raise APIError('Match not completed')
    if 'cluster' not in match:
        raise APIError('Cluster attribute not in match')
    if 'game_mode_name' not in match:
            raise APIError('Game mode name attribute not in match')
    if 'lobby_name' not in match:
            raise APIError('Lobby_name attribute not in match')
    matchRow = [0]*15
    matchRow[0] = matchId
    if match['radiant_win']: # eg True
        matchRow[1] = 1
    else:
        matchRow[1] = -1
    matchRow[2] = match['cluster'] # eg 227 -> translates to Europe West?
    matchRow[3] = match['game_mode_name'] # eg Captains Mode
    matchRow[4] = match['lobby_name'] # eg Ranked
    for i in range(10):
        matchRow[5 + i] = match['players'][i]['hero_id'] # eg 5

    return matchRow

def csvParser(matchInfo):
    string = ""
    for key in matchInfo:
        string += str(key) + ";"

    return string

def serialLoop( api, matchId, stopNum, writer ):
    while stopNum > 0:
        try:
            matchInfo = getMatchInfo( api, matchId )
            writer.writerow([csvParser(matchInfo)])
            stopNum -= 1
            print ("Got " + str(matchId) + ", Need " + str(stopNum) + " more")
        except APIError as e:
            print (e.msg)
        finally:
            matchId -= 1

def parallelLoop( api, matchId, stopNum, writer ):
    p = Pool(4)

    matchList = ( [ (api, matchId - x ) for x in range(2*stopNum) ] )
    for x in p.map(getMatchStar, matchList):
        if len(x) != 0:
            writer.writerow([csvParser(x)])
            
    p.terminate()

def getMatchStar( args ):
    try:
        match = getMatchInfo( args[0], args[1] )
        print ("Match " + str(args[1]) + " successful")
        return match
    except APIError as e:
        print (e.msg)
    return []
        

def writeTitle(writer, title):
    writer.writerow([csvParser(title)])

if __name__=="__main__":
    api = dota2api.Initialise()
    #Partidas do dia 14/3/2019 que acabou as 20:32
    matchId = 4375987530
    ### matchSeqNum = 2242825642
    stopNum = 80000
    outFile = open('dotaMatch2.csv', 'a')
    title = ['MatchId', 'Winner Team', 'Server Location', 'Game Type', 'Game Mode', 'Hero1', 'Hero2', 'Hero3', 'Hero4', 'Hero5', 'Hero6', 'Hero7', 'Hero8', 'Hero9', 'Hero10']
    writer = csv.writer(outFile, title, lineterminator = '\n')

    writeTitle(writer, title)
    start = time.time()
    #serialLoop( api, matchId, stopNum, writer )
    parallelLoop( api, matchId, stopNum, writer )
    end = time.time()
    print(str(end - start) + ' seconds')
    
    
    outFile.close()