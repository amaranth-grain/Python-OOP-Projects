

  <h3 align="center">Assignment 2</h3>

  <p align="center">
    COMP 3522 Assignment 2 - Card Management App
    <br />



## Getting Started

To get a local copy up and running follow these simple steps.

1. Clone the repo
```sh
git clone https://github.com/amaranth-grain/3522_A01041926.git
```
2. Run in your preferred IDE (e.g. PyCharm).  Game will display in console.  Some characters may not display if you are not on UTF-8.
3. Run **card_management.py** to begin.



## Usage

Manage your cards with **One-der Card**, your one-stop shop for managing all the cards in your overflowing wallet.

The card management app can handle many types of cards:

1. Loyalty reward cards 
   e.g. stamp cards, "Buy X get Y Free" cards
2. Gift cards / transit fare cards
3. Basic ID Cards / business cards
4. Credit or debit cards
5. Government ID cards
   e.g. BCServices Card, Driver's License
6. Membership card / tickets



## Features

It offers the following **functionality**:

1. View all stored cards
2. View cards by the types listed above
3. Add cards of different types (see above)
4. Search for card by
   a. Issuer name
   b. ID
5. Delete a card by searching through type, and identifying the card you want to delete
6. Back up data in JSON format.



## Limitations

- It was difficult to perform unit testing as my system hinges on user input.
  I imported unittest.mock to use patch, but it would only take the first input given.  Two of my unit tests fail as a result.

- Validation and error handling are very difficult to anticipate.
  I have tried my best by handling errors gracefully.

  Some examples:
  (a) Converting incompatible into int
  (b) int value outside of menu option selection range
  (c) Weight and height attributes cannot be negative
  (d) Forcing user to select most options by picking from a menu instead of freeform inputs.
  (e) Empty inputs or whitespace only are not accepted.



## Reflection

- It was easier to design the system this time, but as it took a lot of user inputs, the validation and error handling were rather difficult for me to complete.  I feel like I'm probably still missing some glaring mistakes.
- I will probably need some guidance for unit testing with user inputs as it is very confusing.
