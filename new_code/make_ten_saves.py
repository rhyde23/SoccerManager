#make 10 save files

teams_in_league = [
    'Arsenal',
    'Aston Villa',
    'Brighton & Hove Albion',
    'Burnley',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Fulham',
    'Leeds United',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Sheffield United',
    'Southampton',
    'Tottenham Hotspur',
    'West Bromwich Albion',
    'West Ham United',
    'Wolverhampton Wanderers'
]

dictionary = {
    'TeamName':'',
    'ManagerName':'',
    'CurrentLineup':None,
    'CurrentFormation':''
    'CurrentBudget':None,
    'CurrentTeamOverall':None,
    'DaysAdvanced':0,
    'CurrentDate':'June 1 2020',
    'CurrentEmails':[],
    'CurrentStandings':{},
    'CurrentStandingsInOrder':[],
    'TopScorers':{},
    'TopScorersInOrder':[],
    'TopAssistors':{},
    'TopAssistorsInOrder':[]
}

for team in teams_in_league :
    dictionary[team] = {}

basic_info_dictionary = {
    'SaveName':'EMPTY SAVE'
}

import pickle

for i in range(1, 11) :
    print(i)
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\File', str(i), '.dat'])
    output_file = open(file_path, 'wb')
    pickle.dump(dictionary, output_file)
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\File', str(i), 'BasicInfo.dat'])
    output_file = open(file_path, 'wb')
    pickle.dump(basic_info_dictionary, output_file)

file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\ThrowawayFile.dat'])
output_file = open(file_path, 'wb')
pickle.dump(dictionary, output_file)

