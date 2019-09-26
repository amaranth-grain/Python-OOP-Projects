<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

  <h3 align="center">Assignment 1</h3>

  <p align="center">
    COMP 3522 Assignment 1 - Tamagotchi Simulator
    <br />



<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

1. Clone the repo
```sh
git clone https://github.com/amaranth-grain/3522_A01041926.git
```
2. Run in your preferred IDE (e.g. PyCharm).  Game will display in console.  Some characters may not display if you are not on UTF-8.
3. Run **game.py** to begin.



## Usage

Simulate a Tamagotchi by playing with Pokemon pets.

Upon starting the game, a Scorbunny, Crobat, or Sirfetch'd will automatically hatch:

![Pokemon Tamagotchi](./Tamagotchi.png)



Start game by running in Pycharm or other IDE.  

Game includes the following modules only:

- game.py
- peripherals.py
- pokemon.py



**IMPORTANT NOTE:**

**gameui.py** and **interaction.py** are not part of the game.  I had trouble deleting these after I refactored the code.



## Features

The game fulfills the requirements laid out for Assignment 1.

Some highlighted features:

#### Moods

Pokemon in this game are a bit moody and whimsical.  They're not afraid to tell you how they feel!

View the game on UTF-8 encoding for the best gaming experience.  

​                  ![Pokemon Tamagotchi](./pet_mood.png)            

#### **Food**

There are many food choices for your pet.

![Food menu in Tamagotchi game](./food_menu.png)                          

Depending on what you feed your pet, they may entirely refuse to eat it!

Play around to learn what they like.

#### Minigames

1. Guess that Pokemon!
   Type in the name of a starter Pokemon from any generation, and see if you guessed correctly.
2. Water, Fire, Grass
   The Pokemon version of Rock, Paper, Scissors is every bit as fun as the original.
3. Whack-a-Drilbur
   How many Drilburs can you whack?



## Limitations

- Because pet status isn't checked in real time, the game may print alternative results even after a pet has died (its health has reached 0 Health)
- "Invalid input. Try again." message only prints if you enter a non-integer.
  If the menu has three choices, and you enter an integer outside of 1, 2, 3, it will print the menu again but will not notify you that it is an invalid input.



## Reflection

- I learnt a lot about the Single Responsibility Principle through this assignment.  After a certain point, my game became untenable and difficult to maintain as any changes would require modifications in several places as well as a lot of debugging.
- I had trouble wrapping my mind around polymorphism in a dynamically typed language.  I don't think I understand it completely, but I know it's a lot easier to separate different responsibilities to different classes and have smaller classes than to deal with one that is large and difficult to read.
- Creating a Catalogue class which acts as a database full of items I can draw from (with methods to print out items after they are stored) helped immensely with trimming down unnecessary lines in other classes.


