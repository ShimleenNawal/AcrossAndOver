def setup():
    global stageNum, imgRoad, stage1Gift, stage1Car, stage2Car
    global player, playerX, playerY, playerW, playerH
    global friend, friendX, friendY, friendW, friendH
    global carsTop, carsBottom, carXTop, carXBottom, carYTop, carYBottom, carsTopdx, carsBottomdx, carW, carH
    global gifts, giftX, giftY, giftW, giftH
    global restart, restartX, restartY
    global gameEnd, gameEndX, gameEndY
    global buttonW, buttonH
    global startTime, currentTime, score
    global giftCounted, carCounted, giftVisible
    global running, minim 
    
    size(1000, 500)
    
    #stageNum
    # 0:Welcome Page
    # 1:Game Play Level 1
    # 2:Game Play Level 2
    # 3:Game Over (Lose)
    # 4:Game Over (Win)
    
    stageNum = 0
    startTime = millis()
    currentTime = millis()-startTime
    score = 0
    stage1Gift = 2 
    stage1Car = 3
    stage2Car = 3
    running = True
    imgRoad = loadImage("road.jpeg") #background
    player = loadImage("woman.png")
    friend = loadImage("friend.png")
    restart = loadImage("restart.png")
    gameEnd = loadImage("stop.png")
     
   
    #add_library('minim')
    #minim=Minim(this)
    #variable = minim.loadFile("Monkeys Spinning Monkeys.mp3")
    
    #if stageNum==1 or stageNum==2:
    #variable.play()
    
    #if stageNum==0 or stageNum==3 or stageNum==4:
    #y7minim.stop()
    

    carW = 150
    carH = 75
    carsTopdx = 2
    carsBottomdx = -2
    giftW = 50
    giftH = 50
    playerW = 25
    playerH = 50
    friendW = 25
    friendH = 50
    playerX = width/2-50
    playerY = height-150
    friendX = width/2
    friendY = 10
    restartX = 350
    restartY = 250
    gameEndX = 550
    gameEndY = 250
    buttonW = 150
    buttonH = 150
    
    
                
    carsTop = []
    carsBottom = []
    carXTop = []
    carXBottom = []
    carYTop = []
    carYBottom = []
    gifts = []
    giftX = []
    giftY = []
    giftCounted = [] 
    giftVisible = []
    carCounted = [] 
    
    for i in range(stage1Car):
        carsTop.append(loadImage("car"+str(i+3)+".png"))
        carXTop.append(i*400)
        carYTop.append(150)
        carCounted.append(False)
   
    for i in range(stage1Car):
        carsBottom.append(loadImage("car"+str(i)+".png"))
        carXBottom.append(i*400)
        carYBottom.append(275)
        carCounted.append(False)
    
    for i in range(stage2Car):
        carsTop.append(loadImage("car"+str(i+6)+".png"))
        carXTop.append(i*160)
        carYTop.append(150)
        carCounted.append(False)
   
    for i in range(stage2Car):
        carsBottom.append(loadImage("car"+str(i)+".png"))
        carXBottom.append(i*160)
        carYBottom.append(275)
        carCounted.append(False)    
        
    for i in range(stage1Gift):    
        gifts.append(loadImage("gift"+str(i)+".png"))
        giftX.append(random(0,width-giftW))
        giftY.append(random(100,300))                
        giftCounted.append(False)     
        giftVisible.append(True) 
    
    for i in range(2,3):    
        gifts.append(loadImage("gift"+str(i)+".png"))
        giftX.append(random(0,width-giftW))
        giftY.append(random(100,300))                
        giftCounted.append(False)     
        giftVisible.append(True)                     
        
def draw():
    if stageNum==0:
       drawWelcomePage()
    elif stageNum==1:
       drawGamePlayLevel1()
    elif stageNum==2:
       drawGamePlayLevel2() 
    elif stageNum==3: 
       drawGameOverPage()   
    elif stageNum==4:
       drawWinPage() 
       
def drawWelcomePage():
    image(imgRoad, 0, 0, width, height)
    image(player, playerX, playerY, playerW, playerH)
    image(friend, friendX, friendY, friendW, friendH) 
    
    #Instructions
    fill(255)
    textSize(30)
    text("Instructions:", 20,170)
    noStroke()
    ellipse(20, 200, 10, 10)
    text("Use the arrow keys to move in the following directions:", 30, 210)
    text("UP(FORWARD), LEFT(LEFTWARD), RIGHT(RIGHTWARD) and", 20, 250)
    text("DOWN(BACKWARD).", 20, 280)
    ellipse(20, 300, 10, 10)
    text("Collect the presents to earn points. Don't forget to give the" , 30, 310)
    text("presents to your friend after collection." , 30, 340)
    fill(0)
    text("Press any key to start the game.....", 190, 370)

    
