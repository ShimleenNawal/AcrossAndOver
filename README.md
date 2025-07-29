# __Across And Over__
An interactive game to test your instincts and time management skills!


## Background & Storyline
On a bright sunny day, a woman is trying to cross a busy street to meet her friend waiting on the opposite side. The goal is to collect presents scattered across the road for her friend's birthday. Sounds easy, right? Except you have to avoid rushing cars speeding **right at you**. (*Yikes!*) The challenge involves **strategic** movement, **timely** collection, and quick reflexes to prevent collisions. *Across and Over* is a **straight-forward** and **user-friendly** game with two **fun** levels!

*Processing* with Python has been used to develop the game and its dynamic gameplay, symbolizing the test of friendship and the hardships we have to overcome to prove our loyalty to our friends, even if that means we get hurt sometimes. :)

## Characters & Elements
1. __The Woman__: The main player-controlled character attempting to cross and collect presents.
   
2. __Her Friend__: Waiting across the street, signaling the win condition when reached.

3. __Cars__: Moving obstacles in upper and lower halves of the screen, traveling in opposite directions.

4. __Presents__: Items randomly appearing on the screen for collection.
   

## Features
- __Interactive Controls__: Use the arrow keys (UP, DOWN, LEFT, RIGHT) to move the character in all directions.

- __Collectible Presents__: Gather presents to earn points; each collected present increases the score.

- __Dynamic Obstacles__: Moving cars in both directions, with random speeds, create real-time challenges.

- __Time & Score Tracking__: A timer counts elapsed seconds; scores increase with each present collected.

- __Win & Lose Conditions__:  

  - __Win__:
     - Level 1: Collect 2 presents within 30 seconds and reach the friend. The speedy cars rushing constantly are the main obstacles.
     - Level 2: Collect only **ONE** present! The twist? You're given 25 seconds and of course, cars with higher speed coming right at ya! :)     
  - __Lose__: Collide with a car or run out of time before collecting all presents.


## Gameplay 
- __Start__: Press any key on the Welcome Page to begin.

- __Navigation__: Use arrow keys to move the woman around the screen.

- __Objective__: Collect presents to increase the score while avoiding moving cars.
- __Timing__: The game starts a timer upon beginning; players must collect all presents within the timeframes.

- __Game Over Conditions__:  

  - Collision with a car.  

  - Time exceeds without collecting the presents OR Presents are collected but not given to friend in time.  

  - Collecting all presents and reaching the friend before time runs out.

- __Winning__: Successfully collecting all presents within time limit and reaching the friend results in a "YOU WIN" message.

- __Losing__: Collisions or timeout results in a "GAME OVER" message.


## Simple steps to enjoy the game:
1. __Download *Processing*__: Make sure to install [Processing](https://processing.org/download).
2. __Install Python Mode__: Open Processing app. Go to `Tools` > `Add Tool` > `Modes`, and select Python Mode.
3. __Clone/Download this Repository__:
   ```
      git clone https://github.com/YourUsername/AcrossAndOver.git
      cd AcrossAndOver
   ```
5. __Open and Run__: Open the `.pyde` file in Processing and enjoy the game~
