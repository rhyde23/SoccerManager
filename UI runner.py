#user interface runner

import pygame, pickle

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Currier', 25)

display = pygame.display.set_mode((792, 612))

pygame.display.set_caption('SoccerManager')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Saves Screen Stuff

save_number = 0

def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Images\\', 'Save', str(save_number), '.png'])
    print(path)
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
    pygame.K_m:2,
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
    
}

print(keyboard_order)
quit()
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
        
        

