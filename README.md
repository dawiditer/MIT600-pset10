# Object-oriented programming; graphical user interface for word game

We hope you enjoyed the word game from problem sets 5 & 6… because it’s back! In this problem set, you will fill in code for a
graphical version of the 6.00 word game, with support for single player, two player, and vs. computer game modes.
Along the way, you will implement classes to encapsulate and manage the data and functions for the word game. You will also
practice manipulating instances of these classes through methods. Finally, you will see your classes in action as they interact with
a graphical user interface (GUI) module for the 6.00 word game. 

### Problem 1: Install wxPython ###
Before you begin the problem set, you will need a toolkit for making a graphical user interface (GUI) in python. We will use the
wxPython toolkit for this purpose.
First make sure you have Python 2.5.2. You can check what version of Python you have by going to the **“Help”** menu and clicking
**“About IDLE”** from the Python Shell window in IDLE.
With Python 2.5.2 installed, you can download and install wxPython.

### Problem 2: Representing a Hand ###
In problem set 5, you managed a number of data structures and functions pertaining to a player’s hand. The data for the hand was
stored as a dictionary that mapped characters to their corresponding frequencies in the hand.
A number of functions were used to manage the hand: `deal_hand()` was used to initialize a new hand, `display_hand()`, was
used to print the hand to the screen in a readable format, `update_hand()` was used to remove the letters in a word from the
hand, and `is_valid_word()` used the hand to check if the letters necessary for making up a word were present.

We are now going to encapsulate the functions and data associated with a hand in a class called Hand. We have already provided
the constructor method, `__init__()`, which takes as an argument the initial size of the hand (the initialSize parameter).
The constructor also takes an optional second argument (the `initialHandDict` parameter), which is a dictionary representation
(mapping characters to frequencies) that is used to initialize the hand to a particular set of characters. This argument is used for
testing purposes. If no second argument is given, the constructor initializes the hand with random characters.
The class stores the initial size of the hand as the attribute self.initialSize and the dictionary representation for the hand as
the attribute `self.handDict`.

You will need to fill in the remaining functions according to the specifications to have a class representation of a hand.
Fill in the `update()`, `containsLetters()`, `isEmpty()`, and `__eq__()` methods in the Hand class according to the
specifications. Your implementation for each of these methods should be relatively short (probably around 10–20 lines or
fewer per method).
Feel free to make use of the solutions to problem set 5 and problem set 6 in your code. We have provided a skeleton test
harness in **ps10_test.py**. Use `testHand()` to test your Hand class. You should add additional tests to `testHand()` to
adequately test your Hand class. 

### Problem 3: Representing a Player ###
In problem sets 5 and 6, you initialized and managed the state of a player. You kept track of the player’s score, their remaining
time, and their current hand.
In this problem set, you will encapsulate this information in a Player class, except you are no longer keeping track of time. You
will write a set of methods to access and modify this data. We have provided the constructor method, `__init__()`, for the
Player class. The constructor takes as arguments an ID number (idNum) (either 1 for player 1 or 2 for player 2) and a Hand
object (hand) for the player’s hand and stores them as class attributes `self.idNum` and `self.hand`, respectively.
In this problem, you will fill in the remaining methods of the `Player` class according to the specifications to have a class
representation of a `Player`.

Fill in the `getHand()`, `addPoints()`, `getPoints()`, `getIdNum()` and `__cmp__()` methods in the `Player` class.
Again, your implementation for these methods should be very short.
We have provided a skeleton test harness in **ps10_test.py**. Use `testPlayer()` to test your `Player` class. You should
add additional tests to `testPlayer()` to adequately test your `Player` class. 

### Problem 4: Representing a Computer Player ###
A computer player can be thought of as a specialization of the `Player` class. Rather than implementing a class for the computer
player from scratch, we will simply have the `ComputerPlayer` class inherit from the `Player` class and add the
`pickBestWord()` method, which implements the computer player’s algorithm for picking the best word, given its hand and the
word list (a parameter of the method).

You should use the slow greedy algorithm that we implemented in problem set 6 (pick_best_word). The parameter wordlist
is an instance of class `Wordlist` (which is provided). It will be useful to look at the implementation of the `Wordlist` class that is
provided and make sure that you understand the methods available for a Wordlist instance.
Implement the `pickBestWord()` method in the `ComputerPlayer` class. As you reimplement the algorithm, if you are
adapting code from previous problem set solutions, you must make the code compatible with the classes in this problem set.
You should make use of the other classes to access information regarding the computer’s hand and the available words in
the word list.
We have provided a skeleton test harness in **ps10_test.py**. Use `testComputerPlayer()` to test your
`ComputerPlayer` class. You should add additional tests to `testComputerPlayer()` to adequately test your
`ComputerPlayer` class.

### Problem 5: The Graphical User Interface ###
Having implemented and tested the `Hand`, `Player`, and `ComputerPlayer` classes, you should now be able to run the game
using the graphical user interface.
When you start the GUI, you are presented with three options, corresponding to different game modes. Choosing one will show
the main game play window and prompt you so you can prepare to start playing. In **Solo mode**, you are a single player playing
through a hand. In **Vs. Computer mode**, you play first, then the computer player will play. In **Vs. Human mode**, you play first, then
your friend plays. In the **Vs. modes**, both players are dealt the same initial hand, so make sure your friend isn’t watching while you
play!

In the play window, you can enter your words in the text box and either hit **Enter** or press the **Submit** button. The status bar along
the bottom will display messages concerning whether your word was accepted, and accepted words will be added to the word
history list box. On the left and right you will see the stats displays for players 1 and 2, respectively. To end a hand, use up all
your characters or enter a `’.’`. You may also close the window at any time to stop the game.
When playing against the computer, you won’t be able to interact with the main window, but you can see the words that the
computer player chooses as it’s playing
