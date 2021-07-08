#user interface runner

import pygame, pickle
from os import listdir 

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Currier', 25)

display = pygame.display.set_mode((792, 612))

pygame.display.set_caption('SoccerManager')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Load Database and stuff

arsenal = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Arsenal.dat', 'rb'))
aston_villa = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Aston Villa.dat', 'rb'))
brighton_and_hove_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Brighton & Hove Albion.dat', 'rb'))
burnley = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Burnley.dat', 'rb'))
chelsea = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Chelsea.dat', 'rb'))
crystal_palace = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Crystal Palace.dat', 'rb'))
everton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Everton.dat', 'rb'))
fulham = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Fulham.dat', 'rb'))
leeds_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Leeds United.dat', 'rb'))
leicester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Leicester City.dat', 'rb'))
liverpool = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Liverpool.dat', 'rb'))
manchester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Manchester City.dat', 'rb'))
manchester_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Manchester United.dat', 'rb'))
newcastle_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Newcastle United.dat', 'rb'))
sheffield_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Sheffield United.dat', 'rb'))
southampton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Southampton.dat', 'rb'))
tottenham_hotspur = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Tottenham Hotspur.dat', 'rb'))
west_bromwich_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\West Bromwich Albion.dat', 'rb'))
west_ham_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\West Ham United.dat', 'rb'))
wolverhampton_wanderers = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Team Database\\Wolverhampton Wanderers.dat', 'rb'))


#Saves Screen Stuff

save_number = 0

def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Images\\', 'Save', str(save_number), '.png'])
    return pygame.image.load(path).convert()

save_background_images = []
for i in range(10) :
    current_save_image = get_save_image(i+1)
    save_background_images.append(current_save_image)

current_save_image = save_background_images[save_number]

save_names = []
for i in range(10) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves\\', 'File', str(i+1), 'BasicInfo.dat'])
    basic_info = pickle.load(open(path, 'rb'))
    save_names.append(basic_info['SaveName'])

save_names_texts = []
for save_name in save_names :
    save_names_texts.append(myfont.render(save_name, True, (0, 0, 0)))
    
clicker_mode = False
current_clicked = (0, 0)


y_difference = 37
x_start, x_end = 43, 761
buttons = []
for i in range(10) :
    first_y = 154+(i*y_difference)
    second_y = first_y+y_difference
    buttons.append([first_y, second_y])

print(buttons)

offset = [12, 13, 14, 16, 17, 19, 20, 22, 23, 25]


save_selected = None
#####

#Name Save Stuff

keyboard_order = {
    pygame.K_m:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Images\\Page-002.png').convert()
    pygame.K_n:3,
    pygame.K_b:4,
    pygame.K_v:5,
    pygame.K_c:6,
    pygame.K_x:7,
    pygame.K_z:8,
    pygame.K_l:9,
    pygame.K_k:10,
    pygame.K_j:11,
    pygame.K_h:12,
    pygame.K_g:13,
    pygame.K_f:14,
    pygame.K_d:15,
    pygame.K_s:16,
    pygame.K_a:17,
    pygame.K_p:18,
    pygame.K_o:19,
    pygame.K_i:20,
    pygame.K_u:21,
    pygame.K_y:22,
    pygame.K_t:23,
    pygame.K_r:24,
    pygame.K_e:25,
    pygame.K_w:26,
    pygame.K_q:27,
    pygame.K_DELETE:28,
    pygame.K_0:29,
    pygame.K_9:30,
    pygame.K_8:31,
    pygame.K_7:32,
    pygame.K_6:33,
    pygame.K_5:34,
    pygame.K_4:35,
    pygame.K_3:36,
    pygame.K_2:37,
    pygame.K_1:38,
}

keyboard_letters = {
    pygame.K_m:'M',
    pygame.K_n:'N',
    pygame.K_b:'B',
    pygame.K_v:'V',
    pygame.K_c:'C',
    pygame.K_x:'X',
    pygame.K_z:'Z',
    pygame.K_l:'L',
    pygame.K_k:'K',
    pygame.K_j:'J',
    pygame.K_h:'H',
    pygame.K_g:'G',
    pygame.K_f:'F',
    pygame.K_d:'D',
    pygame.K_s:'S',
    pygame.K_a:'A',
    pygame.K_p:'P',
    pygame.K_o:'O',
    pygame.K_i:'I',
    pygame.K_u:'U',
    pygame.K_y:'Y',
    pygame.K_t:'T',
    pygame.K_r:'R',
    pygame.K_e:'E',
    pygame.K_w:'W',
    pygame.K_q:'Q',
    pygame.K_0:'0',
    pygame.K_9:'9',
    pygame.K_8:'8',
    pygame.K_7:'7',
    pygame.K_6:'6',
    pygame.K_5:'5',
    pygame.K_4:'4',
    pygame.K_3:'3',
    pygame.K_2:'1',
    pygame.K_1:'1',
}

path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Images\\', 'Save', str(save_number), '.png'])
pygame.image.load(path).convert()

current_typed = ''

#####
    
manager_loop = True
saves_menu = True
name_save = False




while manager_loop :
    while saves_menu :
        display.fill(white)
        display.blit(current_save_image, (0, 0))
        display.set_at(current_clicked, red)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if clicker_mode :
                    current_clicked = coords
                save_selected = save_number
                print(save_selected)
                saves_menu = False
                name_save = True
                
        
        for i, save_name_text in enumerate(save_names_texts) :
            text_y = buttons[i][0]+offset[i]
            display.blit(save_name_text, (100, text_y))
            
        if x >= x_start and x <= x_end :
            for i, button in enumerate(buttons) :
                if y >= button[0] and y <= button[1] :
                    save_number = i
                    current_save_image = save_background_images[save_number]
        pygame.display.update()
    while name_save :
        display.fill(white)
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                print(event.key)
        pygame.display.update()
        
        