def keyPressed():
    global stageNum, startTime, playerX, playerY
    if stageNum==0:
       stageNum = 1
       startTime = millis()
    if keyCode==UP:
          playerY = playerY - 3
    if keyCode==LEFT:
          playerX = playerX - 3 
    if keyCode==RIGHT:
          playerX = playerX + 3 
    if keyCode==DOWN:
          playerY = playerY + 3
    
#Start game    
def drawGamePlayLevel1():
    global carW, carH, score, stageNum, carCounted, giftCounted, giftVisible, running, currentTime, startTime,  playerX, playerY
    currentTime = millis() - startTime
    image(imgRoad, 0, 0, width, height)  
    image(friend, friendX, friendY, friendW, friendH) 
   
    for i in range(stage1Car):
        if (carCounted[i]==False and running==True):
           image(carsTop[i], carXTop[i], carYTop[i], carW, carH) 
           carXTop[i] = carXTop[i] + carsTopdx
           if (carXTop[i] > width): 
                carXTop[i] = -150
                carYTop[i] = 150
                carW = 150
                carH = 75
                
        #p stands for player
        pLeft = playerX
        pRight = playerX + playerW
        pTop = playerY
        pBottom = playerY + playerH
        
        #e stands for enemy, i.e., the cars
        #Top cars
        eLeftTop = carXTop[i]
        eRightTop = carXTop[i] + carW
        eTopTop = carYTop[i]
        eBottomTop = carYTop[i] + carH

        # Collision between top cars and player
        if ((carCounted[i]==False and running==True and eTopTop+10<pBottom-10 and pTop<eBottomTop-10 and eLeftTop<pRight-5 and pLeft+10<eRightTop)
                or (score<=2 and (currentTime/1000)>30)):
                carCounted[i] = True
                running = False   
                stageNum = 3    
            
    for i in range(stage1Car):
        if (carCounted[i]==False and running==True):
           image(carsBottom[i], carXBottom[i], carYBottom[i], carW, carH)
           carXBottom[i] = carXBottom[i] + carsBottomdx 
           if (carXBottom[i] < -carW): 
                carXBottom[i] = width
                carYBottom[i] = 275
                carW = 150
                carH = 75
                
        #Bottom cars
        eLeftBottom = carXBottom[i]
        eRightBottom = carXBottom[i] + carW
        eTopBottom = carYBottom[i]
        eBottomBottom = carYBottom[i] + carH
        
        # Collision between bottom cars and player
        if ((carCounted[i]==False and running==True and eTopBottom+10<pBottom-10 and pTop<eBottomBottom-10 and eLeftBottom<pRight-5 and pLeft+10<eRightBottom)
                or (score<=2 and (currentTime/1000)>30)):
                carCounted[i] = True
                running = False 
                stageNum = 3
                
    for i in range(stage1Gift):
        if (giftCounted[i]==False and giftVisible[i]==True):
           image(gifts[i], giftX[i], giftY[i], giftW, giftH)
        
        #g stands for gift
        gLeft = giftX[i]
        gRight = giftX[i] + giftW
        gTop = giftY[i]
        gBottom = giftY[i] + giftH
           
        #Collision between gifts and player  
        if (giftCounted[i]==False and giftVisible[i]==True and gTop<pBottom and pTop<gBottom and gLeft<pRight and pLeft<gRight):
              score = score + 1 
              giftCounted[i] = True
              giftVisible[i] = False 
              
        #f stands for friend
        fLeft = friendX
        fRight = friendX + friendW
        fTop = friendY
        fBottom = friendY + friendH
        
        #Collision between player and her friend
        if (score==2 and (currentTime/1000)<=30 and fTop<pBottom and pTop<fBottom and fLeft<pRight and pLeft<fRight):
              stageNum = 2  
              running = True
              score = 0
              carCounted[i] = False
              startTime = millis()
              playerY = height - 120
              
        fill(255)
        textSize(25)    
        text("Level 1: You have 30 seconds!", 600, 50) 
        fill(0)
        textSize(30)   
        text("Time:"+str(currentTime/1000)+"s", 20, 30)
        text("Score:"+str(score), 20, 70)
    
    image(player, playerX, playerY, playerW, playerH)
        
