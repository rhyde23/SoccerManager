#make 10 save files

dictionary = {
    'TeamNumber':None,
    'ManagerName':None,
    'CurrentLineup':None,
    'CurrentBudget':None,
    'CurrentTeamOverall':None,

}

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

