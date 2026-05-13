# Asteroids - V 1.0
#### Python 3.13.12 

A simple version of the Asteroids arcade game. Shoot asteroids and survive!


### <u>Features</u>
* Menu Screen & Scoring System
* Score points by shooting asteroids
* Shoot up to 3 shots per second with your spacebar
* move with WASD
* Asteroids will explode into smaller ones
* Venture off the window if you dare!
* ***New***: screen wrapping for asteroids & player
* ***New***: sound effects 
    * clone repo to your native computer OS to play w/ sound
    * if you use wsl, it likely wont work, check out the .wav bleeps
* ***New***: Cyan spaceship that fires out red shots
* ***New***: Asteroid-Asteroid collision creates chaos w/out clutter
    * My AI Agent wrote this feature. Check out the prompt here for the process.
    * ***New***: Slight randomness to collision interactions (Angles & Speed)
    * LLM powered Agent comment notes left in.
        * Some variable names were adjusted, notes line up w/ code still

### <U>Requirements</u>
* pygame 2.6.1
* random
***
* *Note: this repository is managed by uv*
    * to run the game after cloning: `uv run main.py` 