def drawGamePlayLevel2():
    global carW, carH, score, stageNum, carCounted, giftCounted, giftVisible, running, currentTime, startTime,  playerX, playerY
    currentTime = millis() - startTime
    image(imgRoad, 0, 0, width, height)  
    image(friend, friendX, friendY, friendW, friendH) 
    
    for i in range(stage2Car):
        if (carCounted[i]==False and running==True):
           image(carsTop[i], carXTop[i], carYTop[i], carW, carH) 
           carXTop[i] = carXTop[i] + carsTopdx + 1
           if (carXTop[i] > width): 
                carXTop[i] = -150
                carYTop[i] = 150
                carW = 150
                carH = 75
                
        #p stands for player
        pLeft = playerX
        pRight = playerX + playerW
        pTop = playerY
        pBottom = playerY + playerH
        
        #e stands for enemy, i.e., the cars
        #Top cars
        eLeftTop = carXTop[i]
        eRightTop = carXTop[i] + carW
        eTopTop = carYTop[i]
        eBottomTop = carYTop[i] + carH
        
        # Collision between top cars and player
        if ((carCounted[i]==False and running==True and eTopTop+10<pBottom-10 and pTop<eBottomTop-10 and eLeftTop<pRight-5 and pLeft+10<eRightTop)
                or (score<=1 and (currentTime/1000)>25)):
                carCounted[i] = True
                running = False   
                stageNum = 3       
                
    for i in range(stage2Car):
        if (carCounted[i]==False and running==True):
           image(carsBottom[i], carXBottom[i], carYBottom[i], carW, carH)
           carXBottom[i] = carXBottom[i] + carsBottomdx -1
           if (carXBottom[i] < -carW): 
                carXBottom[i] = width
                carYBottom[i] = 275
                carW = 150
                carH = 75          
        
        #Bottom cars
        eLeftBottom = carXBottom[i]
        eRightBottom = carXBottom[i] + carW
        eTopBottom = carYBottom[i]
        eBottomBottom = carYBottom[i] + carH
        
         # Collision between bottom cars and player
        if ((carCounted[i]==False and running==True and eTopBottom+10<pBottom-10 and pTop<eBottomBottom-10 and eLeftBottom<pRight-5 and pLeft+10<eRightBottom)
                or (score<1 and (currentTime/1000)>25)):
                carCounted[i] = True
                running = False 
                stageNum = 3    
            
    for i in range(2,3):
        if (giftCounted[i]==False and giftVisible[i]==True):
           image(gifts[i], giftX[i], giftY[i], giftW, giftH)
        
        #g stands for gift
        gLeft = giftX[i]
        gRight = giftX[i] + giftW
        gTop = giftY[i]
        gBottom = giftY[i] + giftH  
        
        #Collision between gifts and player   
        if (giftCounted[i]==False and giftVisible[i]==True and gTop<pBottom and pTop<gBottom and gLeft<pRight and pLeft<gRight):
              score = score + 1 
              giftCounted[i] = True
              giftVisible[i] = False
              
        #f stands for friend
        fLeft = friendX
        fRight = friendX + friendW
        fTop = friendY
        fBottom = friendY + friendH   
         
        #Collision between player and her friend
        if (score==1 and (currentTime/1000)<=25 and fTop<pBottom and pTop<fBottom and fLeft<pRight and pLeft<fRight):
              stageNum = 4  
                     
        fill(255)
        textSize(25)    
        text("Welcome to Level 2!", 600, 30) 
        text("Just 1 gift in 25 seconds for a WIN!", 550, 60)
        fill(0)
        textSize(30)   
        text("Time:"+str(currentTime/1000)+"s", 20, 30)
        text("Score:"+str(score), 20, 70)
    
    image(player, playerX, playerY, playerW, playerH)
                
def drawGameOverPage():
    image(restart, restartX, restartY, buttonW, buttonH)
    image(gameEnd, gameEndX, gameEndY, buttonW, buttonH)
    fill(255,0, 0)
    textSize(70)
    text("GAME OVER!", 300, 250)  

def drawWinPage():
    image(restart, restartX, restartY, buttonW, buttonH)
    image(gameEnd, gameEndX, gameEndY, buttonW, buttonH)
    fill(255,0, 0)
    textSize(70)
    text("YOU WIN!", 350, 250) 
    
#Restart the game
def mousePressed():
    global stageNum, score, running, carCounted, giftCounted, giftVisible 
    if (mouseX >= gameEndX and mouseX <= gameEndX + buttonW and mouseY >= gameEndY and mouseY <= gameEndY + buttonH):   
        exit() #Exit game
    elif (mouseX >= restartX and mouseX <= restartX + buttonW and mouseY >= restartY and mouseY <= restartY + buttonH):
        stageNum = 0
        score = 0
        running = True
        setup()
   
         
          
        
          
