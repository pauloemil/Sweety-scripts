import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((1000,500))
pygame.display.set_caption("paulo bubble sort visual")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)
sortDelay = 1
heightList = []
for i in range(198):#generate the list which contain the unsorted heights
    heightList.append([randint(0,500), white])

def draw():
    global heightList
    pygame.display.update()
    window.fill(black)

    muxer = 4#used to increase the space between lines so it can be seen will   | . || . | the diff between the points
    space = muxer/2 #to start right on the first pixel
    for i in range(len(heightList)):
                        #screan, color , (x1, y1), (x2, y2) width
        pygame.draw.line(window,heightList[i][1], (i+space, 500), (i+space, 500 - heightList[i][0]), muxer)
        space += muxer

payed = True #just to make it run once
i = 0
end = len(heightList)
while True: #easy selection sort algorithm

    if sorted(heightList) != heightList:
        end -= 1
        for i in range(end):
            if heightList[i][0] > heightList[end][0]:
                heightList[i][1] = red
                heightList[end][1] = red
                draw() #draw it with red color if not sorted
                pygame.time.delay(sortDelay)
                temp = heightList[i][0]
                heightList[i][0] = heightList[end][0]
                heightList[end][0] = temp
            heightList[i][1] = green
            heightList[end][1] = green
            draw()#draw with green color if sorted
            pygame.time.delay(sortDelay)
            heightList[i][1] = white
            heightList[end][1] = white
    elif payed:
        for j in range(len(heightList)):#run on all of them once more as if iam checking 0_O
            heightList[j][1] = green
            draw()
            pygame.time.delay(50)
            heightList[j][1] = white
        draw()
        print("I'm fuckin done ! -_-!")
        payed = False
        pygame.time.delay(600)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
