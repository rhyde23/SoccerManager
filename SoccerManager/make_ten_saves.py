#make 10 save files

dictionary = {
    'TeamNumber':None,
    'ManagerName':None,
    'CurrentLineup':None,
    'CurrentBudget':None,

}

import pickle

for i in range(1, 11) :
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves', '\\File', str(i), '.dat'])
    output_file = open(file_path, 'wb')
    pickle.dump(dictionary, output_file)
