# pygame-Basic-content-of-a-game
The basic content of a game, including start interface, home page, menu, exit interface, level selection, scene switching, animation, shooting, collision detection, neural network pathfinding and other functions. This is just the basic content of a game. The game design is unreasonable, and the loading interface is pseudo asynchronous loading

scene:
    -Start scene,
    -homepage,
    -Loading interface,
    -Exit the game interface,
    -Level selection interface,
    -Create new archive interface(It can only be opened after the game has been run),
    -About interface,
    -Setting interface,
    -menu,
    -7 game scenes,
    
There are seven game scenes in the game, but only the first one has an environment (it's not written because the game optimization is not good)

NPC neural network is a simple three-layer neural network, including an input layer, a hidden layer and an output layer
The neural network obtains the player's coordinates and its own coordinates to calculate the moving direction, and the training and operation are carried out at the same time, so the NPC will be silly at the beginning
Activation function: S function
    
