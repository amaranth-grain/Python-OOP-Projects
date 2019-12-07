## COMP 3522 Assignment 5

#### **Introduction**

Assignment involves using AsyncIO to make API calls to speed up I/O bound problem.  The user can specify whether they want to query for POKEMON, ABILITY, or MOVE.  They can search a single query, or multiple ones from a .txt file.  The output can be either printed to the console or saved to the specified output file (where a new one will be created if it does not exist).



#### Limitations

- The program is not fully implemented.  I tried to include the expanded Pokemon query, but felt like I was fighting against the Chain of Responsibility when I was implementing it.  In hindsight, I would not have used this design pattern.  And it's too late to refactor, so it is as it stands.  I have successfully made the API calls on all subqueries and returned it in the following format:
  [ [ [Pokemon 1 Stats JSON], [Pokemon 2 Stats JSON] , ... ], 
  [ [Pokemon 1 Ability JSON], [Pokemon 2 Ability JSON] , ... ], 
  [ [Pokemon 1 Move JSON], [Pokemon 2 Move JSON] , ... ]]
  It is passed to the JSONSubqueryHandler, where I stopped.
  I would also refactor by passing a dictionary instead of a list, as it's not intuitive that index 0 is Stats, index 1 is Ability, and index 2 is Move.
- An error message gets printed at the end of the print console because awaiting two async functions meant the interpreter would complain that my async function wasn't awaited unless I awaited everything in the chain before it, all the way back to the starting handler (FileExtensionHandler)



#### Validation

- A lot of the validation is handled by argparse.
  Positional arguments MODE and STRING are handled by argparse if they are missing.
  Casting MODE to PokedexMode handles non MOVE, ABILITY, POKEMON input.
- I check whether the STRING is .txt or not.  If it is .txt, I open the file and lower() and strip() each line.
  If it is not, I make the API call.  I check whether my request.status is 200.
- For the output path, I check whether it ends in .txt or not.

#### Insights

- I tried to reuse the handlers in the chain of responsibility, but hijinks with async makes it difficult to use a chain.  I also feel like using a list of list of lists is a HORRIBLE choice, but I wanted to make all the subquery API calls in one session to avoid opening 20 or 30+ sessions for a single Pokemon.  But it meant that I had a list of list of lists, because I didn't want to bloat the Request object with stat_urls, stat_jsons, move_urls, move_jsons, ability_urls, ability_jsons, etc.

