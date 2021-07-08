#Web Scraper

import requests, re, pickle
from bs4 import BeautifulSoup

def scrape(link) :
    page = requests.get(link)
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    return soup


card_types = ['nifgold', 'nifsilver', 'nifbronze']


def main() :
    final_dict = {
        'Manchester City':{},
        'Manchester United':{},
        'Liverpool':{},
        'Chelsea':{},
        'Leicester City':{},
        'West Ham United':{},
        'Tottenham Hotspur':{},
        'Arsenal':{},
        'Leeds United':{},
        'Everton':{},
        'Aston Villa':{},
        'Newcastle United':{},
        'Wolverhampton Wanderers':{},
        'Crystal Palace':{},
        'Southampton':{},
        'Brighton & Hove Albion':{},
        'Burnley':{},
        'Fulham':{},
        'West Bromwich Albion':{},
        'Sheffield United':{}
    }
    for card_type in card_types :
        x = 0
        while True :
            page_dict = {}
            main_link = "https://www.futwiz.com/en/fifa21/players?page="+str(x)+"&release="+card_type+"&leagues[]=13"
            soup = scrape(main_link)
            player_names_in_order = []
            findings = re.findall('\"[A-Za-z\s]+[0-9]{2}\sRated\"', soup)
            if findings == [] :
                break
            for player_string in findings :
                rating = re.findall('[0-9]+', player_string)[0]
                name = player_string.split(rating)[0][1:][:-1]
                link_version_of_name = '-'.join([s.lower() for s in name.split(' ')])
                link = 'https://www.futwiz.com/'+re.search('a href=\"/en/fifa21/player/'+link_version_of_name+'/[0-9]+\"', soup).group()[8:][:-1]
                player_soup = scrape(link)
                main_info_section = player_soup.split('h1')[1]
                main_info_matches = re.findall('>[^<>]+<', main_info_section)
                nation, team = main_info_matches[3][1:][:-1], main_info_matches[5][1:][:-1]
                if team == 'Brighton &amp; Hove Albion' :
                    team = 'Brighton & Hove Albion'
                chem_section = player_soup.split('mt-10 altpos-pitch mb-20')[1].split('p style')[0]
                chem_section_matches = re.findall('>[^<>]+<', chem_section)
                chem_section_matches = [s[1:][:-1] for s in chem_section_matches if s != '>\n<']
                ratings = chem_section_matches[::2]
                positions = chem_section_matches[1::2]
                chem_dictionary = {}
                for i, pos in enumerate(positions) :
                    chem_dictionary[pos] = int(ratings[i])
                page_dict[name] = {'Rating':rating, 'Team':team, 'Nation':nation, 'Positions':chem_dictionary}
                player_names_in_order.append(name)

            for i, match in enumerate(re.findall('<div class=\"card-21-pack-position\">[A-Z]+</div>', soup)) :
                try :
                    match = re.findall('>[^<>]+<', match)[0][1:][:-1]
                    page_dict[player_names_in_order[i]]['Position'] = match
                except :
                    break
            for player_key in page_dict :
                player_info = page_dict[player_key]
                team = player_info['Team']
                if not team in final_dict :
                    print(team)
                    quit()
                final_dict[team][player_key] = player_info
            x += 1
            print(x)
            
    return final_dict

final_dict = main()
for team in final_dict :
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\', team, '.dat'])
    output_file = open(file_path, 'wb')
    pickle.dump(final_dict[team], output_file)



file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database', '\\ThrowawayFile.dat'])
output_file = open(file_path, 'wb')
pickle.dump({}, output_file)

    
    
    
