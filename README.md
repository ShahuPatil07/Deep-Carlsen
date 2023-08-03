# Deep-Carlsen
In this project, I tried to make a chess engine which is able to compare moves and the best one at a pretty good accuracy.
Initially, I developed entire chess game using Pygame library. That itself included a lot of hardcoding. 
### Here are few problems that I faced during this:
* In the dragging process, I needed to know whether piece is dragged at a square where it's a valid move. For that I had to loop through all valid moves and compare them. But how to compare 2 moves as it was just an object under Move class. Solution was to compare initial and final squares of that move (this is a method in move.py). And for comparing squares, I had to define an equilizer method in Square.py where we check if row1= row2 and column1=column2 to verfy equality.
* When we touch a piece but dont move it, in our next move we face a huge issue. For instance if game goes like e4, e5, and I touch white king but not move it and I play be2, and whatever black plays, in the next move I was able to capture my bishop with my king. After debugging a lot, solution to this was to edit main.py where if (released row == initial row ) && (released col == initial col) then we clear the calculated moves of our dragged piece.
* Problem in in_check method in board.py: To check whether a 'normally' playable move is valid with considering check rules, we are supposed to play that move and iterate through all enemy pieces and check if any piece can capture our king (To check if it's a check). But we can't change board position. Solution I came up with for this was using an imaginary board to calculate. Basically import 'copy' library and use that imaginary board as an exact copy of our current board.
### From player vs player to Self playing engine:
* After a basic player vs player engine was built, I had to build the AI part of it. For this I studied a lot and found out encoding complex networks like Deep Q learing was a bit tough for me as I made the chess game using Pygame and not the available chess library. That's why I have used stockfish evaluation to predict best move for my engine.
* For getting correct evaluation of my position, I needed to convert my Pygame engine to FEN format which is accepted by stockfish. For this I made a function board_to_fen in board.py which returns the string format of current position which is further used by stockfish to evaluate the same.
* To get the best move I made a function best_move in stockfish_play.py where the reward function is (evaluation after move played - evaluation before the move). This way I iterated through all moves again using copy of current board and returned the best move.
### Now let's talk about what every does:
* main.py- It's the operational file from where we run our game.
* backg.py- It is responsible for all what is displayed on the screen.
* board.py- probably the most important. All the chess rules are stored here, backend of what happens when a move is excecuted, also conversion of my chess board to FEN string is done here and a lot more.
* square.py- Used to determine what a particular square consists of (team piece, enemy piece, empty etc)
* stockfish_play.py- Used for engine to predict the best move.
* piece.py- consists of all properties of a piece.
* move.py- defines attributes that a move contains.
* drag.py- Helps in implementing the drag functionality of a piece.
  ### Results:
  
