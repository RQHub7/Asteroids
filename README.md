# Asteroids - V 1.0
#### Python 3.13.12 

A simple version of the Asteroids arcade game. Shoot asteroids and survive!



https://github.com/user-attachments/assets/911f4ee4-5ad6-4b25-94e7-8b7eb19e927a





***
### <u>Features</u>
* Menu Screen & Scoring System
* Score points by shooting asteroids
* **Shoot up to 3 shots per second with your spacebar**
* **Move with WASD**
* Asteroids will explode into smaller ones
* Venture off the window if you dare!
* ***New***: Screen Wrapping
   * Asteroids & Player
* ***New***: Sound Effects  
    * Sound effects were all self recorded using Audacity
    * Clone repo to your native computer OS to play w/ sound
    * *NOTE:* If you use WSL, sounds likely wont come through, check out the .wav bleeps at least
       * See installation instructions to play on Windows 
* ***New***: Cyan spaceship that fires out red shots
* ***New***: Asteroid-Asteroid collision creates chaos w/out clutter
    * My AI Agent wrote this feature. Check out the prompt here for the process.
    * ***New***: Slight randomness to collision interactions (Angles & Speed)
    * LLM powered Agent comment notes left in.
        * Some variable names were adjusted, notes line up w/ code still
***
### <U>Requirements</u>
* pygame 2.6.1
* random
* uv
   * Repository: https://github.com/astral-sh/uv
   * Webpage: https://docs.astral.sh/uv/getting-started/installation/
***
### Installation
* *Note: this repository is managed by uv*
    * Make sure python and uv are installed on system (uv will handle the venv w/ python & pygame versions)
    * Navigate to a good destination folder/directory in powershell and run `git clone https://github.com/RQHub7/Asteroids.git`
***
### Run/Play
   * cd into Asteroids from your chosen folder `cd Asteroids` (still using powershell or terminal)
   * `uv run main.py` - You should see the pygame window as shown above now.
   * **Mouse (left click) for Game Menu, WASD & SPACE to pilot & shoot**
